#!/usr/bin/env python

# We need to capture stdout.

import collections
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

lumi = 19748

#defaultCuts = { "topmass": "jet[X]tau32>0&&jet[X]tau32<0.5&&jet[X]mass<270&&jet[X]mass>130",
#				"wmass": "(jet[X]tau32<0||jet[X]tau32>0.5)&&jet[X]mass<100&&jet[X]mass>70",
#				"btag": "(jet[X]tau32<0||jet[X]tau32>0.5)&&jet[X]csv>0.697"}

defaultCuts = { "topmass": "jet[X]tau32>0&&jet[X]tau32<0.50&&jet[X]mass<270&&jet[X]mass>130",
				"wmass": "(jet[X]tau21<0.75)&&jet[X]mass<100&&jet[X]mass>70",
				"btag": "(jet[X]csv>0.333)"}

def getOtherNum(jetnum, max):
    # This is a really bad function but it works, so I'll fix it later.
    string = ""
    for i in range(max):
        if i + 1 == int(jetnum):
            continue
        string += str(i + 1)
    if "13" == string:
        string = "31"
    return string


def createCutTemplates(filename=None):
	global defaultCuts
	if filename is None:
		return defaultCuts
	
	title = None
	cutDict = collections.OrderedDict()
	with open(filename) as cutfile:
		for line in cutfile:
			if '#' == line[0]:
				if '#title' == line[:len('#title')]:
					title = line[len('#title '):]
				continue
			if line.lstrip().rstrip() == "":
				continue
			cutname, sep, cut = line.partition(': ')
			cut = cut.rstrip('\n')
			cutDict[cutname] = cut
	return cutDict, title

def generateCuts(cutTemplates, numjets=3):
	cuts = collections.OrderedDict()
	for name, template in cutTemplates.iteritems():
		fullCut = ""
		invert = False
		if "INV " == template[:4]:
			invert = True
			template = template[4:]
		if "[X]" in template or "[Y]" in template:
			for i in range(numjets):
				next = i + 2
				if next > numjets:
					next = 1
				jetCut = template.replace("[X]", str(i+1))
				jetCut = jetCut.replace("[Y]", str(next))
				fullCut += "(" + jetCut + ")"
				if i < numjets - 1:
					fullCut += "||"
		else:
			fullCut = template
		if invert:
			fullCut = "!(" + fullCut + ")"
		cuts[name] = fullCut
	return cuts

def fixOutputFiles(location):
	for path, dir, files in os.walk(location):
		for file in files:
			if "signal_1500" in file:
				shutil.move(os.path.join(location, file), os.path.join(location, "Gstar_Semilep_1500GeV.root"))
			if "signal_2000" in file:
				shutil.move(os.path.join(location, file), os.path.join(location, "Gstar_Semilep_2000GeV.root"))
			if "signal_3000" in file:
				shutil.move(os.path.join(location, file), os.path.join(location, "Gstar_Semilep_3000GeV.root"))
			if "wjets_semilep" in file:
				shutil.move(os.path.join(location, file), os.path.join(location, "WJetsToLNu_TuneZ2Star_8TeV-madgraph.root"))
			if "wjet_hadronic" in file:
				shutil.move(os.path.join(location, file), os.path.join(location, "WJetsFullyHadronic_Ht100_Pt50_Pt30_deta22_Mqq200_8TeV-madgraph.root"))
			if "ttbar_hadronic" in file:
				shutil.move(os.path.join(location, file), os.path.join(location, "TTJets_HadronicMGDecays_8TeV-madgraph.root"))
			if "ttbar_semilep" in file:
				shutil.move(os.path.join(location, file), os.path.join(location, "TTJets_SemiLeptMGDecays_8TeV-madgraph.root"))
			if "ttbar_dileptonic" in file:
				shutil.move(os.path.join(location, file), os.path.join(location, "TTJets_FullLeptMGDecays_8TeV-madgraph.root"))
			if "qcd" in file:
				shutil.move(os.path.join(location, file), os.path.join(location, "QCD_TuneZ2star_8TeV-pythia6.root"))
			if "singletop" in file:
				shutil.move(os.path.join(location, file), os.path.join(location, "Singletop.root"))

