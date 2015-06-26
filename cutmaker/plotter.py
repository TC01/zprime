#!/usr/bin/env python

# A marclib-powered plotter.

import glob
import math
import optparse
import os
import shutil
import sys

import ROOT
from marclib import *
from marclib.AnaStep import *

from formatter import *
from formatter import formatlib

lumi = 19800

def doAnalysis(jobname, path, treepath, varname, nowait, title, signalScale=1):
	global lumi
	global signal15file, signal20file, signal30file
	global ttbar_hadronic_file, qcd_file

	signal15file = os.path.join(treepath, "Gstar_Semilep_1500GeV.root")
	signal20file = os.path.join(treepath, "Gstar_Semilep_2000GeV.root")
	signal30file = os.path.join(treepath, "Gstar_Semilep_3000GeV.root")

	# Legacy!
	ttbar_hadronic_file = os.path.join(treepath, "TTJets_HadronicMGDecays_8TeV-madgraph.root")
	qcd_file = os.path.join(treepath, "QCD_TuneZ2star_8TeV-pythia6.root")
	singletop_file = os.path.join(treepath, "Singletop.root")
	wjet_hadronic_file = os.path.join(treepath, "WJetsFullyHadronic_Ht100_Pt50_Pt30_deta22_Mqq200_8TeV-madgraph.root")

	ttbar_semilep_file = os.path.join(treepath, "TTJets_SemiLeptMGDecays_8TeV-madgraph.root")
	ttbar_leptonic_file = os.path.join(treepath, "TTJets_FullLeptMGDecays_8TeV-madgraph.root")
	wjets_semilep_file = os.path.join(treepath, "WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball.root")

	# Things that are potentially rubbish, partial list: these scale factors.
	signal15 = dist(signal15file, "signal_1500", ROOT.TColor.kBlue, signalScale * 0.37*0.68*2*0.2/160000, "no")
	signal20 = dist(signal20file, "signal_2000", ROOT.TColor.kBlue+2, signalScale * 0.054*0.68*2*0.2/160000, "no")
	signal30 = dist(signal30file, "signal_3000", ROOT.TColor.kBlue+4, signalScale * 0.0015*0.68*2*0.2/160000, "no")

	ttbar_semilep = dist(ttbar_semilep_file, "ttbar_semilep", ROOT.TColor.kRed, 107.7/25424818, "no")
	ttbar_leptonic = dist(ttbar_leptonic_file, "ttbar_dileptonic", ROOT.TColor.kRed + 2, 25.17/12119013, "no")
	
	# Singletop and QCD distributions.
	singletop = dist(singletop_file, "singletop", ROOT.TColor.kSpring, 1, "yes")
	qcd = dist(qcd_file, "qcd", ROOT.TColor.kYellow, 1, "yes")
	
	wjet_semilep = dist(wjets_semilep_file, "wjets_semilep", ROOT.TColor.kGreen, 33836.9/57709905, "no")

	step = pile("tree")
	step.addSig(signal15)
	step.addSig(signal20)
	step.addSig(signal30)
	step.addBkg(ttbar_semilep)
	step.addBkg(ttbar_leptonic)
	step.addBkg(singletop)
	step.addBkg(qcd)
	step.addBkg(wjet_semilep)

	step.addCut(cut('1', 'identity'))

	jobname = jobname + '_' + varname
	if signalScale != 1:
		jobname += "_" + str(signalScale)
	none = AnaStep(jobname, step, lumi, varname, [50, 0, 4000], "no", title)

	# Process output files.
	os.remove(os.path.join(os.getcwd(), "DELETEMEIFYOUWANT.root"))
	for location, dir, files in os.walk(os.getcwd()):
		if location == os.getcwd():
			for file in files:
				if ".root" in file:
					os.remove(os.path.join(location, file))
				if ".png" in file or ".pdf" in file:
					try:
						os.remove(os.path.join(path, "plots", file))
					except:
						pass
					shutil.move(file, os.path.join(path, "plots"))
				if "output.log" in file:
					os.remove(os.path.join(location, file))
#	formatlib.doFormatting(jobname, path)

	if not nowait:
		raw_input()

def main():
	# Hierarchy: output/, plots/, cuts.conf in path/

	parser = optparse.OptionParser()
	parser.add_option("-p", "--path", type="string", default='', help="Path where source can be found and output will be written.")
	parser.add_option("-c", "--cut", action="append", dest="cuts", help="Name of a cut to use that is stored in cuts.conf.")
	parser.add_option('-n', '--name', type='string', default="", help="Identifying part of output name.")
	parser.add_option('-v', '--variable', type='string', dest="varname", default="EventMass", help="The variable to plot, defaults to total mass.")

	# These options are ignored if not specified, and path/source/ and path/cuts.conf are used instead.
	parser.add_option('-t', '--trees', type='string', default=None, dest='trees', help="Location of trees, separate from working path.")
	parser.add_option('-f', '--cut-file', type='string', default=None, dest='cutfile', help="Location of cuts config file, separate from working path.")

	parser.add_option('-s', '--scale-signal', dest='scaleSignal', default=1, type=int, help="Scale factor on the signals. Defaults to 1 (no extra scaling).")
	parser.add_option('-l', '--title', dest='title', default=None, help="The title of the plot.")

	parser.add_option('--no-cwd', action='store_true', dest='nocwd', default=False, help="Make paths absolute instead of relative to cwd.")
	parser.add_option('--no-wait', action='store_true', dest='nowait', default=False, help="Do not wait to allow the user to look at plots.")
	
	options, args = parser.parse_args()

	if options.nocwd:
		path = os.path.abspath(options.path)
	else:
		path = os.path.abspath(os.path.join(os.getcwd(), options.path))

	# This needs to happen up here.
	if not os.path.exists(path):
		os.mkdir(path)

	# Extract location of trees from command line options.
	treepath = ""
	if not options.trees is None:
		if os.path.exists(os.path.abspath(options.trees)):
			treepath = os.path.abspath(options.trees)
	if treepath == "":
		if not os.path.exists(os.path.join(path, "output")):
			print "Error: unable to find source trees."
			sys.exit(1)
		treepath = os.path.join(path, "output")

	print "\n"
	name = options.name
	if name == "":
		working = path.rstrip('/')
		name = os.path.basename(working)
	try:
		os.remove(os.path.join(os.getcwd(), 'output.log'))
	except:
		pass
	
	title = options.title
	if title is None:
		title = name
	if options.scaleSignal != 1:
		title += " (Signal " + str(options.scaleSignal) + "x)"
	
	doAnalysis(name, path, treepath, options.varname, options.nowait, title, options.scaleSignal)

if __name__ == '__main__':
	main()
