# SimpleCutSequencer:
# Takes a vector of cuts (Strings) and applies them.
import os
import math
import ROOT
#from ROOT import *
import sys
from OneCut import *

class SimpleCutSequencer:
	def __init__(self, tree, cuts, var, name, bins, scale, weights):
		self.var = var
		self.num_cuts = len(cuts)
		self.tree = tree
		self.plots = []
		with open('output.log', 'ab') as logfile:
			logfile.write('Applying cuts to: ' + name + '\n')
		for i in range(self.num_cuts):
			step = OneCut(self.tree, cuts[i])
			step.printVals()
			self.tree = step.getTree("step_" + str(i+1))
			if weights == "no":
				self.plots.append(step.getPlot(self.var, name+"@step_"+str(i+1), bins[0], bins[1], bins[2], scale))
			elif weights == "yes":
				self.plots.append(step.getPlotByEvent(self.var, name+"@step_"+str(i+1), bins[0], bins[1], bins[2], scale))
		with open('output.log', 'ab') as logfile:
			logfile.write('\n')
	def getTree(self):
		return self.tree
	def getPlots(self, o):
		if o == "all":
			return self.plots
		else:
			return self.plots[self.num_cuts-1]
	def DrawSequence(self, name, cut_names, leg_name, color):
		rows = findrows(self.num_cuts)
		leg = ROOT.TLegend(0.72, 0.72, 0.89, 0.89)
		leg.SetLineColor(0)
		leg.SetFillColor(0)
		leg.AddEntry(self.plots[0], leg_name, "L")
		c = ROOT.TCanvas("Sequencer","Sequencer", 1200, 370*rows)
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
		c.SaveAs(name+".pdf")
		c.SaveAs(name+".png")
			
def findrows(num):
	if num < 4:
		return 1
	elif num < 7 and num > 3:
		return 2
	elif num < 10 and num > 6:
		return 3
	else:
		return 4
