# copy of TT_TemplateMaker with correct values put in for N and a. Makes plots showing how well the morphing performed.

lumi = 19748.
import ROOT
from ROOT import *
from CutOnTree import writeplot

N = 1.6360463748350496
a = 0.4773194160462202

Nu = N + 0.4305091441738136
au = a - 0.9397537176912021
# no this isn't a type, recall that alpha is a negative factor but the value being listed here is positive, so a smaller alpha is closer to positve

Nd = N - 0.4305091441738136
ad = a + 0.9397537176912021
# no this isn't a type, recall that alpha is a negative factor but the value being listed here is positive, so a smaller alpha is closer to positve

#N = 0.96
#a = 0.0012

#Nu = N + 0.1
#au = a - 0.00023 # no this isn't a type, recall that alpha is a negative factor but the value being listed here is positive, so a smaller alpha is closer to positve

#Nd = N - 0.1
#ad = a + 0.00023 # no this isn't a type, recall that alpha is a negative factor but the value being listed here is positive, so a smaller alpha is closer to positve


TW = "("+str(N)+"*2.71828^(-"+str(a)+"*0.5*(MCantitoppt+MCtoppt)))"
TW_aup = "("+str(N)+"*2.71828^(-"+str(au)+"*0.5*(MCantitoppt+MCtoppt)))"
TW_adn = "("+str(N)+"*2.71828^(-"+str(ad)+"*0.5*(MCantitoppt+MCtoppt)))"
TW_Nup = "("+str(Nu)+"*2.71828^(-"+str(a)+"*0.5*(MCantitoppt+MCtoppt)))"
TW_Ndn = "("+str(Nd)+"*2.71828^(-"+str(a)+"*0.5*(MCantitoppt+MCtoppt)))"


p0 = "0.402504"
p1 = "0.000641416"
p2 = "0.124863"
p3 = "0.00452712"
p4 = "0.00024813"

ntW = "(" + p0 + " + " + p1 + " * (hadWcandmass - 80.))"
ntW_el = ntW
ntW_mu = ntW

ntWu = "(" + p0 + " + " + p1 + " * (hadWcandmass - 80.) + sqrt((hadWcandmass - 80.) * (hadWcandmass - 80.) * " + p3 + " * " + p3 + " + (hadWcandmass - 80.) * 2 * " + p4 + " + " + p2 + " * " + p2 + "))"
ntWd = "(" + p0 + " + " + p1 + " * (hadWcandmass - 80.) - sqrt((hadWcandmass - 80.) * (hadWcandmass - 80.) * " + p3 + " * " + p3 + " + (hadWcandmass - 80.) * 2 * " + p4 + " + " + p2 + " * " + p2 + "))"


rootDir = "/eos/uscms/store/user/bjr/trees/pruned/"

# singletop
sFileName = ['T_t-channel_TuneZ2star_8TeV-powheg-tauola.root',
             'T_s-channel_TuneZ2star_8TeV-powheg-tauola.root',
             'T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola.root',
             'Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola.root',
             'Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola.root',
             'Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola.root']
sxs = [56.4,3.79,11.117,30.7,1.768,11.117]
sn = [3758227, 259961, 497658, 1935072, 139974, 493460]
sFilePrefix = rootDir
# data
dFileNameE = rootDir + "SingleElectron.root"
dFileNameM = rootDir + "SingleMu.root"
# ttbar
tFileName = ["TTJets_SemiLeptMGDecays_8TeV-madgraph.root", "TTJets_FullLeptMGDecays_8TeV-madgraph.root"]
txs = [107.7,25.17]
tn = [25424818,12043695]
tFilePrefix = rootDir

# Define cuts we'll use:
# Cuts:
El = "cuts[0]>0.&cuts[2]>0."
Mu = "cuts[3]>0.&cuts[2]>0."

PreSel = "((lep2Drel>25.||lep2Ddr>0.5) && leppt > 25 && numjets > 2 && hadWcandpt > 200)"

# Poorly named these days, but whoops.
TopTag = "(hadWcandmass > 50 && hadWcandmass < 120 && hadWcandtau21 < 0.5)"
AntiTag = "(hadWcandmass > 50 && hadWcandmass < 120 && hadWcandtau21 > 0.5)"

# Subtractions: removed from estimate of NonTop
mtZPs = TH1F("mtZPs", "", 25, 0, 2500)
msZPs = TH1F("msZPs", "", 25, 0, 2500)

etZPs = TH1F("etZPs", "", 25, 0, 2500)
esZPs = TH1F("esZPs", "", 25, 0, 2500)

# Estimates:
mdZPe = TH1F("MU__NT", "", 25, 0, 2500)
edZPe = TH1F("EL__NT", "", 25, 0, 2500)

# data:
mdZP = TH1F("MU__DATA", "", 25, 0, 2500)
edZP = TH1F("EL__DATA", "", 25, 0, 2500)

