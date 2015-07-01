# The heavy top (T) candidate plugin.
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

def setup(variables, isData):
	variables['hadtopcandpt'] = array.array('f', [-1.0])
	variables['hadtopcandmass'] = array.array('f', [-1.0])
	variables['hadtopcandeta'] = array.array('f', [100.0])
	variables['hadtopcandphi'] = array.array('f', [100.0])
	return variables

def analyze(event, variables, labels, isData):
	
	# We only care if there is a valid "closest jet" to the event.
	# If there isn't, we can't distinguish which jets to make into a T candidate.
	closest = variables['closest_jet'][0]
	if closest >= 0 and closest < maxJets:
		jetNumbers = [1, 2, 3]
		jetNumbers.remove(int(closest) + 1)
		firstJet = 'jet' + str(jetNumbers[0])
		secondJet = 'jet' + str(jetNumbers[1])
		
		# Require that one of the remaining jets be a b and the other be a W.
		valid = False
		firstJetMass = variables[firstJet + 'mass'][0]
		secondJetMass = variables[secondJet + 'mass'][0]
		if firstJetMass < bMassMax and secondJetMass < wMassMax and secondJetMass > wMassMin:
			valid = True
		if secondJetMass < bMassMax and firstJetMass < wMassMax and firstJetMass > wMassMin:
			valid = True

		# Also require that there *are* at least three jets.
		if int(variables['numjets'][0]) < 3:
			valid = False
		
		if valid:
			wJet = ROOT.TLorentzVector()
			bJet = ROOT.TLorentzVector()
			wJet.SetPtEtaPhiM(variables[firstJet + 'pt'][0], variables[firstJet + 'eta'][0], variables[firstJet + 'phi'][0], variables[firstJet + 'mass'][0])
			bJet.SetPtEtaPhiM(variables[secondJet + 'pt'][0], variables[secondJet + 'eta'][0], variables[secondJet + 'phi'][0], variables[secondJet + 'mass'][0])
			
			TopCandidate = wJet + bJet
			variables['hadtopcandpt'][0] = TopCandidate.Pt()
			variables['hadtopcandeta'][0] = TopCandidate.Eta()
			variables['hadtopcandphi'][0] = TopCandidate.Phi()
			variables['hadtopcandmass'][0] = TopCandidate.M()
		
	return variables

def reset(variables):
	variables['hadtopcandpt'][0] = -1.0
	variables['hadtopcandeta'][0] = 100.0
	variables['hadtopcandphi'][0] = 100.0
	variables['hadtopcandmass'][0] = -1.0
	return variables

def createCuts(cutArray):
	return cutArray

def makeCuts(event, variables, cutArray, labels, isData):
	return cutArray
