### DRAW OUR FULL SELECTION PLOTS:
import os
import math
from array import array
import ROOT
import sys
import scipy
from ROOT import *

F = TFile("Zprime_Theta_Feed.root")

height = 50

# Make the Data Pretty:
eData = F.Get("EL__DATA")
mData = F.Get("MU__DATA")
for i in [eData,mData]:
	i.SetStats(0)
	i.Sumw2()
	i.SetLineColor(1)
	i.SetFillColor(0)
	i.SetMarkerColor(1)
	i.SetMarkerStyle(20)
	i.GetYaxis().SetTitle("events / 100 GeV")
	i.GetXaxis().SetTitle("Event Mass: m_{tbW} [GeV]")
# Import Backgrounds:
eST = F.Get("EL__ST")
eST.SetFillColor(kViolet)
eTT = F.Get("EL__TT")
eTT.SetFillColor(kRed)
eNT = F.Get("EL__NT")
eNT.SetFillColor(kSpring)
mST = F.Get("MU__ST")
mST.SetFillColor(kViolet)
mTT = F.Get("MU__TT")
mTT.SetFillColor(kRed)
mNT = F.Get("MU__NT")
mNT.SetFillColor(kSpring)


# Plot the Signal
eZ15 = F.Get('EL__zp1500')
mZ15 = F.Get('MU__zp1500')
for i in [eZ15, mZ15]:
	i.SetLineColor(kBlue)
	i.SetLineWidth(2)
# Make the stacks:
eStack = THStack("estack", "")
eStack.Add(eST)
eStack.Add(eTT)
eStack.Add(eNT)
mStack = THStack("mstack", "")
mStack.Add(mST)
mStack.Add(mTT)
mStack.Add(mNT)
# make BKGHeight, we'll need this later:
ebkgH = eST.Clone("eB")
ebkgH.Add(eTT,1)
ebkgH.Add(eNT,1)
mbkgH = mST.Clone("eB")
mbkgH.Add(mTT,1)
mbkgH.Add(mNT,1)

# Get the errors:
eNT_fu = F.Get("EL__NT__linfiterr__up")
eNT_fd = F.Get("EL__NT__linfiterr__down")
eNT_Nu = F.Get("EL__NT__N__up")
eNT_Nd = F.Get("EL__NT__N__down")
eNT_au = F.Get("EL__NT__a__up")
eNT_ad = F.Get("EL__NT__a__down")
eTT_Nu = F.Get("EL__TT__N__up")
eTT_Nd = F.Get("EL__TT__N__down")
eTT_au = F.Get("EL__TT__a__up")
eTT_ad = F.Get("EL__TT__a__down")

mNT_fu = F.Get("MU__NT__linfiterr__up")
mNT_fd = F.Get("MU__NT__linfiterr__down")
mNT_Nu = F.Get("MU__NT__N__up")
mNT_Nd = F.Get("MU__NT__N__down")
mNT_au = F.Get("MU__NT__a__up")
mNT_ad = F.Get("MU__NT__a__down")
mTT_Nu = F.Get("MU__TT__N__up")
mTT_Nd = F.Get("MU__TT__N__down")
mTT_au = F.Get("MU__TT__a__up")
mTT_ad = F.Get("MU__TT__a__down")

# Make the pull plot:
ePull = eData.Clone("ePull")
ePull.SetFillColor(kBlue-3)
ePull.Add(eST,-1)
ePull.Add(eTT,-1)
ePull.Add(eNT,-1)
mPull = mData.Clone("mPull")
mPull.SetFillColor(kBlue-3)
mPull.Add(mST,-1)
mPull.Add(mTT,-1)
mPull.Add(mNT,-1)

eBoxes = []
mBoxes = []

for i in range(ePull.GetNbinsX()+1):
	V = ePull.GetBinContent(i)
	ue = math.sqrt((eNT_fu.GetBinContent(i) - eNT.GetBinContent(i))**2 + (eNT_Nu.GetBinContent(i) - eNT.GetBinContent(i))**2 + (eNT_au.GetBinContent(i) - eNT.GetBinContent(i))**2 + (eTT_Nu.GetBinContent(i) - eTT.GetBinContent(i))**2 + (eTT_au.GetBinContent(i) - eTT.GetBinContent(i))**2 + (eST.GetBinContent(i)*0.2)**2 + eData.GetBinErrorUp(i)**2)
	de = math.sqrt((eNT_fd.GetBinContent(i) - eNT.GetBinContent(i))**2 + (eNT_Nd.GetBinContent(i) - eNT.GetBinContent(i))**2 + (eNT_ad.GetBinContent(i) - eNT.GetBinContent(i))**2 + (eTT_Nd.GetBinContent(i) - eTT.GetBinContent(i))**2 + (eTT_ad.GetBinContent(i) - eTT.GetBinContent(i))**2 + (eST.GetBinContent(i)*0.2)**2 + eData.GetBinErrorLow(i)**2)
	if V > 0.:
		e = ue
	else:
		e = de
	if e > 1:
		f = V/e
	else:
		f = e
	x1 = ePull.GetBinCenter(i) - (0.5*ePull.GetBinWidth(i))
	y1 = ebkgH.GetBinContent(i) - de
	if y1 < 0.:
		y1 = 0
	x2 = ePull.GetBinCenter(i) + (0.5*ePull.GetBinWidth(i))
	y2 = ebkgH.GetBinContent(i) + ue
	ePull.SetBinContent(i, f)
	tempbox = TBox(x1,y1,x2,y2)
	eBoxes.append(tempbox)

