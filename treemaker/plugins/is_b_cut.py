# Check if something is a W; jet mass > 30, < 140
# Creates three cuts for three jets; jet1_isw, jet2_isw, jet3_isw.

from Treemaker.Treemaker import cuts

numJets = 3
bMassMax = 50

def setup(variables, isData):
	return variables

def createCuts(cutArray):
	description = "Is the jet a b candidate?"
	cutArray["jet1_isb"] = cuts.Cut("Jet 1 b", description)
	cutArray["jet2_isb"] = cuts.Cut("Jet 2 b", description)
	cutArray["jet3_isb"] = cuts.Cut("Jet 3 b", description)
	return cutArray

def analyze(event, variables, labels, isData):
	return variables

def makeCuts(event, variables, cutArray, labels, isData):
	for i in range(numJets):
		jetName = "jet" + str(i)
		if variables[jetName + "mass"] < bMassMax:
			cutArray[jetName + "_isb"].passed = 1
	return cutArray

def reset(variables):
	return variables
