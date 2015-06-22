# SimpleCutSequencer:
# Takes a vector of cuts (Strings) and applies them.

# Should now be renamed "ComplexCutSequencer" because...
# ...
# ...well...
# it's not entirely my fault!
# --bjr

import os
import math
import ROOT
from ROOT import *
import sys
from OneCut import *

class SimpleCutSequencer:
	def __init__(self, tree, cuts, var, name, bins, scale):
		self.var = var
		self.num_cuts = len(cuts)
		self.tree = tree
		self.plots = []
		for i in range(self.num_cuts):
			step = OneCut(self.tree, cuts[i])
			step.printVals()
			self.tree = step.getTree("step_" + str(i+1))
			self.plots.append(step.getPlot(self.var, name+"@step_"+str(i+1), bins[0], bins[1], bins[2], scale))
	def getPlots(self, o):
		if o == "all":
			return self.plots
		else:
			return self.plots[self.num_cuts]
	def DrawSequence(self, name, cut_names, leg, color):
		rows = findrows(self.num_cuts)
		leg = TLegend(0.72, 0.72, 0.89, 0.89)
		leg.SetLineColor(0)
		leg.SetFillColor(0)
		leg.AddEntry(self.plots[0], name, "L")
		c = TCanvas("Sequencer","Sequencer", 1200, 370*rows)
		c.Divide(3, rows)
		for i in range(self.num_cuts):
			c.cd(i+1)
			self.plots[i].GetXaxis().SetTitle(self.var + " with cut: " +cut_names[i])
			self.plots[i].GetXaxis().SetTitleSize(0.04)
			self.plots[i].GetYaxis().SetTitle("events   ")
			self.plots[i].GetYaxis().SetTitleSize(0.045)
			self.plots[i].GetYaxis().SetTitleOffset(1.15)
			self.plots[i].SetLineWidth(3)
			self.plots[i].SetLineColor(color)
			self.plots[i].Draw()
			leg.Draw()
		c.SaveAs(name+".png")
		c.SaveAs(name+".pdf")
		return c			

def findrows(num):
	if num < 4:
		return 1
	elif num < 7 and num > 3:
		return 2
	elif num < 10 and num > 6:
		return 3
	else:
		return 4

class QCDSequencer(SimpleCutSequencer, object):

	def __init__(self, trees, cuts, var, name, bins, scales, tempfile):
		self.var = var
		self.num_cuts = len(cuts)
		self.plots = []
		self.tempfile = tempfile

		working_trees = []
		files = []

		for i in range(len(trees)):
			tfile = TFile(trees[i])
			tree = tfile.Get("UnmergedEvents")
			tree.SetName("UnmergedEvents_" + str(i))
			self.tempfile.cd()
			working_trees.append(tree)
			files.append(tfile)
			print working_trees

		self.tempfile.cd()
		print working_trees
		for i in range(self.num_cuts):
			for j in range(len(trees)):
				self.tempfile.cd()
				step = OneCut(working_trees[j], cuts[i])
				step.printVals()
				working_trees[j] = step.getTree("step_" + str(i+1) + "_QCD" + str(j+1))
				plot = step.getPlot(self.var, name+"@step_"+str(i+1) + "_QCD" + str(j+1), bins[0], bins[1], bins[2], scales[j])
				if len(self.plots) == i:
					self.plots.append(plot)
				else:
					self.plots[i].Add(plot)


	def DrawSequence(self, name, cut_names, leg, color, canvas=None):
		self.tempfile.cd()
		canvas = super(QCDSequencer, self).DrawSequence(name, cut_names, leg, color, canvas)
		return canvas
