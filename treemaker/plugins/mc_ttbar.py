# Monte Carlo Top / Anti-Top plugin.
# Uses GenParticles collection.
# As this is a Monte Carlo plugin, it should not analyze() run if isData is True.

import array

from Treemaker.Treemaker import cuts

# No magic numbers!
PGD_TOP = 6
PGD_ANTITOP = -6

def setup(variables, isData):
	variables['MCtoppt'] = array.array('f', [-1.0])
	variables['MCantitoppt'] = array.array('f', [-1.0])
	return variables

def analyze(event, variables, labels, isData):
	if not isData:
		GenParticles = labels['PrunedGenParticles'][''].product()
		for particle in GenParticles:
			if particle.pgdId() == PGD_TOP:
				variables['MCtoppt'][0] = particle.pt()
			if particle.pgdId() == PGD_ANTITOP:
				variables['MCantitoppt'][0] = particle.pt()
	
	return variables

def reset(variables):
	variables['MCtoppt'][0] = -1.0
	variables['MCantitoppt'][0] = -1.0
	return variables

def createCuts(cutArray):
	return cutArray

def makeCuts(event, variables, cutArray, labels, isData):
	return cutArray
