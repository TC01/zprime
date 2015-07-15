import ROOT
from ROOT import *
from CutOnTree import writeplot


####
## Code that assembles all (I do mean all) relevant histograms for output to theta. DOES NOT ADD SIGNAL. SIGNAL POINTS ARE PROCESSED SEPARATELY AND -M-U-S-T- BE PROCESSED SECOND.
####

# Defs:
lumi = 19748.

#rootDir = "/srv/data"
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

N = 1 + 0.2*1.6360463748350496
a = 0.0013 - (0.2*0.4773194160462202*0.0013)

Nu = N + 0.2*0.4305091441738136
au = a - 0.2*0.9397537176912021 * 0.0013

Nd = N - 0.2*0.4305091441738136
ad = a + 0.2*0.9397537176912021 * 0.0013

TW = "("+str(N)+"*2.71828^(-"+str(a)+"*0.5*(MCantitoppt+MCtoppt)))"
TW_aup = "("+str(N)+"*2.71828^(-"+str(au)+"*0.5*(MCantitoppt+MCtoppt)))"
TW_adn = "("+str(N)+"*2.71828^(-"+str(ad)+"*0.5*(MCantitoppt+MCtoppt)))"
TW_Nup = "("+str(Nu)+"*2.71828^(-"+str(a)+"*0.5*(MCantitoppt+MCtoppt)))"
TW_Ndn = "("+str(Nd)+"*2.71828^(-"+str(a)+"*0.5*(MCantitoppt+MCtoppt)))"
# NT-est vars (and errors)

p0 = "0.402504"
p1 = "0.000641416"
p2 = "0.124863"
p3 = "0.00452712"
p4 = "0.00024813"

p0 = "0.691861"
p1 = "0.0096715"
p2 = "0.16024"
p3 = "0.00593041"
p4 = "0.000622613"

ntW = "(" + p0 + " + " + p1 + " * (hadWcandmass - 80.))"

ntWu = "(" + p0 + " + " + p1 + " * (hadWcandmass - 80.) + sqrt((hadWcandmass - 80.) * (hadWcandmass - 80.) * " + p3 + " * " + p3 + " + (hadWcandmass - 80.) * 2 * " + p4 + " + " + p2 + " * " + p2 + "))"
ntWd = "(" + p0 + " + " + p1 + " * (hadWcandmass - 80.) - sqrt((hadWcandmass - 80.) * (hadWcandmass - 80.) * " + p3 + " * " + p3 + " + (hadWcandmass - 80.) * 2 * " + p4 + " + " + p2 + " * " + p2 + "))"


# Theser are all the data driven uncrt, we'll have to load in separate Ntuples for most of the MC systematics.

### Set Up the Histograms:
# Not Saved: These don't play a part in limit setting, and are thus going to be discarded
msZPs = TH1F("msZPs", "", 30, 500, 3500)
esZPs = TH1F("esZPs", "", 30, 500, 3500)

msZPsU = TH1F("msZPsU", "", 30, 500, 3500) # sub up
esZPsU = TH1F("esZPsU", "", 30, 500, 3500)

msZPsD = TH1F("msZPsD", "", 30, 500, 3500) # sub down
esZPsD = TH1F("esZPsD", "", 30, 500, 3500)

mtZPs = TH1F("mtZPs", "", 30, 500, 3500) # Central Value
etZPs = TH1F("etZPs", "", 30, 500, 3500)

mtZPsU = TH1F("mtZPsU", "", 30, 500, 3500) # sub up
etZPsU = TH1F("etZPsU", "", 30, 500, 3500)

mtZPsD = TH1F("mtZPsD", "", 30, 500, 3500) # sub down
etZPsD = TH1F("etZPsD", "", 30, 500, 3500)

mtZPs_Nup = TH1F("mtZPs_Nup", "", 30, 500, 3500) # N up
etZPs_Nup = TH1F("etZPs_Nup", "", 30, 500, 3500)

mtZPs_Ndn = TH1F("mtZPs_Ndn", "", 30, 500, 3500) # N down
etZPs_Ndn = TH1F("etZPs_Ndn", "", 30, 500, 3500)

mtZPs_aup = TH1F("mtZPs_aup", "", 30, 500, 3500) # a up
etZPs_aup = TH1F("etZPs_aup", "", 30, 500, 3500)

mtZPs_adn = TH1F("mtZPs_adn", "", 30, 500, 3500) # a down
etZPs_adn = TH1F("etZPs_adn", "", 30, 500, 3500)

