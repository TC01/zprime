# OneCut:
# Makes one cut on a tree, keeps all the info.
import os
import math
import ROOT
from array import array
#from ROOT import *
import sys

class OneCut:
	def __init__(self, father, cuts): #Makes the cut on a tree
		self.NumFather 	= father.GetEntries() 
		self.Son	= father.CopyTree(cuts)
		self.NumSon	= self.Son.GetEntries()
	def getTree(self, name): #Returns the new tree
		self.Son.SetName(name)
		return self.Son
	def printVals(self): #Numbers and Percentages (as a vector of doubles)
		Vals = []
		Vals.append(self.NumFather)
		Vals.append(self.NumSon)
		Vals.append(self.NumSon/self.NumFather)
		Vals.append(100*self.NumSon/self.NumFather)
		print '-- Original Tree had '+str(self.NumFather)+' events.'
		print '-- New Tree has '+str(self.NumSon)+' events.'
		if self.NumFather > 0:
			print '--        Efficiency: {0:4.3}%'.format(100*float(self.NumSon)/float(self.NumFather))
		return Vals
	def getPlot(self, var, name, bins, minbin, maxbin, scale): #Returns a formatted binned histogram for quick plotting
		plot = ROOT.TH1F(name, name, bins, minbin, maxbin)
		self.Son.Draw(var+">>"+name,"", "goff")
		plot.Scale(scale)
		plot.SetStats(0)
		plot.SetTitle("")
		return plot
	def getPlotByEvent(self, var, name, bins, minbin, maxbin, scale): # same as above, but with weighted events
		plot = ROOT.TH1F(name, name, bins, minbin, maxbin)
		x = array('f', [-1.0])
		w = array('f', [-1.0])
		self.Son.SetBranchAddress(var, x)
		self.Son.SetBranchAddress('weight', w)
		n = self.Son.GetEntries()
		for j in range(0, n):
			self.Son.GetEntry(j)
			plot.Fill(x[0],w[0])
		self.Son.ResetBranchAddresses()
		plot.Scale(scale)
		plot.SetStats(0)
		plot.SetTitle("")
		return plot
			
