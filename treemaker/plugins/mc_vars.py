import array
import math
import os
import sys
from math import *
import ROOT

def setup(variables, isData):
	variables['trigW'] = array.array('f', [1.0])
	variables['trigWEu'] = array.array('f', [0.0])
	variables['trigWEd'] = array.array('f', [0.0])
	return variables

def createCuts(cuts): # Not used
	return cuts
	
def analyze(event, variables, labels, isData):	
	return variables
	
def makeCuts(event, variables, cuts, labels, isData): # Not used
	pt = variables['leppt'][0]
	eta = math.fabs(variables['lepeta'][0])
	path = os.path.join(os.environ['CMSSW_BASE'], 'src', 'Treemaker', 'Treemaker', 'python', 'plugins')
	if cuts['isMuon'].passed > 0.5:
		File = ROOT.TFile(os.path.join(path, "SingleMuonTriggerEfficiencies_eta2p1_Run2012ABCD_v5trees.root"))
		if eta < 0.9:
			graph = File.Get("IsoMu24_eta2p1_DATA_over_MC_TightID_IsodB_PT_ABSETA_Barrel_0to0p9_pt25-500_2012ABCD")
		elif eta > 0.9 and eta < 1.2:
			graph = File.Get("IsoMu24_eta2p1_DATA_over_MC_TightID_IsodB_PT_ABSETA_Transition_0p9to1p2_pt25-500_2012ABCD")
		else:
			graph = File.Get("IsoMu24_eta2p1_DATA_over_MC_TightID_IsodB_PT_ABSETA_Endcaps_1p2to2p1_pt25-500_2012ABCD")
		variables['trigW'][0] = graph.Eval(pt)
		Tuple = maketuple(graph)
		point = findnearestpoint(Tuple, pt)
		variables['trigWEu'][0] = point[0]
		variables['trigWEd'][0] = point[1]
		variables['trigW'][0] = point[2]
	elif cuts['isElectron'].passed > 0.5:
		File = ROOT.TFile(os.path.join(path, "electrons_scale_factors.root"))
		graph = File.Get("electronsDATAMCratio_FO_ID")
		bin = graph.FindBin(eta,pt)
		bin1 = ROOT.Long(0.)
		bin2 = ROOT.Long(0.)
		bin3 = ROOT.Long(0.)
		graph.GetBinXYZ(bin, bin1, bin2, bin3)
		b1 = int(bin1)
		b2 = int(bin2)
		variables['trigW'][0] = graph.GetBinContent(bin)
		variables['trigWEu'][0] = graph.GetBinErrorUp(b1,b2)
		variables['trigWEd'][0] = graph.GetBinErrorLow(b1,b2)
	return cuts
	
def reset(variables):
	variables['trigW'][0] = 1.0
	variables['trigWEu'][0] = 0.0
	variables['trigWEd'][0] = 0.0
	return variables

def maketuple(graph):
	tupe = []
	for i in range(0, graph.GetN()-1):
		X = ROOT.Double(0.)
		Y = ROOT.Double(0.)
		graph.GetPoint(i,X,Y)
		bottom = X - graph.GetErrorXlow(i)
		top = X + graph.GetErrorXhigh(i)
		errorUp = graph.GetErrorYhigh(i)
		errorDown = graph.GetErrorYlow(i)
		tupe.append([bottom,top,errorUp,errorDown,Y])
	return tupe
def findnearestpoint(Tuple, pt):
	Y = 0.0
	up = 0.0
	down = 0.0
	for i in Tuple:
		if pt < i[1] and pt > i[0]:
			Y = i[4]
			up = i[2]
			down = i[3]
	if pt > Tuple[len(Tuple) - 1][1]:
		up = Tuple[len(Tuple) - 1][2]
		down = Tuple[len(Tuple) - 1][3]
		Y = Tuple[len(Tuple) - 1][4]
	return [up,down,Y]
	# returns the nearest point in the graph to the bin specified. Maybe one day root will be real and let you eval the error?