for i in range(mPull.GetNbinsX()+1):
	V = mPull.GetBinContent(i)
	ue = math.sqrt((mNT_fu.GetBinContent(i) - mNT.GetBinContent(i))**2 + (mNT_Nu.GetBinContent(i) - mNT.GetBinContent(i))**2 + (mNT_au.GetBinContent(i) - mNT.GetBinContent(i))**2 + (mTT_Nu.GetBinContent(i) - mTT.GetBinContent(i))**2 + (mTT_au.GetBinContent(i) - mTT.GetBinContent(i))**2 + (mST.GetBinContent(i)*0.2)**2 + mData.GetBinErrorUp(i)**2)
	de = math.sqrt((mNT_fd.GetBinContent(i) - mNT.GetBinContent(i))**2 + (mNT_Nd.GetBinContent(i) - mNT.GetBinContent(i))**2 + (mNT_ad.GetBinContent(i) - mNT.GetBinContent(i))**2 + (mTT_Nd.GetBinContent(i) - mTT.GetBinContent(i))**2 + (mTT_ad.GetBinContent(i) - mTT.GetBinContent(i))**2 + (mST.GetBinContent(i)*0.2)**2 + mData.GetBinErrorLow(i)**2)
	if V > 0.:
		e = ue
	else:
		e = de
	if e > 1:
		f = V/e
	else:
		f = e
	mPull.SetBinContent(i, f)
	x1 = mPull.GetBinCenter(i) - (0.5*mPull.GetBinWidth(i))
	y1 = mbkgH.GetBinContent(i) - de
	if y1 < 0.:
		y1 = 0
	x2 = mPull.GetBinCenter(i) + (0.5*mPull.GetBinWidth(i))
	y2 = mbkgH.GetBinContent(i) + ue
	tempbox = TBox(x1,y1,x2,y2)
	mBoxes.append(tempbox)

for k in [eBoxes,mBoxes]:
	for i in k:
		i.SetFillColor(49)
		i.SetFillStyle(3335)

# Beautify pull plots:
for P in [ePull,mPull]:
	P.GetXaxis().SetTitle("")
	P.SetFillStyle(1001)
	P.SetLineColor(kBlue-3)
	P.SetFillColor(kBlue-3)
	P.GetXaxis().SetNdivisions(0)
	P.GetYaxis().SetNdivisions(4)
	P.GetYaxis().SetTitle("(Data - Bkg)/#sigma")
	P.GetYaxis().SetLabelSize(85/15*P.GetYaxis().GetLabelSize())
	P.GetYaxis().SetTitleSize(4.2*P.GetYaxis().GetTitleSize())
	P.GetYaxis().SetTitleOffset(0.175)
	P.GetYaxis().SetRangeUser(-3.,3.)

# Legend
be = TLegend(0.5,0.6,0.89,0.89)
be.SetHeader("Electron Events")
be.SetFillColor(0)
be.SetLineColor(0)
be.AddEntry(eData, "data", "PL")
be.AddEntry(eTT, "semi-leptonic t#bar{t}", "F")
be.AddEntry(eNT, "non-top bkg.", "F")
be.AddEntry(eST, "single top", "F")
be.AddEntry(eBoxes[0], "error in BKG est", "F")
#be.AddEntry(eZ15, "Z'_{1.5TeV}", "L")

bm = TLegend(0.5,0.6,0.89,0.89)
bm.SetHeader("Muon Events")
bm.SetFillColor(0)
bm.SetLineColor(0)
bm.AddEntry(mData, "data", "PL")
bm.AddEntry(mTT, "semi-leptonic t#bar{t}", "F")
bm.AddEntry(mNT, "non-top bkg.", "F")
bm.AddEntry(mST, "single top", "F")
bm.AddEntry(mBoxes[0], "error in BKG est", "F")
#bm.AddEntry(mZ15, "Z'_{1.5TeV}", "L")

eC = TCanvas("eC","",700,550)
eplot = TPad("epad1", "The pad 80% of the height",0,0.15,1,1)
epull = TPad("epad2", "The pad 20% of the height",0,0,1.0,0.15)
eplot.Draw()
epull.Draw()
eplot.cd()
eData.Draw()
eData.GetYaxis().SetRangeUser(0.,height)
eStack.Draw("same")
#eZ15.Draw("same")
eData.Draw("same")
for i in eBoxes:
	i.Draw("same")
be.Draw("same")
epull.cd()
ePull.Draw("hist")
eC.Update()

eC.SaveAs("electrons_sr_fit.pdf")
eC.SaveAs("electrons_sr_fit.png")

mC = TCanvas("mC","",700,550)
mplot = TPad("mpad1", "The pad 80% of the height",0,0.15,1,1)
mpull = TPad("mpad2", "The pad 20% of the height",0,0,1.0,0.15)
mplot.Draw()
mpull.Draw()
mplot.cd()
mData.Draw()
mData.GetYaxis().SetRangeUser(0., height)
mStack.Draw("same")
#mZ15.Draw("same")
mData.Draw("same")
for i in mBoxes:
	i.Draw("same")
bm.Draw("same")
mpull.cd()
mPull.Draw("hist")
mC.Update()

mC.SaveAs("muons_sr_fit.pdf")
mC.SaveAs("muons_sr_fit.png")

raw_input()
