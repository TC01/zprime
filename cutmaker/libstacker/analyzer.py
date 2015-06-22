#!/usr/bin/env python

import optparse
import os

import libstacker

location = "trees/"

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

def plotJetVar(name, jetvar, jetcut, exit, bins = 50, lower = 0, upper = 4000):
	global location, log

	jets = 3
	vars = []
	cuts = []
	for i in range(jets):
		jetnum = str(i + 1)
		currentJetCut = jetcut.replace("[X]", jetnum)
		currentJetCut = currentJetCut.replace("[Y]", getOtherNum(jetnum, jets))
		newvar = jetvar.replace("[X]", jetnum)
		newvar = newvar.replace("[Y]", getOtherNum(jetnum, jets))
		vars.append(newvar)
		cuts.append(currentJetCut)
	
	stack = libstacker.doPlotThings(name, cuts, vars, bins, lower, upper, location, log)
	if not exit:
		raw_input()

def plotGlobalVar(name, var, exit, bins = 50, lower = 0, upper = 4000):
	global location, log

	vars = [var]
	cuts = [""]
	stack = libstacker.doPlotThings(name, cuts, vars, bins, lower, upper, location, log)
	if not exit:
		raw_input()

def main():
	global location, log
	parser = optparse.OptionParser()

	parser.add_option("-j", "--jet", default="top", dest="jet", help="The jet to parse.")
	parser.add_option("-v", "--variable", default="m_all", dest="variable", help="The variable to plot.")
	parser.add_option("-e", "--exit", default=False, action="store_true", dest="exit", help="Exit immediately when done, don't raw_input.")
	parser.add_option("-d", "--location", default=location, dest="location", help="The location to run over.")
	parser.add_option("-l", "--log", default=False, action="store_true", dest="log", help="Plot in log scale.")

	options, args = parser.parse_args()

	location = options.location
	log = options.log

	# Select the right generic cut (selection criteria) to use 
	topmass = '(jet[X]mass > 130 && jet[X]mass < 270)'
	nottop_tag = '(jet[X]mass < 130 || jet[X]mass > 270)'
	jets = {'top':topmass, 'bigtop':nottop_tag}
	try:
		jetcut = jets[options.jet]
	except:
		print "Error: Unrecognized jet."
		return

	variables = ["jetmass", "m_all"]
	if options.variable == "m_all":
		plotGlobalVar("hadronic_unmergedmass", "UNMERGEDMASS", options.exit)

	if options.variable == "jetmass":
		plotJetVar("hadronic_" + options.jet + "_mass", "jet[X]mass", jetcut, options.exit, 50, 0, 500)
	if options.variable == "other_jetmass":
		plotJetVar("hadronic_" + options.jet + "_other_jets_mass", "HADTPRIME_jet[Y]_mass", jetcut, options.exit)

if __name__ == '__main__':
	main()
