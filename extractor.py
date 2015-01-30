#!/usr/bin/env python

import os
import sys

import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

import optparse

from libstacker import libstacker

variable = "RECO23mass"

def extractDirectory(directory, var):
	current = os.getcwd()
	os.chdir(directory)
	outputFilename = variable + ".root"
	outputFile = ROOT.TFile(os.path.join(directory, outputFilename), "RECREATE")

	for path, dirs, files in os.walk(directory):
		for rootFile in files:
			if ".root" not in rootFile:
				continue
			if rootFile == outputFilename:
				continue

			# Hardcoding bins because I'm lazy.
			bins = [50, 0, 4000]
			
			hist = libstacker.makeSingleHistogram(rootFile, [variable], ["tree"], bins, [""])
			hist.SetName(rootFile.partition(".")[0])

			#tfile = ROOT.TFile(os.path.join(directory, rootFile))
			#tree = tfile.Get("tree")
			#argset = ROOT.RooArgSet(variable)
			#cut = ROOT.RooFormulaVar("all", "all", "1", ROOT.RooArgList())
			#dataset = ROOT.RooDataSet(rootFile, rootFile, tree, argset, cut)

			outputFile.cd()
			hist.Write()

#			tfile.Close()

	os.chdir(current)

def main():
	# I'll write an optparse line later, for -v.

	parser = optparse.OptionParser()
	parser.add_option("-p", "--path", type="string", dest="path", default=os.getcwd(), help="Path where source can be found and output will be written.")
	parser.add_option('-v', '--variable', type='string', dest="varname", default="RECO123mass", help="The variable to plot, defaults to total mass.")

	(opts, args) = parser.parse_args()
	variable = opts.varname
	pathName = opts.path

	try:
		pathName = os.path.abspath(pathName)
		directory = os.path.join(pathName, "output")
		extractDirectory(directory, variable)
	except:
		print "Error: unknown source directory, or directory lacks a output/ folder."
		sys.exit(1)

if __name__ == '__main__':
	main()