# Create save file:
fout = TFile("Zprime_Theta_Feed.root", "RECREATE") # Careful, unlike older versions of the code, this will overwrite old files.
fout.cd()
# Saved: Histograms created here will be saved to file.
# data:
mZPd = TH1F("MU__DATA", "", 30, 500, 3500)
eZPd = TH1F("EL__DATA", "", 30, 500, 3500)
# Central Value BKG:
mZPs = TH1F("MU__ST", "", 30, 500, 3500)
eZPs = TH1F("EL__ST", "", 30, 500, 3500)
mZPt = TH1F("MU__TT", "", 30, 500, 3500)
eZPt = TH1F("EL__TT", "", 30, 500, 3500)
mZPn = TH1F("MU__NT", "", 30, 500, 3500)
eZPn = TH1F("EL__NT", "", 30, 500, 3500)
# Errors from non-top:
mZPnU = TH1F("MU__NT__linfiterr__up", "", 30, 500, 3500)
eZPnU = TH1F("EL__NT__linfiterr__up", "", 30, 500, 3500)
mZPnD = TH1F("MU__NT__linfiterr__down", "", 30, 500, 3500)
eZPnD = TH1F("EL__NT__linfiterr__down", "", 30, 500, 3500)
# Errors from ttbar:
mZPt_aup = TH1F("MU__TT__a__up", "", 30, 500, 3500)
eZPt_aup = TH1F("EL__TT__a__up", "", 30, 500, 3500)
mZPn_aup = TH1F("MU__NT__a__up", "", 30, 500, 3500)
eZPn_aup = TH1F("EL__NT__a__up", "", 30, 500, 3500)
mZPt_adn = TH1F("MU__TT__a__down", "", 30, 500, 3500)
eZPt_adn = TH1F("EL__TT__a__down", "", 30, 500, 3500)
mZPn_adn = TH1F("MU__NT__a__down", "", 30, 500, 3500)
eZPn_adn = TH1F("EL__NT__a__down", "", 30, 500, 3500)
mZPt_Nup = TH1F("MU__TT__N__up", "", 30, 500, 3500)
eZPt_Nup = TH1F("EL__TT__N__up", "", 30, 500, 3500)
mZPn_Nup = TH1F("MU__NT__N__up", "", 30, 500, 3500)
eZPn_Nup = TH1F("EL__NT__N__up", "", 30, 500, 3500)
mZPt_Ndn = TH1F("MU__TT__N__down", "", 30, 500, 3500)
eZPt_Ndn = TH1F("EL__TT__N__down", "", 30, 500, 3500)
mZPn_Ndn = TH1F("MU__NT__N__down", "", 30, 500, 3500)
eZPn_Ndn = TH1F("EL__NT__N__down", "", 30, 500, 3500)
# Errors from MC:
# Now we fill them:

#cuts

# ???
Fulltag = "(leptopcandmass > 140 && leptopcandmass < 250 && hadWcandtau21<0.5 && (lep2Drel>25.||lep2Ddr>0.5) && hadtopcandmass > 250. && (hadWcandmass > 50 && hadWcandmass < 120 && hadWcandpt > 200) && cuts[2] > 0 && numjets > 2 && leppt > 25)"
Antitag = "(leptopcandmass > 140 && leptopcandmass < 250 && hadWcandtau21>0.5 && (lep2Drel>25.||lep2Ddr>0.5) && hadtopcandmass > 250. && (hadWcandmass > 50 && hadWcandmass < 120 && hadWcandpt > 200) && cuts[2] > 0 && numjets > 2 && leppt > 25)"

# Subtractions:
# ttbar:
for i in range(len(tFileName)):
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPs, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntW+"*"+TW+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPs_aup, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntW+"*"+TW_aup+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPs_adn, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntW+"*"+TW_adn+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPs_Nup, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntW+"*"+TW_Nup+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPs_Ndn, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntW+"*"+TW_Ndn+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPsU, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntWu+"*"+TW+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mtZPsD, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntWd+"*"+TW+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPs, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntW+"*"+TW+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPs_aup, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntW+"*"+TW_aup+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPs_adn, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntW+"*"+TW_adn+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPs_Nup, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntW+"*"+TW_Nup+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPs_Ndn, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntW+"*"+TW_Ndn+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPsU, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntWu+"*"+TW+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], etZPsD, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntWd+"*"+TW+")")
# single top
for i in range(len(sFileName)):
	writeplot(sFilePrefix+sFileName[i], lumi*sxs[i]/sn[i], msZPs, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntW+")")
	writeplot(sFilePrefix+sFileName[i], lumi*sxs[i]/sn[i], msZPsU, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntWu+")")
	writeplot(sFilePrefix+sFileName[i], lumi*sxs[i]/sn[i], msZPsD, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntWd+")")
	writeplot(sFilePrefix+sFileName[i], lumi*sxs[i]/sn[i], esZPs, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntW+")")
	writeplot(sFilePrefix+sFileName[i], lumi*sxs[i]/sn[i], esZPsU, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntWu+")")
	writeplot(sFilePrefix+sFileName[i], lumi*sxs[i]/sn[i], esZPsD, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntWd+")")
