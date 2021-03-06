# This file creates the template morphing distribions Theta needs to pin down the ttbar parameters. Output is a root file containing all the histograms.
lumi = 19748.
import ROOT
from ROOT import *
from CutOnTree import writeplot


#### Define the template weights for the renormanliztion of TTBAR:
# use functional form: N * e^(a * HT / 2)
# N = 1.0
# a = 0.0013
# 1 sig N guess is 20%
# 1 sig a guess is -20% <-- note that a smaller a gives a bigger effect (careful!)

TW = "(1.0*2.71828^(-0.0013*0.5*(MCantitoppt+MCtoppt)))" # central
TW_nu = "(1.0*1.20*2.71828^(-0.0013*0.5*(MCantitoppt+MCtoppt)))" # N up
TW_nd = "(1.0*0.80*2.71828^(-0.0013*0.5*(MCantitoppt+MCtoppt)))" # N down
TW_au = "(1.0*2.71828^(-0.0013*0.80*0.5*(MCantitoppt+MCtoppt)))" # a up
TW_ad = "(1.0*2.71828^(-0.0013*1.20*0.5*(MCantitoppt+MCtoppt)))" # a down
# NT-est vars (and errors)

p0 = '0.425371'
p1 = '0.00916933'
p2 = '0.210172'
p3 = '0.00756191'
p4 = '0.00105536'

p0 = '0.482869'
p1 = '0.00532022'
p2 = '0.089892'
p3 = '0.00339438'
p4 = '0.000187741'

p0 = '0.547774'
p1 = '0.00755772'
p2 = '0.0974039'
p3 = '0.00368537'
p4 = '0.000239982'

p0 = '0.583043'
p1 = '0.00877524'
p2 = '0.101541'
p3 = '0.00384622'
p4 = '0.000270291'


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


PreSel = "((lep2Drel>25.||lep2Ddr>0.5) && leppt > 25 && numjets > 2 && hadWcandpt > 200 && leptopcandmass > 140 && leptopcandmass < 250)"

# Poorly named these days, but whoops.
TopTag = "(hadWcandmass > 50 && hadWcandmass < 120 && hadWcandtau21 < 0.5)"
AntiTag = "(hadWcandmass > 50 && hadWcandmass < 120 && hadWcandtau21 > 0.5)"


# Subtractions: removed from estimate of NonTop
mtZPs = TH1F("mtZPs", "", 25, 0, 2500)
msZPs = TH1F("msZPs", "", 25, 0, 2500)

etZPs = TH1F("etZPs", "", 25, 0, 2500)
esZPs = TH1F("esZPs", "", 25, 0, 2500)

mtZPs_nu = TH1F("mtZPs_nu", "", 25, 0, 2500)
etZPs_nu = TH1F("etZPs_nu", "", 25, 0, 2500)
mtZPs_nd = TH1F("mtZPs_nd", "", 25, 0, 2500)
etZPs_nd = TH1F("etZPs_nd", "", 25, 0, 2500)
mtZPs_au = TH1F("mtZPs_au", "", 25, 0, 2500)
etZPs_au = TH1F("etZPs_au", "", 25, 0, 2500)
mtZPs_ad = TH1F("mtZPs_ad", "", 25, 0, 2500)
etZPs_ad = TH1F("etZPs_ad", "", 25, 0, 2500)

# plots: Save to this file:
savefile = TFile("TTBAR_THETA_FEED.root", "RECREATE")
savefile.cd()

# Estimates:
mdZPe = TH1F("MU__NT", "", 25, 0, 2500)
edZPe = TH1F("EL__NT", "", 25, 0, 2500)
mdZPe_nu = TH1F("MU__NT__N__up", "", 25, 0, 2500)
edZPe_nu = TH1F("EL__NT__N__up", "", 25, 0, 2500)
mdZPe_nd = TH1F("MU__NT__N__down", "", 25, 0, 2500)
edZPe_nd = TH1F("EL__NT__N__down", "", 25, 0, 2500)
mdZPe_au = TH1F("MU__NT__a__up", "", 25, 0, 2500)
edZPe_au = TH1F("EL__NT__a__up", "", 25, 0, 2500)
mdZPe_ad = TH1F("MU__NT__a__down", "", 25, 0, 2500)
edZPe_ad = TH1F("EL__NT__a__down", "", 25, 0, 2500)

# data:
mdZP = TH1F("MU__DATA", "", 25, 0, 2500)
edZP = TH1F("EL__DATA", "", 25, 0, 2500)

