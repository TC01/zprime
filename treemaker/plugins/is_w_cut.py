# Check if something is a W; jet mass > 30, < 140
# Creates three cuts for three jets; jet1_isw, jet2_isw, jet3_isw.

from Treemaker.Treemaker import cuts

numJets = 3
wMassMin = 50
wMassMax = 120
wPtMin = 200

def setup(variables, isData):
	return variables

def createCuts(cutArray):
	description = "Is the jet a W?"
	cutArray["jet1_isw"] = cuts.Cut("Jet 1 W", description)
	cutArray["jet2_isw"] = cuts.Cut("Jet 2 W", description)
	cutArray["jet3_isw"] = cuts.Cut("Jet 3 W", description)

	cutArray["jet1_isw_pt"] = cuts.Cut("Jet 1 W with Pt", description)
	cutArray["jet2_isw_pt"] = cuts.Cut("Jet 2 W with Pt", description)
	cutArray["jet3_isw_pt"] = cuts.Cut("Jet 3 W with Pt", description)

	return cutArray

def analyze(event, variables, labels, isData):
	return variables

def makeCuts(event, variables, cutArray, labels, isData):
	for i in range(numJets):
		jetName = "jet" + str(i + 1)
		if variables[jetName + "mass"][0] > wMassMin and variables[jetName + "mass"][0] < wMassMax:
			if variables[jetName + "pt"][0] > wPtMin:
				cutArray[jetName + "_isw_pt"].passed = 1
			cutArray[jetName + "_isw"].passed = 1
	return cutArray

def reset(variables):
	return variables
