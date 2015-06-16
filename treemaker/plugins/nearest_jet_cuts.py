# The Triangle and 2D Cuts, implemented using 'find closest jet' method.
# Despite the names, these don't seem to be cuts... yet. Perhaps we'll add some
# to the cut array later.

import array
import math

import ROOT

from Treemaker.Treemaker import cuts

maxJets = 3

# Code from Marc used in Ye Olde G* Analysis Treemaker
# (returns the index of the jet (from a collection "jets") closest to the given four-vector)
def ClosestJet(jets, fourvec):
	DR = 9999.
	index = -1
	for j in range(0,len(jets)):
		if jets[j].Pt() > 0 :
			dR = fourvec.DeltaR(jets[j])
			if dR < DR :
				DR = fourvec.DeltaR(jets[j])
				index = j
	return index

def setup(variables, isData):
	variables['lep2Drel'] = array.array('f', [100.0])
	variables['lep2Ddr'] = array.array('f', [-1.0])
	variables['tri_lep'] = array.array('f', [100.0])
	variables['tri_jet'] = array.array('f', [-1.0])
	variables['closest_jet'] = array.array('f', [-1.0])
	return variables

def analyze(event, variables, labels, isData):
	# We need to create a list of all the jets.
	# Hm.
	
	# This seems to be a design flaw; analyze() should be able to access the
	# state of cuts. Since it can't, we have to do this. TODO: fix.
	electrons = labels['jhuElePFlow']['electron'].product()
	muons = labels['jhuMuonPFlow']['muon'].product()
	isHadronic = False
	if len(electrons) == 0 and len(muons) == 0:
		isHadronic = True
	
	# Now, create a list of all the jets that exist. Simplest way to do that:
	jets = []
	if not isHadronic:
		for i in xrange(min(maxJets, int(variables['numjets'][0]))):
			jetNum = str(i + 1)
			newJet = ROOT.TLorentzVector()
			jetPt = variables['jet' + jetNum + 'pt'][0]
			jetEta = variables['jet' + jetNum + 'eta'][0]
			jetPhi = variables['jet' + jetNum + 'phi'][0]
			jetMass = variables['jet' + jetNum + 'mass'][0]
			newJet.SetPtEtaPhiM(jetPt, jetEta, jetPhi, jetMass)
			jets.append(newJet)
	
		# Now compute the relevant quantities that will get cut on later.
		lepVector = ROOT.TLorentzVector()
		lepVector.SetPtEtaPhiM(variables['leppt'][0], variables['lepeta'][0], variables['lepphi'][0], variables['lepmass'][0])
		closest = ClosestJet(jets, lepVector)
		if closest < maxJets and closest >= 0:
			variables['lep2Drel'][0] = lepVector.Perp(jets[closest].Vect())
			variables['lep2Ddr'][0] = lepVector.DeltaR(jets[closest])
			variables['tri_lep'][0] = abs(variables['lepphi'][0] - variables['metphi'][0])
			variables['tri_jet'][0] = abs(jets[closest].Phi() - variables['metphi'][0])
			variables['closest_jet'][0] = closest
		
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
