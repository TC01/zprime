import ROOT
from ROOT import *
from CutOnTree import writeplot


####
## Code that assembles all (I do mean all) relevant histograms for output to theta. DOES NOT ADD SIGNAL. SIGNAL POINTS ARE PROCESSED SEPARATELY AND -M-U-S-T- BE PROCESSED SECOND.
####

# Defs:
lumi = 19748.

# Define files:
# single top
sFileName = ['t','s','tW','_t','_s','_tW']
sxs = [56.4,3.79,11.117,30.7,1.768,11.117]
sn = [3758227, 259961, 497658, 1935072, 139974, 493460]
sFilePrefix = '/home/osherson/Work/Trees/Gstar/T'
# data
dFileNameE = "/home/osherson/Work/Trees/Gstar/SingleElectron.root"
dFileNameM = "/home/osherson/Work/Trees/Gstar/SingleMu.root"
# ttbar
tFileName = ["tt", "ttl_uncut"]
txs = [107.7,25.17]
tn = [25424818,12043695]
tFilePrefix = "/home/osherson/Work/Trees/Gstar/"


# TT-rw vars (and errors)
N = 0.96
a = 0.0012

Nu = N + 0.1
au = a - 0.00023 # no this isn't a type, recall that alpha is a negative factor but the value being listed here is positive, so a smaller alpha is closer to positve

Nd = N - 0.1
ad = a + 0.00023 # no this isn't a type, recall that alpha is a negative factor but the value being listed here is positive, so a smaller alpha is closer to positve

TW = "("+str(N)+"*2.71828^(-"+str(a)+"*0.5*(MCantitoppt+MCtoppt)))"
TW_aup = "("+str(N)+"*2.71828^(-"+str(au)+"*0.5*(MCantitoppt+MCtoppt)))"
TW_adn = "("+str(N)+"*2.71828^(-"+str(ad)+"*0.5*(MCantitoppt+MCtoppt)))"
TW_Nup = "("+str(Nu)+"*2.71828^(-"+str(a)+"*0.5*(MCantitoppt+MCtoppt)))"
TW_Ndn = "("+str(Nd)+"*2.71828^(-"+str(a)+"*0.5*(MCantitoppt+MCtoppt)))"
# NT-est vars (and errors)
ntW = "(0.072885 + 0.000660127*(topcandmass-170.))"
ntWu = "(((0.072885 + 0.000660127*(topcandmass-170.)) + ((topcandmass-170.)*(topcandmass-170.)*(0.000633024*0.000633024)+((topcandmass-170.)*2*0.0000193051+(0.0348167*0.0348167)))^0.5))"
ntWd = "(((0.072885 + 0.000660127*(topcandmass-170.)) - ((topcandmass-170.)*(topcandmass-170.)*(0.000633024*0.000633024)+((topcandmass-170.)*2*0.0000193051+(0.0348167*0.0348167)))^0.5))"

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
Fulltag = "(topcandtau2/topcandtau1>0.1&(lepcut2Drel>25.||lepcut2Ddr>0.5)&heavytopcandmass>800.)&(topcandtau3/topcandtau2<0.55&topcandmass<250&topcandmass>140)&isLoose>0."
Antitag = "(topcandtau2/topcandtau1>0.1&(lepcut2Drel>25.||lepcut2Ddr>0.5)&heavytopcandmass>800.)&(topcandtau3/topcandtau2>0.55&topcandmass<250&topcandmass>140)&isLoose>0."
# Subtractions:
# ttbar:
for i in range(len(tFileName)):
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], mtZPs, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntW+"*"+TW+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], mtZPs_aup, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntW+"*"+TW_aup+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], mtZPs_adn, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntW+"*"+TW_adn+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], mtZPs_Nup, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntW+"*"+TW_Nup+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], mtZPs_Ndn, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntW+"*"+TW_Ndn+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], mtZPsU, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntWu+"*"+TW+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], mtZPsD, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntWd+"*"+TW+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], etZPs, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntW+"*"+TW+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], etZPs_aup, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntW+"*"+TW_aup+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], etZPs_adn, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntW+"*"+TW_adn+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], etZPs_Nup, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntW+"*"+TW_Nup+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], etZPs_Ndn, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntW+"*"+TW_Ndn+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], etZPsU, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntWu+"*"+TW+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], etZPsD, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntWd+"*"+TW+")")
# single top
for i in range(len(sFileName)):
	writeplot(sFilePrefix+sFileName[i]+'.root', lumi*sxs[i]/sn[i], msZPs, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntW+")")
	writeplot(sFilePrefix+sFileName[i]+'.root', lumi*sxs[i]/sn[i], msZPsU, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntWu+")")
	writeplot(sFilePrefix+sFileName[i]+'.root', lumi*sxs[i]/sn[i], msZPsD, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntWd+")")
	writeplot(sFilePrefix+sFileName[i]+'.root', lumi*sxs[i]/sn[i], esZPs, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntW+")")
	writeplot(sFilePrefix+sFileName[i]+'.root', lumi*sxs[i]/sn[i], esZPsU, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntWu+")")
	writeplot(sFilePrefix+sFileName[i]+'.root', lumi*sxs[i]/sn[i], esZPsD, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntWd+")")
