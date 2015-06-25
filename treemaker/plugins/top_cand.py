# The top candidate plugin. (Actually, leptonic top candidate).
# Depends on lep_nu_wcand and on nearest_jet_cuts (to determine closest jet).

import array
import math

import ROOT

from Treemaker.Treemaker import cuts

# TODO: add "params" to config file that get loaded into variables.
# e.g. maxJets gets set across all plugins this way.
maxJets = 3

bMassMax = 50

def setup(variables, isData):
	variables['leptopcandpt'] = array.array('f', [-1.0])
	variables['leptopcandmass'] = array.array('f', [-1.0])
	variables['leptopcandeta'] = array.array('f', [100.0])
	variables['leptopcandphi'] = array.array('f', [100.0])
	variables['leptopcandtau21'] = array.array('f', [1.0])
	variables['leptopcandtau32'] = array.array('f', [1.0])
	return variables

def analyze(event, variables, labels, isData):
	
	# We only care if there is a valid "closest jet" to the event.
	# We also care if that jet meets our b-tagging criteria.
	closest = variables['closest_jet'][0]
	if closest >= 0 and closest < maxJets:
		jetName = 'jet' + str(int(closest) + 1)
		if variables[jetName + 'mass'][0] < 50:
			# TODO: how are topcandtaus computed?
			variables['leptopcandtau21'][0] = variables[jetName + 'tau21'][0]
			variables['leptopcandtau32'][0] = variables[jetName + 'tau32'][0]
			
			# Create the 4-vectors, then add them.
			closestJet = ROOT.TLorentzVector()
			wCandidate = ROOT.TLorentzVector()
			wCandidate.SetPtEtaPhiM(variables['WcandPt_plus'][0], variables['WcandEta_plus'][0], variables['WcandPhi_plus'][0], variables['lepmass'][0])
			closestJet.SetPtEtaPhiM(variables[jetName + 'pt'][0], variables[jetName + 'eta'][0], variables[jetName + 'phi'][0], variables[jetName + 'mass'][0])
			
			topCandidate = wCandidate + closestJet
			variables['leptopcandpt'][0] = topCandidate.Pt()
			variables['leptopcandeta'][0] = topCandidate.Eta()
			variables['leptopcandphi'][0] = topCandidate.Phi()
			variables['leptopcandmass'][0] = topCandidate.M()
		
	return variables

def reset(variables):
	variables['leptopcandpt'][0] = -1.0
	variables['leptopcandeta'][0] = 100.0
	variables['leptopcandphi'][0] = 100.0
	variables['leptopcandmass'][0] = -1.0
	variables['leptopcandtau21'][0] = 1.0
	variables['leptopcandtau32'][0] = 1.0
	return variables

def createCuts(cutArray):
	return cutArray

def makeCuts(event, variables, cutArray, labels, isData):
	return cutArray
