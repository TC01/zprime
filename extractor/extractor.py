#!/usr/bin/env python

import os
import sys

import ROOT

variable = "RECO23mass"

def extractDirectory(directory, var):

	outputFilename = variable + ".root"
	outputFile = ROOT.TFile(os.path.join(directory, outputFilename), "RECREATE")

	for path, dirs, files in os.walk(directory):
		for rootFile in files:
			if ".root" not in rootFile:
				continue
			tfile = ROOT.TFile(os.path.join(directory, rootFile))
			tree = tfile.Get("tree")
			argset = ROOT.RooArgSet(variable)
			cut = ROOT.RooFormulaVar("all", "all", "1", ROOT.RooArgList())
			dataset = ROOT.RooDataSet(rootFile, rootFile, tree, argset, cut)

			# Hardcode nbins to 50 for now?
			outputFile.cd()
			arglist = ROOT.RooArgList(variable)
			histogram = dataset.createHistogram(arglist, 50)
			histogram.Save()

			tfile.Close()


def main():
	# I'll write an optparse line later, for -v.
	if len(sys.argv) != 2:
		print "Error: please provide a directory."
		sys.exit(1)
	pathName = sys.argv[1]
#	try:
	pathName = os.path.abspath(pathName)
	directory = os.path.join(pathName, "output")
	extractDirectory(directory, variable)
#	except:
#		print "Error: unknown source directory, or directory lacks a output/ folder."
#		sys.exit(1)

if __name__ == '__main__':
	main()
