# QCD Stacker Class:
# INCLUDES:
import os
import ROOT
from ROOT import *
import sys
from anadist import *

# CLASS:
class QCD_stack:
	def __init__(self, path, var, trees, bins, cut):
		files = []
		for i in range(1,8):
			files.append(path+"QCD"+str(i)+".root")

		xs = [34138.15, 1759.549, 113.8791, 26.9921, 3.550036, 0.737844, 0.03352235, 0.001829005]
		n = [6000000, 6000000, 4000000, 4000000, 4000000, 2000000, 2000000, 1000000]
		self.stack = TH1F("qcd_"+var, "qcd"+var, bins[0], bins[1], bins[2])
		for i in range(len(files)):
		    for j in range(len(trees)):
			stackbuild = singledist("newhist"+str(j)+str(i), var, cut, trees[j], files[i], [xs[i], 1, n[i]], bins)
			self.stack.Add(stackbuild.GET())	
	def GetStack(self):
		return self.stack
