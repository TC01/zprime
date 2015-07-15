# The hadronic W candidate plugin.
# Depends on lep_nu_wcand and on nearest_jet_cuts (to determine closest jet).

import array
import math

import ROOT

from Treemaker.Treemaker import cuts

# TODO: add "params" to config file that get loaded into variables.
# e.g. maxJets gets set across all plugins this way.
maxJets = 3

bMassMax = 50
wMassMin = 50
wMassMax = 120
wPtMin = 200

def setup(variables, isData):
	variables['hadWcandpt'] = array.array('f', [-1.0])
	variables['hadWcandmass'] = array.array('f', [-1.0])
	variables['hadWcandeta'] = array.array('f', [100.0])
	variables['hadWcandphi'] = array.array('f', [100.0])

	variables['hadWcandtau21'] = array.array('f', [1.0])
	variables['hadWcandtau32'] = array.array('f', [1.0])

	variables['possible_had_W'] = array.array('f', [0.0])

	return variables

def analyze(event, variables, labels, isData):

	# The goal of this one is merely to tag a jet as being the W candidate.
	# Ideally, that's the jet farthest from the lepton.

	jetNumbers = [i + 1 for i in xrange(maxJets)]

	closest = variables['closest_jet'][0]
	if closest >= 0 and closest < maxJets:
		jetNumbers.remove(int(closest) + 1)

	# Verify that the jets exist.
	candidates = []
	for jetNum in jetNumbers:
		jet = 'jet' + str(jetNum)
		candidates.append(jet)
		try:
			jetMass = variables[jet + 'mass'][0]
			jetPt = variables[jet + 'pt'][0]
		except KeyError:
			candidates.remove(jet)
			break
		if not (jetMass < wMassMax and jetMass > wMassMin and jetPt > wPtMin):
			candidates.remove(jet)

	# Select the first jet to meet these criteria. Discard the rest.
	# (this should be the highest energy jet. Not sure if that's what we want).
	# (But it's better than selecting one at random?)
	variables['possible_had_W'][0] = len(candidates)
	for candidate in candidates:
		variables['hadWcandpt'][0] = variables[jet + 'pt'][0]
		variables['hadWcandeta'][0] = variables[jet + 'eta'][0]
		variables['hadWcandphi'][0] = variables[jet + 'phi'][0]
		variables['hadWcandmass'][0] = variables[jet + 'mass'][0]
		variables['hadWcandtau32'][0] = variables[jet + 'tau32'][0]
		variables['hadWcandtau21'][0] = variables[jet + 'tau21'][0]
		break
		
	return variables

def reset(variables):
	variables['hadWcandpt'][0] = -1.0
	variables['hadWcandeta'][0] = 100.0
	variables['hadWcandphi'][0] = 100.0
	variables['hadWcandmass'][0] = -1.0
	variables['hadWcandtau21'][0] = 1.0
	variables['hadWcandtau32'][0] = 1.0
	return variables

def createCuts(cutArray):
	return cutArray

def makeCuts(event, variables, cutArray, labels, isData):
	return cutArray