# MC measurements:
mtZPm = TH1F("MU__tt", "", 25, 0, 2500)
msZPm = TH1F("MU__st", "", 25, 0, 2500)
etZPm = TH1F("EL__tt", "", 25, 0, 2500)
esZPm = TH1F("EL__st", "", 25, 0, 2500)

# Now we fill these all up:
#Subtraction:
for i in range(len(tFileName)): # ttbar
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPs, "EventMass", "("+PreSel+"&"+AntiTag+"&"+El+")", "("+ntW_el+"*"+TW+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPs, "EventMass", "("+PreSel+"&"+AntiTag+"&"+Mu+")", "("+ntW_mu+"*"+TW+")")
for i in range(len(sFileName)): # signle top
	writeplot(sFilePrefix+sFileName[i], lumi*sxs[i]/sn[i], esZPs, "EventMass", "("+PreSel+"&"+AntiTag+"&"+El+")", "("+ntW_el+")")
	writeplot(sFilePrefix+sFileName[i], lumi*sxs[i]/sn[i], msZPs, "EventMass", "("+PreSel+"&"+AntiTag+"&"+Mu+")", "("+ntW_mu+")")
#Estimates:
writeplot(dFileNameE, 1.0, edZPe, "EventMass", "("+PreSel+"&"+AntiTag+"&"+El+")", "("+ntW_el+")")
writeplot(dFileNameM, 1.0, mdZPe, "EventMass", "("+PreSel+"&"+AntiTag+"&"+Mu+")", "("+ntW_mu+")")
#data:
writeplot(dFileNameE, 1.0, edZP, "EventMass", "("+PreSel+"&"+TopTag+"&"+El+")", "1.0")
writeplot(dFileNameM, 1.0, mdZP, "EventMass", "("+PreSel+"&"+TopTag+"&"+Mu+")", "1.0")

# Fill MC:
for i in range(len(tFileName)): # All  versions of the ttbar
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPm, "EventMass", "("+PreSel+"&"+TopTag+"&"+El+")", "("+TW+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPm, "EventMass", "("+PreSel+"&"+TopTag+"&"+Mu+")", "("+TW+")")
for i in range(len(sFileName)):
	writeplot(sFilePrefix+sFileName[i], lumi*sxs[i]/sn[i], esZPm, "EventMass", "("+PreSel+"&"+TopTag+"&"+El+")", "1.0")
	writeplot(sFilePrefix+sFileName[i], lumi*sxs[i]/sn[i], msZPm, "EventMass", "("+PreSel+"&"+TopTag+"&"+Mu+")", "1.0")

# Correct the NonTop Est to not double-count anything:
edZPe.Add(esZPs,-1)
mdZPe.Add(msZPs,-1)

edZPe.Add(etZPs,-1)
mdZPe.Add(mtZPs,-1)

# Plotting:
# Colors
msZPm.SetFillColor(kViolet)
esZPm.SetFillColor(kViolet)
mtZPm.SetFillColor(kRed)
etZPm.SetFillColor(kRed)
mdZPe.SetFillColor(kSpring)
edZPe.SetFillColor(kSpring)

estack = THStack("E", "E")
estack.Add(esZPm)
estack.Add(etZPm)
estack.Add(edZPe)
mstack = THStack("M", "M")
mstack.Add(msZPm)
mstack.Add(mtZPm)
mstack.Add(mdZPe)

# Data (and pad info since we draw it first)

edZP.SetStats(0)
edZP.Sumw2()
edZP.SetLineColor(1)
edZP.SetFillColor(0)
edZP.SetMarkerColor(1)
edZP.SetMarkerStyle(20)
edZP.GetXaxis().SetTitle("Event Mass")
edZP.GetYaxis().SetTitle("events")


mdZP.SetStats(0)
mdZP.Sumw2()
mdZP.SetLineColor(1)
mdZP.SetFillColor(0)
mdZP.SetMarkerColor(1)
mdZP.SetMarkerStyle(20)
mdZP.GetXaxis().SetTitle("Event Mass")
mdZP.GetYaxis().SetTitle("events")


# Legend
bl = TLegend(0.5,0.6,0.89,0.89)
bl.SetFillColor(0)
bl.SetLineColor(0)

bl.AddEntry(mtZPm, "corr. semi-leptonic t#bar{t}", "F")
bl.AddEntry(mdZPe, "non-top bkg.", "F")
bl.AddEntry(msZPm, "single top", "F")
bl.AddEntry(mdZP, "data", "PL")



C = TCanvas()
C.Divide(2,1)
C.cd(1)
edZP.Draw()
edZP.GetYaxis().SetRangeUser(0, 80)
estack.Draw("same")
edZP.Draw("same")
bl.Draw()
C.cd(2)
mdZP.Draw()
mdZP.GetYaxis().SetRangeUser(0, 80)
mstack.Draw("same")
mdZP.Draw("same")
bl.Draw()

C.SaveAs("tt_check.pdf")
C.SaveAs("tt_check.png")

raw_input()
