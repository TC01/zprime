# A plugin that turns a nu + lepton (lep* + met*) into a W candidate
# Depends on lep_vars, met_vars.

import array
import math

import ROOT

from Treemaker.Treemaker import cuts

modifiers = ["plus", "minus"]
maxJets = 3

# Code from Marc used in Ye Olde G* Analysis Treemaker
def make_lepW(met, lep):
	newmet = ROOT.TLorentzVector()
	newmet_m = ROOT.TLorentzVector()
	newmet_p = ROOT.TLorentzVector()
	newmet.SetPtEtaPhiM(met.Pt(),0,met.Phi(),0)
	newmet_m.SetPtEtaPhiM(met.Pt(),0,met.Phi(),0)
	newmet_p.SetPtEtaPhiM(met.Pt(),0,met.Phi(),0)
	phivec = [math.cos(met.Phi()), math.sin(met.Phi())]
	P_lep = math.sqrt((lep.Px()*lep.Px())+(lep.Py()*lep.Py())+(lep.Pz()*lep.Pz()))
	P_phi = (lep.Px()*phivec[0])+(lep.Py()*phivec[1])
	b = (80.4*80.4) + (P_lep*P_lep) - (lep.E()*lep.E()) + (2*met.Pt()*P_phi)
	arg = (lep.E()*lep.E()) * ((4*met.Pt()*met.Pt()*((lep.Pz()*lep.Pz())-(lep.E()*lep.E())))+(b*b))
	if arg <= 0:
		Pz_met = lep.Pz()*b/(2*((lep.E()*lep.E()) -(lep.Pz()*lep.Pz())))
		newmet.SetPz(Pz_met)
		newmet.SetE(math.sqrt(newmet.Px()*newmet.Px()+newmet.Py()*newmet.Py()+newmet.Pz()*newmet.Pz()))
		return [newmet, newmet]
	else:
		Pz_met_p = ((lep.Pz()*b)+math.sqrt(arg))/(2*((lep.E()*lep.E()) -(lep.Pz()*lep.Pz())))
		Pz_met_m = ((lep.Pz()*b)-math.sqrt(arg))/(2*((lep.E()*lep.E()) -(lep.Pz()*lep.Pz())))
		newmet_p.SetPz(Pz_met_p)
		newmet_p.SetE(math.sqrt(newmet_p.Px()*newmet_p.Px()+newmet_p.Py()*newmet_p.Py()+newmet_p.Pz()*newmet_p.Pz()))
		newmet_m.SetPz(Pz_met_m)
		newmet_m.SetE(math.sqrt(newmet_m.Px()*newmet_m.Px()+newmet_m.Py()*newmet_m.Py()+newmet_m.Pz()*newmet_m.Pz()))
		return [newmet_p, newmet_m]	

def setup(variables, isData):
	variables['EventMass'] = array.array('f', [-1.0])
	for modifier in modifiers:
		variables["meteta_" + modifier] = array.array('f', [100.0])
		variables['WcandPt_' + modifier] = array.array('f', [-1.0])
		variables['WcandEta_' + modifier] = array.array('f', [100.0])
		variables['WcandPhi_' + modifier] = array.array('f', [100.0])
	return variables

def analyze(event, variables, labels, isData):
	unfittedMET = ROOT.TLorentzVector()
	lepVector = ROOT.TLorentzVector()
	
	# Also write out the "total event mass", using WcandPlus.
	eventReco = None
	for i in xrange(maxJets):
		jetName = "jet" + str(i + 1)
		eventJet = 
		if eventReco is None:
			eventReco = eventJet
		else:
			eventReco += eventJet
	
	# Create the four vectors, then use make_lepW to do fitted MET.
	electrons = labels['jhuElePFlow']['electron'].product()
	muons = labels['jhuMuonPFlow']['muon'].product()
	if not (len(electrons) == 0 and len(muons) == 0):
		unfittedMET.SetPtEtaPhiM(variables['metpt'][0], 0.0, variables['metphi'][0], 0.0)
		lepVector.SetPtEtaPhiM(variables['leppt'][0], variables['lepeta'][0], variables['lepphi'][0], variables['lepmass'][0])
		fittedMET = make_lepW(unfittedMET, lepVector)
		for i in xrange(2):
			variables['meteta_' + modifiers[i]][0] = fittedMET[i].Eta()
			W_cand = fittedMET[i] + lepVector
			if i == 0:
				eventReco + W_cand
			variables['WcandPt_' + modifiers[i]][0] = W_cand.Pt()
			variables['WcandEta_' + modifiers[i]][0] = W_cand.Eta()
			variables['WcandPhi_' + modifiers[i]][0] = W_cand.Phi()
	
	# I think this is the right total event mass, for the leptonic events.
	variables['EventMass'][0] = eventReco.M()
		
	return variables

def reset(variables):
	variables['EventMass'][0] = -1.0
	for modifier in modifiers:
		variables["meteta_" + modifier][0] = 100.0
		variables['WcandPt_' + modifier][0] = -1.0
		variables['WcandEta_' + modifier][0] = 100.0
		variables['WcandPhi_' + modifier][0] = 100.0
	return variables

def createCuts(cutArray):
	return cutArray

def makeCuts(event, variables, cutArray, labels, isData):
	return cutArray
