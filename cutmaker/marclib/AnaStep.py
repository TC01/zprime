# AnaStep: Takes a step in the Analysis (multiple dists).
import os
import math
import ROOT
#from ROOT import *
import sys
from SimpleCutSequencer import *
from anadist import *

class dist:
	def __init__(self, path, name, color, scale, w):
		self.path = path
		self.name = name
		self.color = color
		self.scale = scale
		self.w = w
	def getPath(self):
		return self.path
	def getName(self):
		return self.name
	def getColor(self):
		return self.color
	def getScale(self):
		return self.scale
	def getWeight(self):
		return self.w

class cut:
	def __init__(self, cut, name):
		self.cut = cut
		self.name = name
	def getCut(self):
		return self.cut
	def getName(self):
		return self.name
class pile:
	def __init__(self, tree):
		self.Bkg = []
		self.Sig = []
		self.Cuts = []
		self.tree = tree
	def nameTree(self):
		return self.tree
	def addBkg(self, BKG):
		self.Bkg.append(BKG)
	def getBkg(self, n):
		return self.Bkg[n]
	def addSig(self, SIG):
		self.Sig.append(SIG)
	def getSig(self, n):
		return self.Sig[n]
	def addCut(self, CUT):
		self.Cuts.append(CUT)
	def getCuts(self):
		return self.Cuts
	def numBkg(self):
		return len(self.Bkg)
	def numSig(self):
		return len(self.Sig)
	def numCuts(self):
		return len(self.Cuts)
	
	
# That was just setup. Now the real function:
class AnaStep:
	def __init__(self, name, PILE, lumi, var, bins, save, title):
		out_tmp = ROOT.TFile("DELETEMEIFYOUWANT.root", "recreate") # not a real file! Acts as (slow) ram for moving Trees.
		# # # # # # #
		numB = PILE.numBkg()
		numS = PILE.numSig()
		numC = PILE.numCuts()
		cuts = []
		cutnames = []
		self.sig_plots = []
		self.bkg_plots = []
		bkgcol = []
		bkgnames = []
		sigcol = []
		signames = []
		for c in range(numC):
			cuts.append(PILE.getCuts()[c].getCut())
			cutnames.append(PILE.getCuts()[c].getName())
		for b in range(numB):
			bkgcol.append(PILE.getBkg(b).getColor())
			bkgnames.append(PILE.getBkg(b).getName())
			tmp_bfile = ROOT.TFile(PILE.getBkg(b).getPath())
			tmp_tree = tmp_bfile.Get(PILE.nameTree())
			out_tmp.cd()
			tmp = SimpleCutSequencer(tmp_tree, cuts, var, name+"_"+PILE.getBkg(b).getName(), bins, lumi*PILE.getBkg(b).getScale(), PILE.getBkg(b).getWeight())
			tmp.DrawSequence(name+"_"+PILE.getBkg(b).getName(), cutnames, PILE.getBkg(b).getName(), PILE.getBkg(b).getColor())
			self.bkg_plots.append(tmp.getPlots("last"))
			if save == 'yes':
				tmp_savefileb = ROOT.TFile(PILE.getBkg(b).getName()+'_'+name+".root", 'recreate')
				tmp_savefileb.cd()
				tmp_savetreeb = tmp.getTree().CopyTree('')
				tmp_savetreeb.SetName('tree')
				tmp_savefileb.Write()
				tmp_savefileb.Close()
		for s in range(numS):
			sigcol.append(PILE.getSig(s).getColor())
			signames.append(PILE.getSig(s).getName())
			tmp_sfile = ROOT.TFile(PILE.getSig(s).getPath())
			tmp_tree = tmp_sfile.Get(PILE.nameTree())
			out_tmp.cd()
			tmp = SimpleCutSequencer(tmp_tree, cuts, var, name+"_"+PILE.getSig(s).getName(), bins, lumi*PILE.getSig(s).getScale(), PILE.getSig(s).getWeight())
			tmp.DrawSequence(name+"_"+PILE.getSig(s).getName(), cutnames, PILE.getSig(s).getName(), PILE.getSig(s).getColor())
			self.sig_plots.append(tmp.getPlots("last"))
			if save == 'yes':
				tmp_savefiles = ROOT.TFile(PILE.getSig(s).getName()+'_'+name+".root", 'recreate')
				tmp_savefiles.cd()
				tmp_savetrees = tmp.getTree().CopyTree('')
				tmp_savetrees.SetName('tree')
				tmp_savefiles.Write()
				tmp_savefiles.Close()
		# now make the final plot:
		data = data = ROOT.TH1F("data", "data", bins[0], bins[1], bins[2])
		thestack = multidist("stack", self.bkg_plots, self.sig_plots, data, bkgcol, sigcol, [bins[1], bins[2]])
		thestack.PLOTSTACKS(name, bkgnames, signames, "Data", [0.7,0.7,0.89,0.89], var, title)
		thestack.PLOTSTACKS('log_' + name, bkgnames, signames, "Data", [0.7,0.7,0.89,0.89], var, title + "(Logarithmic)", True)
	
	def getBkgPlots(self):
		return self.bkg_plots

	def getSigPlots(self):
		return self.sig_plots




		
