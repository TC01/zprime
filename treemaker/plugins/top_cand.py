# The top candidate plugin.
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
	variables['topcandpt'] = array.array('f', [-1.0])
	variables['topcandmass'] = array.array('f', [-1.0])
	variables['topcandeta'] = array.array('f', [100.0])
	variables['topcandphi'] = array.array('f', [100.0])
	variables['topcandtau21'] = array.array('f', [1.0])
	variables['topcandtau32'] = array.array('f', [1.0])
	return variables

def analyze(event, variables, labels, isData):
	
	# We only care if there is a valid "closest jet" to the event.
	# We also care if that jet meets our b-tagging criteria.
	closest = variables['closest'][0]
	if closest >= 0 and closest < maxJets:
		jetName = 'jet' + str(closest)
		if variables[jetName + 'mass'][0] < 50:
			# TODO: how are topcandtaus computed?
			variables['topcandtau21'][0] = variables[jetName + 'tau21'][0]
			variables['topcandtau32'][0] = variables[jetName + 'tau32'][0]
			
			# Create the 4-vectors, then add them.
			closestJet = ROOT.TLorentzVector()
			wCandidate = ROOT.TLorentzVector()
			wCandidate.SetPtEtaPhiM(variables['WcandPt_plus'][0], variables['WcandEta_plus'][0], variables['WcandPhi_plus'][0], variables['lepmass'][0])
			closestJet.SetPtEtaPhiM(variables[jetName + 'pt'][0], variables[jetName + 'phi'][0], variables[jetName + 'eta'][0], variables[jetName + 'mass'][0])
			
			topCandidate = wCandidate + closestJet
			variables['topcandpt'][0] = topCandidate.Pt()
		
	return variables

def reset(variables):
	variables['lep2Drel'][0] = -1.0
	variables['lep2Drel'][0] = -1.0
	variables['tri_jet'][0] = -1.0
	variables['tri_lep'][0] = -1.0
	variables['closest_jet'][0] = -1.0
	return variables

def createCuts(cutArray):
	return cutArray

def makeCuts(event, variables, cutArray, labels, isData):
	return cutArray
