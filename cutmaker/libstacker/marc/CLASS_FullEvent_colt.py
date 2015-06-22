import os
import ROOT
from ROOT import *
import sys
from anadist import *

# CLASS:
class colt:
	def __init__(self, path, var, trees, bins, cut, name):
		self.hist = TH1F(name + "_" + path, "temp"+path, bins[0], bins[1], bins[2])
	    	for j in range(len(trees)):
			histbuild = singledist("newhist"+str(j), var, cut, trees[j], path, [1, 1, 1], bins)
			self.hist.Add(histbuild.GET())	
	def GetHist(self):
		return self.hist
