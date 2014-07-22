import os
import glob
import math
import ROOT
from ROOT import *
import sys

from anadist import *
from CLASS_FullEvent_colt import *
from CLASS_QCD_FullEventStacker import *

import SimpleCutSequencer

def getSigFiles(energy = "1500GeV"): 
	files = []
	suffixes = ["2WP", "WM", "2WM", "WP"]
	root = "Gstar_Hadronic_" + energy + "_"
	for suffix in suffixes:
		files.append(root + suffix + "_ntuples.root")
	return files
		

def getFileName(type):
	"""Unfortunately, I had to hardcode this."""
	if type == "ttbar_s":
		return "TTBAR_semi.root"
	if type == "ttbar_h":
		return "TTJets_HadronicMGDecays_8TeV-madgraph.root"
	if type == "ttbar_l":
		return "TllTBAR_fu.root"
	if type == "wjets":
		return "WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball.root"

	return ""

def getTreeName(channel):
	tree = "UnmergedEvents"
	return tree	

def getHistogram(file, var, trees, bins, cut, isQCD):
	if isQCD:
		qcd_stack = QCD_stack(file, var, trees, bins, cut)
		hist = qcd_stack.GetStack()
	else:
		workingColt = colt(file, var, trees, bins, cut, var)
		hist = workingColt.GetHist()
	return hist

def makeSingleHistogram(file, vars, trees, bins, cuts, isQCD=False):
	if len(vars) != len(cuts):
		print "ERROR."
		return None

	hist = getHistogram(file, vars[0], trees, bins, cuts[0], isQCD)
	for i in range(len(vars) - 1):
		var = vars[i + 1]
		cut = cuts[i + 1]
		newHist = getHistogram(file, var, trees, bins, cut, isQCD)
		hist.Add(newHist)

	return hist

def sequenceCuts(filename, treenames, cuts, cutnames, variable, name, bins, scale, color, tempfile):
	file = TFile(filename)
	if len(treenames) == 1:
		tree = file.Get(treenames[0])

	else:
		print "NotImplementedError!"

	tempfile.cd()
	sequencer = SimpleCutSequencer.SimpleCutSequencer(tree, cuts, variable, name, bins, scale)
	return sequencer

def doCutSequencing(name, cuts, cutnames, var, nbins, lower, upper, folder):
	bins = [nbins, lower, upper]
	lumi = 19800
	path = folder + "/"

	outf = TFile("test.root", "recreate")
	
#	sig_file = path + "Gstar_Hadronic_1500GeV.root"
#	name = "signal"
#	sequencer = sequenceCuts(sig_file, ["UnmergedEvents"], cuts, cutnames, var, name, bins, 0.37*2*0.68*0.2*19748/160000, kBlue, outf)
#	outf.cd()
#	canvas = sequencer.DrawSequence(name, cutnames, name, kBlue, canvas)

#	ttbar_had_file = path + getFileName("ttbar_h")
#	name = "ttbar"
#	sequencer = sequenceCuts(ttbar_had_file, ["UnmergedEvents"], cuts, cutnames, var, name, bins, 97.13*19748/10485781, kRed, outf)
#	outf.cd()
#	canvas = sequencer.DrawSequence(name, cutnames, name, kRed, canvas)

	# QCD: Ew.
	name = "qcd"
	xs = [34138.15, 1759.549, 113.8791, 26.9921, 3.550036, 0.737844, 0.03352235, 0.001829005]
	n = [6000000, 6000000, 4000000, 4000000, 4000000, 2000000, 2000000, 1000000]
	scales = []
	treenames = []
	for i in range(len(xs)):
		scales.append(xs[i] * 1 / n[i])
		treename = path + "QCD" + str(i+1) + ".root"
		treenames.append(treename)
	sequencer = SimpleCutSequencer.QCDSequencer(treenames, cuts, var, name, bins, scales, outf)
	canvas = sequencer.DrawSequence(name, cutnames, name, kYellow)
	outf.Close()

	raw_input()

def doPlotThings(name, cuts, vars, nbins, lower, upper, folder, log=False):
	# Get all the files and rescale them:
	bins = [nbins, lower, upper]
	lumi = 19800
	path = folder + "/"
	trees = []
	trees.append(getTreeName(""))
	
	sig_files = getSigFiles()
	sigmm_file = path + sig_files[0]
	sigmp_file = path + sig_files[1]
	sigpm_file = path + sig_files[2]
	sigpp_file = path + sig_files[3]

	sigpp_hist = makeSingleHistogram(sigpp_file, vars, trees, bins, cuts)
	sigpm_hist = makeSingleHistogram(sigpm_file, vars, trees, bins, cuts)
	sigmp_hist = makeSingleHistogram(sigmp_file, vars, trees, bins, cuts)
	sigmm_hist = makeSingleHistogram(sigmm_file, vars, trees, bins, cuts)

	#TTbar:
#	trees = ["UnmergedEvents_Mu", "UnmergedEvents_El"]
	ttbar_file = path + getFileName("ttbar_s")
	ttbar_hist = makeSingleHistogram(ttbar_file, vars, trees, bins, cuts)

	ttbar_lep_file = path + getFileName("ttbar_l")
	ttbar_lep_hist = makeSingleHistogram(ttbar_lep_file, vars, trees, bins, cuts)

	ttbar_had_file = path + getFileName("ttbar_h")
	ttbar_had_hist = makeSingleHistogram(ttbar_had_file, vars, trees, bins, cuts)

	#Wjets:
	# Temporary hack, I should rerun the hadronic treemaker on these.
	trees = ["UnmergedEvents_Mu", "UnmergedEvents_El"]
	wjets_file = path + getFileName("wjets") + ".derp"
	wjets_hist = makeSingleHistogram(wjets_file, vars, trees, bins, cuts)

	#QCD:
	trees = []
	trees.append(getTreeName(""))
#	trees = ["UnmergedEvents_Mu", "UnmergedEvents_El"]
	qcd_hist = makeSingleHistogram(path, vars, trees, bins, cuts, True)

	#DATA:
	data_file = path+"DATA.root"
	data_hist = makeSingleHistogram(data_file, vars, trees, bins, cuts)


	#RESCALING:
	sigmm_hist.Scale(lumi*0.37/160000)
	sigmp_hist.Scale(lumi*0.37/160000)
	sigpm_hist.Scale(lumi*0.37/160000)
	sigpp_hist.Scale(lumi*0.37/160000)
	ttbar_hist.Scale(lumi*97.13/25424818)
	wjets_hist.Scale(lumi*33836.9/57653686)
	qcd_hist.Scale(lumi)

	signal = sigpp_hist
	signal.Add(sigmm_hist)
	signal.Add(sigmp_hist)
	signal.Add(sigpm_hist)

	#### START THE PLOTTING PART:
	bkg = [wjets_hist, qcd_hist, ttbar_had_hist]
	sig = [signal]
	bkgcol = [kGreen, kYellow, kRed, kRed+1, kRed-1]
	sigcol = [kBlue]
	bkgnames = ["W+jets", "QCD", "Hadronic TTbar"]
	signames = ["G*, 1.5 TeV Hadronic"]
	mw = [bins[1], bins[2]]
	legsize = [0.6,0.6,0.89,0.89]
	
	thestack = multidist("stack", bkg, sig, data_hist, bkgcol, sigcol, mw)
	thestack.PLOTSTACKS(name, bkgnames, signames, "Data", legsize, name, log)
	return thestack