# DATA:
writeplot(dFileNameM, 1.0, mZPd, "EventMass", "("+Fulltag+"&cuts[3]>0.)", "(1.0)")
writeplot(dFileNameE, 1.0, eZPd, "EventMass", "("+Fulltag+"&cuts[0]>0.)", "(1.0)")
# NONTOP EST:
writeplot(dFileNameM, 1.0, mZPn, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntW+")")
writeplot(dFileNameE, 1.0, eZPn, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntW+")")
writeplot(dFileNameM, 1.0, mZPn_aup, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntW+")")
writeplot(dFileNameE, 1.0, eZPn_aup, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntW+")")
writeplot(dFileNameM, 1.0, mZPn_adn, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntW+")")
writeplot(dFileNameE, 1.0, eZPn_adn, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntW+")")
writeplot(dFileNameM, 1.0, mZPn_Nup, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntW+")")
writeplot(dFileNameE, 1.0, eZPn_Nup, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntW+")")
writeplot(dFileNameM, 1.0, mZPn_Ndn, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntW+")")
writeplot(dFileNameE, 1.0, eZPn_Ndn, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntW+")")
writeplot(dFileNameM, 1.0, mZPnU, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntWu+")")
writeplot(dFileNameE, 1.0, eZPnU, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntWu+")")
writeplot(dFileNameM, 1.0, mZPnD, "EventMass", "("+Antitag+"&cuts[3]>0.)", "("+ntWd+")")
writeplot(dFileNameE, 1.0, eZPnD, "EventMass", "("+Antitag+"&cuts[0]>0.)", "("+ntWd+")")
# TTBAR:
for i in range(len(tFileName)):
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mZPt, "EventMass", "("+Fulltag+"&cuts[3]>0.)", "("+TW+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mZPt_aup, "EventMass", "("+Fulltag+"&cuts[3]>0.)", "("+TW_aup+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mZPt_adn, "EventMass", "("+Fulltag+"&cuts[3]>0.)", "("+TW_adn+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mZPt_Nup, "EventMass", "("+Fulltag+"&cuts[3]>0.)", "("+TW_Nup+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], mZPt_Ndn, "EventMass", "("+Fulltag+"&cuts[3]>0.)", "("+TW_Ndn+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], eZPt, "EventMass", "("+Fulltag+"&cuts[0]>0.)", "("+TW+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], eZPt_aup, "EventMass", "("+Fulltag+"&cuts[0]>0.)", "("+TW_aup+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], eZPt_adn, "EventMass", "("+Fulltag+"&cuts[0]>0.)", "("+TW_adn+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], eZPt_Nup, "EventMass", "("+Fulltag+"&cuts[0]>0.)", "("+TW_Nup+")")
	writeplot(tFilePrefix+tFileName[i], lumi*txs[i]/tn[i], eZPt_Ndn, "EventMass", "("+Fulltag+"&cuts[0]>0.)", "("+TW_Ndn+")")
# SINGLE TOP:
for i in range(len(sFileName)):
	writeplot(sFilePrefix+sFileName[i], lumi*sxs[i]/sn[i], mZPs, "EventMass", "("+Fulltag+"&cuts[3]>0.)", "(1.0)")
	writeplot(sFilePrefix+sFileName[i], lumi*sxs[i]/sn[i], eZPs, "EventMass", "("+Fulltag+"&cuts[0]>0.)", "(1.0)")
	# error files:
# Do the substractions as needed:
mZPn.Add(msZPs,-1)
eZPn.Add(esZPs,-1)
mZPn.Add(mtZPs,-1)
eZPn.Add(etZPs,-1)
# Nup:
mZPn_Nup.Add(msZPs,-1)
eZPn_Nup.Add(esZPs,-1)
mZPn_Nup.Add(mtZPs_Nup,-1)
eZPn_Nup.Add(etZPs_Nup,-1)
# Ndn
mZPn_Ndn.Add(msZPs,-1)
eZPn_Ndn.Add(esZPs,-1)
mZPn_Ndn.Add(mtZPs_Ndn,-1)
eZPn_Ndn.Add(etZPs_Ndn,-1)
# aup:
mZPn_aup.Add(msZPs,-1)
eZPn_aup.Add(esZPs,-1)
mZPn_aup.Add(mtZPs_aup,-1)
eZPn_aup.Add(etZPs_aup,-1)
# adn:
mZPn_adn.Add(msZPs,-1)
eZPn_adn.Add(esZPs,-1)
mZPn_adn.Add(mtZPs_adn,-1)
eZPn_adn.Add(etZPs_adn,-1)
# fit U
mZPnU.Add(msZPsU,-1)
eZPnU.Add(esZPsU,-1)
mZPnU.Add(mtZPsU,-1)
eZPnU.Add(etZPsU,-1)
# fit D
mZPnD.Add(msZPsD,-1)
eZPnD.Add(esZPsD,-1)
mZPnD.Add(mtZPsD,-1)
eZPnD.Add(etZPsD,-1)
# save file! now you're done!
fout.Write()
fout.Save()
fout.Close()
