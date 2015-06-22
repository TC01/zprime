#!/usr/bin/env python

# TODO: write cut thingy.
# that is, write a thing that can open a file and read from it
# i.e: ./analyzer.py -p output/ -o bprime/ -i bprime/cuts
# cuts file format:
#  name: {cut description language}
# which is a fancy word for "jet[X] like we process.
# -i can be overridden by -c options to select only specific ones.

# cuts file loaded into dictionary which is then passed to generate cuts.

# ALSO: write output thing to make our output files have the same names they did before.
# and to move them somewhere nicer.

import os
import glob
import math
import ROOT
import sys
from AnaStep import *
import optparse

lumi = 19800
path = os.path.join(os.getcwd(), "trees")

#defaultCuts = { "topmass": "jet[X]tau32>0&&jet[X]tau32<0.5&&jet[X]mass<270&&jet[X]mass>130",
#				"wmass": "(jet[X]tau32<0||jet[X]tau32>0.5)&&jet[X]mass<100&&jet[X]mass>70",
#				"btag": "(jet[X]tau32<0||jet[X]tau32>0.5)&&jet[X]csv>0.697"}

defaultCuts = { "topmass": "jet[X]tau32>0&&jet[X]tau32<0.50&&jet[X]mass<270&&jet[X]mass>130",
				"wmass": "(jet[X]tau21<0.75)&&jet[X]mass<100&&jet[X]mass>70",
				"btag": "(jet[X]csv>0.333)"}

def generateCuts(cutTemplates, numjets=3):
	cuts = {}
	for name, template in cutTemplates.iteritems():
		fullCut = ""
		if "jet[X]" in template:
			for i in range(numjets):
				jetCut = template.replace("[X]", str(i+1))
				fullCut += "(" + jetCut + ")"
				if i < numjets - 1:
					fullCut += "||"
		else:
			fullCut = template
		cuts[name] = fullCut
	return cuts

def main():
	global lumi, path
	global signal15file, signal20file, signal30file
	global ttbar_hadronic_file, qcd_file
	global defaultCuts

	parser = optparse.OptionParser()
	parser.add_option("-p", "--path", type="string", default=path, help="Path where trees can be found.")
	parser.add_option("-c", "--cut", action="append", dest="cuts", help="Name of a cut to use.")
	parser.add_option('-o', '--output', type='string', default=os.path.join(os.getcwd(), "output"), help="Dir to copy output plots to.")
	parser.add_option('-n', '--name', type='string', default="hadronic", help="Identifying part of output name.")
	options, args = parser.parse_args()

	if os.path.exists(os.path.abspath(options.path)):
		path = os.path.abspath(options.path)

	cuts = generateCuts(defaultCuts)

	signal15file = os.path.join(path, "Gstar_Hadronic_1500GeV.root")
	signal20file = os.path.join(path, "Gstar_Hadronic_2000GeV.root")
	signal30file = os.path.join(path, "Gstar_Hadronic_3000GeV.root")

	ttbar_hadronic_file = os.path.join(path, "TTJets_HadronicMGDecays_8TeV-madgraph.root")
	qcd_file = os.path.join(path, "QCD_TuneZ2star_8TeV-pythia6.root")
	wjet_hadronic_file = os.path.join(path, "WJetsFullyHadronic_Ht100_Pt50_Pt30_deta22_Mqq200_8TeV-madgraph.root")

	signal15 = dist(signal15file, "signal_1500", ROOT.TColor.kBlue, 0.37*0.68*0.2/160000, "no")
	signal20 = dist(signal20file, "signal_2000", ROOT.TColor.kBlue+3, 0.054*0.68*0.2/160000, "no")
	signal30 = dist(signal30file, "signal_3000", ROOT.TColor.kBlue+4, 0.0015*0.68*0.2/160000, "no")

	ttbar_hadronic = dist(ttbar_hadronic_file, "ttbar_hadronic", ROOT.TColor.kRed, 53.4/10537444, "no")
	qcd = dist(qcd_file, "qcd", ROOT.TColor.kYellow, 1, "yes")
	# Uh. xs?
	wjet_hadronic = dist(wjet_hadronic_file, "wjet_hadronic", ROOT.TColor.kGreen, 1/4951861, "no")

	step = pile("tree")
	step.addSig(signal15)
	step.addSig(signal20)
	step.addSig(signal30)
	step.addBkg(ttbar_hadronic)
	step.addBkg(qcd)
	step.addBkg(wjet_hadronic)

	if options.cuts is None:
		for name, realcut in cuts.iteritems():
			step.addCut(cut(realcut, name))
			print "Added cut " + name + ": " + cuts[name]
	else:
		for name in options.cuts:
			try:
				step.addCut(cut(cuts[name], name))
				print "Added cut " + name + ": " + cuts[name]
			except:
				print "Cut not understood: " + name			

	none = AnaStep(options.name, step, lumi, 'RECO123mass', [50, 0, 4000], "yes")

	os.remove(os.path.join(os.getcwd(), "DELETEMEIFYOUWANT.root"))
	raw_input()

if __name__ == '__main__':
	main()
