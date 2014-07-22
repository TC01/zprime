#!/usr/bin/env python

import os
import ROOT
#from ROOT import *
import sys

import optparse

rejection = "jet3pt>50&&numjets>2"

def rejectEvents(location, name):
	global rejection
	file = ROOT.TFile(location)
	tree = file.Get('tree')

	holding = ROOT.TFile("holding.root", "recreate")
	holding.cd()

	copy = tree.CopyTree(rejection)
	copy.SetName('TREE')

	newfile = ROOT.TFile(os.path.join(os.getcwd(), name), "RECREATE")
	newfile.cd()

	newTree = copy.CopyTree('')
	newTree.SetName('tree')

	newfile.Write()
	newfile.Save()

	newfile.Close()
	holding.Close()
	file.Close()

def main():
	parser = optparse.OptionParser()
	parser.add_option('-d', '--directory', type='string', default=os.getcwd(), help="Directory to process.")
	options, args = parser.parse_args()

	location = os.path.abspath(options.directory)
	for path, dir, files in os.walk(location):
		if path == location:
			for file in files:
				if ".root" in file:
					rejectEvents(os.path.join(path, file), file)
					print "Applied rejection cuts to " + file

	os.remove(os.path.join(os.getcwd(), "holding.root"))

if __name__ == '__main__':
	main()
