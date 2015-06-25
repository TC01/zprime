import array
import math
import ROOT
from math import *

def setup(variables, isData):
	variables['isGTt'] = array.array('f', [0.0])
	return variables

def createCuts(cuts): # Not used
	return cuts
	
def analyze(event, variables, labels, isData):	
	genHandle = labels['prunedGenParticles']['']
	genPart = genHandle.product()
	for ig in genPart:
		if math.fabs(ig.pdgId()) == 6:
		    if math.fabs(ig.mother().pdgId()) == 6000010:
			variables['isGTt'][0] = 1.0
	return variables
	
def makeCuts(event, variables, cuts, labels, isData): # Not used
	return cuts
	
def reset(variables):
	variables['isGTt'][0] = 0.0
	return variables