# DATA:
writeplot(dFileNameM, 1.0, mZPd, "EventMass", "("+Fulltag+"&isMuon>0.)", "(1.0)")
writeplot(dFileNameE, 1.0, eZPd, "EventMass", "("+Fulltag+"&isElec>0.)", "(1.0)")
# NONTOP EST:
writeplot(dFileNameM, 1.0, mZPn, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntW+")")
writeplot(dFileNameE, 1.0, eZPn, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntW+")")
writeplot(dFileNameM, 1.0, mZPn_aup, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntW+")")
writeplot(dFileNameE, 1.0, eZPn_aup, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntW+")")
writeplot(dFileNameM, 1.0, mZPn_adn, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntW+")")
writeplot(dFileNameE, 1.0, eZPn_adn, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntW+")")
writeplot(dFileNameM, 1.0, mZPn_Nup, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntW+")")
writeplot(dFileNameE, 1.0, eZPn_Nup, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntW+")")
writeplot(dFileNameM, 1.0, mZPn_Ndn, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntW+")")
writeplot(dFileNameE, 1.0, eZPn_Ndn, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntW+")")
writeplot(dFileNameM, 1.0, mZPnU, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntWu+")")
writeplot(dFileNameE, 1.0, eZPnU, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntWu+")")
writeplot(dFileNameM, 1.0, mZPnD, "EventMass", "("+Antitag+"&isMuon>0.)", "("+ntWd+")")
writeplot(dFileNameE, 1.0, eZPnD, "EventMass", "("+Antitag+"&isElec>0.)", "("+ntWd+")")
# TTBAR:
for i in range(len(tFileName)):
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], mZPt, "EventMass", "("+Fulltag+"&isMuon>0.)", "("+TW+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], mZPt_aup, "EventMass", "("+Fulltag+"&isMuon>0.)", "("+TW_aup+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], mZPt_adn, "EventMass", "("+Fulltag+"&isMuon>0.)", "("+TW_adn+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], mZPt_Nup, "EventMass", "("+Fulltag+"&isMuon>0.)", "("+TW_Nup+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], mZPt_Ndn, "EventMass", "("+Fulltag+"&isMuon>0.)", "("+TW_Ndn+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], eZPt, "EventMass", "("+Fulltag+"&isElec>0.)", "("+TW+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], eZPt_aup, "EventMass", "("+Fulltag+"&isElec>0.)", "("+TW_aup+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], eZPt_adn, "EventMass", "("+Fulltag+"&isElec>0.)", "("+TW_adn+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], eZPt_Nup, "EventMass", "("+Fulltag+"&isElec>0.)", "("+TW_Nup+")")
	writeplot(tFilePrefix+tFileName[i]+'.root', lumi*txs[i]/tn[i], eZPt_Ndn, "EventMass", "("+Fulltag+"&isElec>0.)", "("+TW_Ndn+")")
# SINGLE TOP:
for i in range(len(sFileName)):
	writeplot(sFilePrefix+sFileName[i]+'.root', lumi*sxs[i]/sn[i], mZPs, "EventMass", "("+Fulltag+"&isMuon>0.)", "(1.0)")
	writeplot(sFilePrefix+sFileName[i]+'.root', lumi*sxs[i]/sn[i], eZPs, "EventMass", "("+Fulltag+"&isElec>0.)", "(1.0)")
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
