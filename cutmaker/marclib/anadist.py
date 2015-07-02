
import os
import glob
import math
import ROOT
#from ROOT import *
import sys

class singledist:
	def __init__(self, n, v, c, ch, f, s, b):
	# Creates a simple histogram named "n" of a varbiale "v", with cuts "c", from chain "ch", in file "f" and with a scale "s = [xs, lumi, numMCevents]". Bound are set in the final variable: "b" (which is "[bins, min, max]").
		chain = ROOT.TChain(ch)
		chain.Add(f)
		self.hist = ROOT.TH1F(n, n, b[0], b[1], b[2])
		chain.Draw(v+">>"+n,""+c, "goff")
		self.eff = self.hist.Integral()/s[2]
		self.hist.Scale(s[0]*s[1]/s[2])
		self.binning = b
	def GETBINNING(self):
		return self.binning
	def GET(self):
#	RETURNS THE HISTOGRAM
		return self.hist
	def GETEFF(self):
		return (100*self.eff)
	def GETINT(self):
		return self.hist.Integral()

class multidist:
	# Combines multiple "singledist" objects into an object with name "n", divided between "b" and "s" (background, signal). bc and bs are the colors. This can be done inside a mass window "mw"
	def __init__(self, n, b, s, d, bc, sc, mw):
		self.b = b
		self.s = s
		self.bn = 0
		self.sn = 0
		self.bstack = ROOT.THStack(n+"_bkg", "")
		self.sstack = ROOT.THStack(n+"_sig", "")
		for i in range(len(b)):
			b[i].SetTitle("")
			b[i].GetYaxis().SetTitle("events")
			b[i].GetXaxis().SetTitle("inv. mass (GeV)")
			b[i].SetLineColor(1)
			b[i].SetLineWidth(1)
			b[i].SetFillColor(bc[i])
			self.bn = self.bn + getInt(b[i], mw)
			self.bstack.Add(b[i])	
		for i in range(len(s)):
			s[i].SetTitle("")
			s[i].GetYaxis().SetTitle("events")
			s[i].GetXaxis().SetTitle("inv. mass (GeV)")
			s[i].SetLineColor(sc[i])
			s[i].SetLineWidth(3)
			self.sn = self.sn + getInt(s[i], mw)
			self.sstack.Add(s[i], "same")
		self.data = d.Clone('data')
		self.data.SetFillColor(0)
		self.data.SetLineColor(1)
		self.data.Sumw2()
		self.data.SetMarkerStyle(20)
		#self.data.SetMarkerSize(5)
	def GET(self):
			stacks =  [self.bstack, self.sstack]
			return stacks
	def PLOTSTACKS(self, pn, bn, sn, dn, C, xname, title="", logscale=False): # background/signal names (for legend). C are coordinates for the l. Save name for pdf is "pn".
			leg = ROOT.TLegend(C[0], C[1], C[2], C[3])
			leg.SetLineColor(0)
			leg.SetFillColor(0)
			leg.AddEntry(self.data, dn, "P")
			for i in range(len(self.b)):
				if bn[i] != "":
					leg.AddEntry(self.b[i], bn[i], "F")
			for i in range(len(self.s)):
				if sn[i] != "":
					leg.AddEntry(self.s[i], sn[i], "L")
			hh = 0
			for i in self.b:
				hh = ROOT.TMath.Max(hh, i.GetMaximum())
			for j in self.s:
				hh = ROOT.TMath.Max(hh, j.GetMaximum())
			hh = ROOT.TMath.Max(hh, self.sstack.GetMaximum())
			hh = ROOT.TMath.Max(hh, self.bstack.GetMaximum())
			self.bstack.SetMaximum(hh*1.2)
			c = ROOT.TCanvas("itt"+pn)
			c.cd()
			if logscale:
				c.SetLogy()
			self.bstack.Draw()
			self.bstack.GetYaxis().SetTitle("events")
			self.bstack.GetXaxis().SetTitle(xname)
			self.bstack.SetTitle(title)
			plots = []
			for i in self.sstack.GetStack():
				new = i
				for plot in plots:
					new.Add(plot, -1)
				plots.append(i)
				new.Draw("same")
				c.Update()

				# Change by Ben Rosser: STATISTICS!
				factor = 1
				
				shiftDown = new.GetMean() - factor * new.GetRMS()
				shiftUp = new.GetMean() + factor * new.GetRMS()
				lastBackground = self.bstack.GetHists(self.bstack.GetNhists())
				startBin = lastBackground.FindBin(shiftDown)
				endBin = lastBackground.FindBin(shiftUp)
				
				bkgEvents = lastBackground.Integral(startBin, endBin)
				with open('output.log', 'ab') as outputLog:
					outputLog.write(sn + ": S = " + new.GetEffectiveEntries() + ", B = " + str(bkgEvents) + "\n")
					answer = new.GetEffectiveEntries() / (1.5 + math.sqrt(bkgEvents))
					outputLog.write("        Eff(Sig) / (1.5 + sqrt(B)) = ", answer)

			self.data.Draw("same,E")
			leg.Draw()
			c.SaveAs(pn+".pdf")
			c.SaveAs(pn+".png")


def getInt(h, mw):
	l = h.FindBin(mw[0])
	u = h.FindBin(mw[1])
	return h.Integral(l, u)
