#!/usr/bin/env python

import os
import glob
import math
import ROOT
import sys
from AnaStep import *
import optparse

lumi = 19800
path = os.path.join(os.getcwd(), "trees")

signal15file = os.path.join(path, "Gstar_Hadronic_1500GeV.root")
signal20file = os.path.join(path, "Gstar_Hadronic_2000GeV.root")
signal30file = os.path.join(path, "Gstar_Hadronic_3000GeV.root")

ttbar_hadronic_file = os.path.join(path, "TTJets_HadronicMGDecays_8TeV-madgraph.root")
qcd_file = os.path.join(path, "QCD_TuneZ2star_8TeV-pythia6.root")

def main():
	global lumi, path
	global signal15file, signal20file, signal30file
	global ttbar_hadronic_file, qcd_file

	parser = optparse.OptionParser()
	parser.add_option("-c", "--cut", action="append", dest="cuts", help="Name of a cut to use.")
	options, args = parser.parse_args()


	signal15 = dist(signal15file, "signal_1500", ROOT.TColor.kBlue, 0.37*0.68*0.2/160000, "no")
	signal20 = dist(signal20file, "signal_2000", ROOT.TColor.kBlue+3, 0.37*0.68*0.2/160000, "no")
	signal30 = dist(signal30file, "signal_3000", ROOT.TColor.kBlue+4, 0.37*0.68*0.2/160000, "no")

	ttbar_hadronic = dist(ttbar_hadronic_file, "ttbar_hadronic", ROOT.TColor.kRed, 53.4/10537444, "no")
	qcd = dist(qcd_file, "qcd", ROOT.TColor.kYellow, 1, "yes")

	step = pile("tree")
	step.addSig(signal15)
	step.addSig(signal20)
	step.addSig(signal30)
	step.addBkg(ttbar_hadronic)
	step.addBkg(qcd)

	cuts = []
	cuts.append(cut('(jet1mass<270&&jet1mass>130)||(jet2mass<270&&jet2mass>130)||(jet3mass<270&&jet3mass>130)', 'topmass'))
	cuts.append(cut('(jet1mass<100&&jet1mass>70)||(jet2mass<100&&jet2mass>70)||(jet3mass<100&&jet3mass>70)', 'wmass'))
	cuts.append(cut('jet1csv<0.55||jet2csv<0.55||jet3csv<0.55', 'toptag'))
	cuts.append(cut('jet1csv<0.5||jet2csv<0.5||jet3csv<0.5', 'wtag_tight'))
	cuts.append(cut('jet1csv<0.75||jet2csv<0.75||jet3csv<0.75', 'wtag_loose'))
	cuts.append(cut('jet1csv>0.697||jet2csv>0.697||jet3csv>0.697', 'btag'))
	cuts.append(cut('jet1tau21<0.5||jet2tau21<0.5||jet3tau21<0.5', 'tau'))
	cuts.append(cut('jet3pt>50', 'pt_test'))
	cuts.append(cut('(jet1tau32>0&&jet1tau32<0.5)||(jet2tau32>0&&jet2tau32<0.5)||(jet3tau32>0&&jet3tau32<0.5)', 'tau32'))
	for realcut in cuts:
		if options.cuts is None or realcut.getName() in options.cuts:
			step.addCut(realcut)

	none = AnaStep('hadronic', step, lumi, 'RECO123mass', [50, 0, 4000], "no")

	os.remove(os.path.join(os.getcwd(), "DELETEMEIFYOUWANT.root"))
	raw_input()

if __name__ == '__main__':
	main()
