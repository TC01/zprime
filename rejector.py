#!/usr/bin/env python

import os
import ROOT
#from ROOT import *
import sys

import optparse

#from optparse import OptionParser
#parser = OptionParser()
#parser.add_option('--n', metavar='N', type='string', action='store',
 #                 dest='nm',
#                  help='')
#parser.add_option('--o', metavar='N', type='string', action='store',
#                  dest='out',
#                  help='')
#(options, args) = parser.parse_args()

#f = TFile(options.nm)
#t = f.Get('tree')

#newf = TFile("holding.root", "recreate" )
#newf.cd()

#T = t.CopyTree("(isHad<1.0&numjets>1&jet2pt>50&leppt>50&metpt>50)")
#T.SetName('TREE')

#newnewf = TFile(options.out+".root", "recreate")
#newnewf.cd()

#TT = T.CopyTree('')
#TT.SetName('tree')

#newnewf.Write()
#newnewf.Save()

def rejectLeptons(location, name):
	file = ROOT.TFile(location)
	tree = file.Get('tree')

	holding = ROOT.TFile("holding.root", "recreate")
	holding.cd()

	copy = tree.CopyTree("isHad>=1.0&&numjets>1")
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
					rejectLeptons(os.path.join(path, file), file)
					print "Applied rejection cuts to " + file

	os.remove(os.path.join(os.getcwd(), "holding.root"))

if __name__ == '__main__':
	main()