# MC measurements:
mtZPm = TH1F("MU__tt", "", 25, 0, 2500)
mtZPm_nu = TH1F("MU__tt__N__up", "", 25, 0, 2500)
mtZPm_nd = TH1F("MU__tt__N__down", "", 25, 0, 2500)
mtZPm_au = TH1F("MU__tt__a__up", "", 25, 0, 2500)
mtZPm_ad = TH1F("MU__tt__a__down", "", 25, 0, 2500)
msZPm = TH1F("MU__st", "", 25, 0, 2500)
etZPm = TH1F("EL__tt", "", 25, 0, 2500)
etZPm_nu = TH1F("EL__tt__N__up", "", 25, 0, 2500)
etZPm_nd = TH1F("EL__tt__N__down", "", 25, 0, 2500)
etZPm_au = TH1F("EL__tt__a__up", "", 25, 0, 2500)
etZPm_ad = TH1F("EL__tt__a__down", "", 25, 0, 2500)
esZPm = TH1F("EL__st", "", 25, 0, 2500)

# Now we fill these all up:
#Subtraction:
for i in range(len(tFileName)): # ttbar
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPs, "EventMass", "("+PreSel+"&"+AntiTag+"&"+El+")", "("+ntW_el+"*"+TW+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPs, "EventMass", "("+PreSel+"&"+AntiTag+"&"+Mu+")", "("+ntW_mu+"*"+TW+")")

	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPs_nu, "EventMass", "("+PreSel+"&"+AntiTag+"&"+El+")", "("+ntW_el+"*"+TW_nu+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPs_nu, "EventMass", "("+PreSel+"&"+AntiTag+"&"+Mu+")", "("+ntW_mu+"*"+TW_nu+")")

	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPs_nd, "EventMass", "("+PreSel+"&"+AntiTag+"&"+El+")", "("+ntW_el+"*"+TW_nd+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPs_nd, "EventMass", "("+PreSel+"&"+AntiTag+"&"+Mu+")", "("+ntW_mu+"*"+TW_nd+")")

	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPs_au, "EventMass", "("+PreSel+"&"+AntiTag+"&"+El+")", "("+ntW_el+"*"+TW_au+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPs_au, "EventMass", "("+PreSel+"&"+AntiTag+"&"+Mu+")", "("+ntW_mu+"*"+TW_au+")")

	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPs_ad, "EventMass", "("+PreSel+"&"+AntiTag+"&"+El+")", "("+ntW_el+"*"+TW_ad+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPs_ad, "EventMass", "("+PreSel+"&"+AntiTag+"&"+Mu+")", "("+ntW_mu+"*"+TW_ad+")")
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

	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPm_nu, "EventMass", "("+PreSel+"&"+TopTag+"&"+El+")", "("+TW_nu+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPm_nu, "EventMass", "("+PreSel+"&"+TopTag+"&"+Mu+")", "("+TW_nu+")")

	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPm_nd, "EventMass", "("+PreSel+"&"+TopTag+"&"+El+")", "("+TW_nd+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPm_nd, "EventMass", "("+PreSel+"&"+TopTag+"&"+Mu+")", "("+TW_nd+")")

	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPm_au, "EventMass", "("+PreSel+"&"+TopTag+"&"+El+")", "("+TW_au+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPm_au, "EventMass", "("+PreSel+"&"+TopTag+"&"+Mu+")", "("+TW_au+")")

	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPm_ad, "EventMass", "("+PreSel+"&"+TopTag+"&"+El+")", "("+TW_ad+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPm_ad, "EventMass", "("+PreSel+"&"+TopTag+"&"+Mu+")", "("+TW_ad+")")
for i in range(len(sFileName)):
	writeplot(sFilePrefix+sFileName[i], lumi*sxs[i]/sn[i], esZPm, "EventMass", "("+PreSel+"&"+TopTag+"&"+El+")", "1.0")
	writeplot(sFilePrefix+sFileName[i], lumi*sxs[i]/sn[i], msZPm, "EventMass", "("+PreSel+"&"+TopTag+"&"+Mu+")", "1.0")

# Correct the NonTop Est to not double-count anything:
edZPe.Add(esZPs,-1)
mdZPe.Add(msZPs,-1)
edZPe_nu.Add(edZPe)
mdZPe_nu.Add(mdZPe)
edZPe_nd.Add(edZPe)
mdZPe_nd.Add(mdZPe)
edZPe_au.Add(edZPe)
mdZPe_au.Add(mdZPe)
edZPe_ad.Add(edZPe)
mdZPe_ad.Add(mdZPe)

edZPe.Add(etZPs,-1)
mdZPe.Add(mtZPs,-1)
edZPe_nu.Add(etZPs_nu,-1)
mdZPe_nu.Add(mtZPs_nu,-1)
edZPe_nd.Add(etZPs_nd,-1)
mdZPe_nd.Add(mtZPs_nd,-1)
edZPe_au.Add(etZPs_au,-1)
mdZPe_au.Add(mtZPs_au,-1)
edZPe_ad.Add(etZPs_ad,-1)
mdZPe_ad.Add(mtZPs_ad,-1)

savefile.Write()
savefile.Save()









