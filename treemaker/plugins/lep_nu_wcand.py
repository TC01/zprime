# A plugin that turns a nu + lepton (lep* + met*) into a W candidate
# Depends on lep_vars, met_vars.

import array

from Treemaker.Treemaker import cuts

# Code from Marc used in Ye Olde G* Analysis Treemaker
def make_lepW(met, lep):
	
	pass

def setup(variables, isData):
	variables['meteta_plus'] = array.array('f', [100.0])
	variables['meteta_minus'] = array.array('f', [100.0])
	modifiers = ["plus", "minus"]
	for modifier in modifiers:
		variables['WcandPt_' + modifier] = array.array('f', [-1.0])
		variables['WcandEta_' + modifier] = array.array('f', [100.0])
		variables['WcandPhi_' + modifier] = array.array('f', [100.0])
	return variables

def analyze(event, variables, labels, isData):
	ptHandle = labels['jhuGen']['metpt']
	phiHandle = labels['jhuGen']['metphi']
	if ptHandle.isValid() and phiHandle.isValid():
		variables['metpt'][0] = ptHandle.product()[0]
		variables['metphi'][0] = phiHandle.product()[0]
	return variables

def reset(variables):
	variables['metpt'][0] = -1.0
	variables['metphi'][0] = 100.0
	return variables

def createCuts(cutDict):
	return cuts

def makeCuts(event, variables, cutDict, labels, isData):
	return cuts