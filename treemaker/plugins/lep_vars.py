import array

# Leptons plugin. This plugin also has some cuts for is_muon and is_electron.
# (and is_had, of course).

from Treemaker.Treemaker import cuts

def setup(variables, isData):
	variables['lepphi'] = array.array('f', [100.0])
	variables['leppt'] = array.array('f', [-1.0])
	variables['lepeta'] = array.array('f', [100.0])
	variables['lepmass'] = array.array('f', [-1.0])
	return variables

def fillLeptons(variables, vector):
	variables['leppt'][0] = vector[0].Pt()
	variables['lepphi'][0] = vector[0].Phi()
	variables['lepeta'][0] = vector[0].Eta()
	variables['lepmass'][0] = vector[0].M()
	return variables

def analyze(event, variables, labels, isData):
	electrons = labels['jhuElePFlow']['electron'].product()
	muons = labels['jhuMuonPFlow']['muon'].product()
	# Do nothing if there are no electrons *or* muons.
	if len(electrons) == 0 and len(muons) == 0:
		return variables
	
	# Sort into three different categories: only the muons and electrons one
	# is hard.
	if len(electrons) == 0 and len(muons) > 0:
		variables = fillLeptons(variables, electrons)
	elif len(electrons) > 0 and len(muons) == 0:
		variables = fillLeptons(variables, muons)
	else:
		if electrons[0].Pt() > muons[0].Pt():
			variables = fillLeptons(variables, electrons)
		else:
			variables = fillLeptons(variables, muons)
		
	return variables

def reset(variables):
	variables['leppt'][0] = -1.0
	variables['lepphi'][0] = 100.0
	variables['lepeta'][0] = 100.0
	variables['lepmass'][0] = -1.0
	return variables

def createCuts(cutArray):
	cutArray["isHadronic"] = cuts.Cut("Hadronic", "Is the event purely hadronic?")
	cutArray["isMuon"] = cuts.Cut("Muon", "Is the event a muon event?")
	cutArray["isElectron"] = cuts.Cut("Electron", "Is the event an electron event?")
	return cutArray

def makeCuts(event, variables, cutArray, labels, isData):
	# It may *seem* expensive to do this again... I'm not sure if it is or isn't.
	# Certainly it's not very expensive at all compared to Handle, which is OOM worse.
	# Maybe we should put .product() in labels.
	electrons = labels['jhuElePFlow']['electron'].product()
	muons = labels['jhuMuonPFlow']['muon'].product()
	if len(electrons) == 0 and len(muons) == 0:
		cutArray['isHadronic'].passed = 1
	elif len(electrons) == 0 and len(muons) > 0:
		cutArray['isMuon'].passed = 1
	elif len(muons) == 0 and len(electrons) > 0:
		cutArray['isElectron'].passed = 1
	else:
		if electrons[0].Pt() > muons[0].Pt():
			cutArray['isElectron'].passed = 1
		else:
			cutArray['isMuon'].passed = 1
	return cutArray