def doAnalysis(jobname, path, treepath, cutfile, varname, nowait, cutArray=None):
	global lumi
	global signal15file, signal20file, signal30file
	global ttbar_hadronic_file, qcd_file

	cuts, title = createCutTemplates(cutfile)
	if title is None:
		jobname = title
	cuts = generateCuts(cuts)

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
	wjets_semilep_file = os.path.join(treepath, "WJetsToLNu_TuneZ2Star_8TeV-madgraph.root")

	# Things that are potentially rubbish, partial list: these scale factors.
	signal15 = dist(signal15file, "signal_1500", ROOT.TColor.kBlue, 0.37*0.68*2*0.2/160000, "no")
	signal20 = dist(signal20file, "signal_2000", ROOT.TColor.kBlue+2, 0.054*0.68*2*0.2/160000, "no")
	signal30 = dist(signal30file, "signal_3000", ROOT.TColor.kBlue+4, 0.0015*0.68*2*0.2/160000, "no")

	ttbar_semilep = dist(ttbar_semilep_file, "ttbar_semilep", ROOT.TColor.kRed, 107.7/25424818, "no")
	ttbar_leptonic = dist(ttbar_leptonic_file, "ttbar_dileptonic", ROOT.TColor.kRed + 2, 25.17/12119013, "no")

	# Singletop and QCD distributions.
	singletop = dist(singletop_file, "singletop", ROOT.TColor.kViolet, 1, "yes")
	qcd = dist(qcd_file, "qcd", ROOT.TColor.kYellow, 1, "yes")

	wjet_semilep = dist(wjets_semilep_file, "wjets_semilep", ROOT.TColor.kGreen, 1, "yes")

	step = pile("tree")
	step.addSig(signal15)
	step.addSig(signal20)
	step.addSig(signal30)
	step.addBkg(ttbar_semilep)
	step.addBkg(ttbar_leptonic)
	step.addBkg(singletop)
	step.addBkg(qcd)
	step.addBkg(wjet_semilep)

	if cutArray is None:
		for name, realcut in cuts.iteritems():
			step.addCut(cut(realcut, name))
			message = name + ': ' + cuts[name]
			with open('cuts.order', 'ab') as orderingFile:
				orderingFile.write(message)
			print "Added cut " + message
	else:
		for name in cutArray:
			try:
				step.addCut(cut(cuts[name], name))
				print "Added cut " + name + ": " + cuts[name]
			except:
				print "Cut not understood: " + name

	none = AnaStep(jobname, step, lumi, varname, [50, 0, 4000], "yes", title)

	# Process output files.
	os.remove(os.path.join(os.getcwd(), "DELETEMEIFYOUWANT.root"))
	for location, dir, files in os.walk(os.getcwd()):
		if location == os.getcwd():
			for file in files:
				if ".root" in file:
					shutil.move(file, os.path.join(path, "output"))
				if ".png" in file or ".pdf" in file:
					shutil.move(file, os.path.join(path, "plots"))
				if "output.log" in file:
					try:
						os.remove(os.path.join(path, "output.log"))
					except:
						pass
					shutil.move(file, path)
				if "cuts.order" in file:
					try:
						os.remove(os.path.join(path, "cuts.order"))
					except:
						pass
					shutil.move(file, path)
	fixOutputFiles(os.path.join(path, "output"))
	formatlib.doFormatting(jobname, path)

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
		if not os.path.exists(os.path.join(path, "..", "output")):
			print "Error: unable to find source trees."
			sys.exit(1)
		treepath = os.path.join(path, "..", "output")

	# Extract location of cutfile from command line options.
	cutfile = ""
	if not options.cutfile is None:
		if os.path.exists(os.path.abspath(options.cutfile)):
			cutfile = os.path.abspath(options.cutfile)
		shutil.copy(cutfile, os.path.join(path, "cuts.conf"))
	if cutfile == "":
		if not os.path.exists(os.path.join(path, "cuts.conf")):
			print "Error: unable to find cut config file."
			sys.exit(1)
		cutfile = os.path.join(path, "cuts.conf")

	if os.path.exists(os.path.join(path, "output")):
		print "WARNING: Deleting contents of " + path + "/output/"
		shutil.rmtree(os.path.join(path, "output"))
	os.mkdir(os.path.join(path, "output"))

	if os.path.exists(os.path.join(path, "plots")):
		print "WARNING: Deleting contents of " + path + "/plots/"
		shutil.rmtree(os.path.join(path, "plots"))
	os.mkdir(os.path.join(path, "plots"))

	print "\n"
	name = options.name
	if name == "":
		working = path.rstrip('/')
		name = os.path.basename(working)
	try:
		os.remove(os.path.join(os.getcwd(), 'output.log'))
	except:
		pass
	doAnalysis(name, path, treepath, cutfile, options.varname, options.nowait)

if __name__ == '__main__':
	main()
