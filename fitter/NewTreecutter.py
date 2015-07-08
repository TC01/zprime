import ROOT
from ROOT import *


def makePlot(plot, chain, var, jet, Cut, Weight, scale):
	newVar = jet + var
	chain.Draw(newVar+">>"+jet, Weight+"*"+Cut, "goff")
	plot.Scale(scale)
	return plot

	# Takes a File (which must contain a tree named "tree") and applies the cut "Cut" and the weight "Weight", then plots the var "var" on the TH1F "plot".
def writeplot(File, scale, plot, var, Cut, Weight):
	# Allows to add multiple distributions to the plot
#	temp1 = plot.Clone("jet1")
	temp2 = plot.Clone("jet2")
	temp3 = plot.Clone("jet3")

	chain = ROOT.TChain("tree")
	chain.Add(File)

	plot = makePlot(plot, chain, var, 'jet1', Cut, Weight, scale)
	temp2 = makePlot(temp2, chain, var, 'jet2', Cut, Weight, scale)
	temp3 = makePlot(temp3, chain, var, 'jet3', Cut, Weight, scale)

#	plot.Add(temp1)
	plot.Add(temp2)
	plot.Add(temp3)

	return plot


def make2DPlot(source, chain, varX, varY, jet, Cut, Weight, scale):
	plot = source.Clone(jet)

	newVarX = jet + varX
	newVarY = jet + varY

	# W-tag selection cut.
	Cut = "(" + Cut + " && " + newVarX + ' > 50 &&' + newVarX + " < 120 && " + jet + "pt" + " > 200)"

	chain.Draw(newVarY+":"+newVarX+">>" + jet, Weight+"*"+Cut, "goff")

	plot.Scale(scale)

#	canvas = ROOT.TCanvas()
#	canvas.cd()
#	plot.Draw('COLZ')
#	raw_input()

	return plot

def write2dplot(File, scale, plot, var, var2, Cut, Weight):
	chain = ROOT.TChain("tree")
	chain.Add(File)

	temp1 = make2DPlot(plot, chain, var, var2, 'jet1', Cut, Weight, scale)
	temp2 = make2DPlot(plot, chain, var, var2, 'jet2', Cut, Weight, scale)
	temp3 = make2DPlot(plot, chain, var, var2, 'jet3', Cut, Weight, scale)

	plot.Add(temp1)
	plot.Add(temp2)
	plot.Add(temp3)

	canvas = ROOT.TCanvas()
	canvas.cd()
	plot.Draw('COLZ')
	raw_input()


	return plot
