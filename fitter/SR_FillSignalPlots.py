import ROOT
from ROOT import *
from CutOnTree import writeplot
lumi = 19748.
# Load signals:
# 1500:
z15FileName = "/eos/uscms/store/user/bjr/trees/pruned/Gstar_Semilep_1500GeV.root"
z15xs = .1
z15n = 160000/3
# 2000:
z2FileName = "/eos/uscms/store/user/bjr/trees/pruned/Gstar_Semilep_2000GeV.root"
z2xs = .1
z2n = 160000/3
# 3000:
z3FileName = "/eos/uscms/store/user/bjr/trees/pruned/Gstar_Semilep_3000GeV.root"
z3xs = .1
z3n = 160000/3

#cuts
Fulltag = "(hadWcandtau21<0.5 && (lep2Drel>25.||lep2Ddr>0.5) && hadtopcandmass > 250. && (hadWcandmass > 50 && hadWcandmass < 120 && hadWcandpt > 200) && cuts[2] > 0 && numjets > 2 && leppt > 25)"

fout = TFile("Zprime_Theta_Feed.root", "UPDATE") #
fout.cd()

# Plots:

mZP15 = TH1F("MU__zp1500", "", 30, 500, 3500)
eZP15 = TH1F("EL__zp1500", "", 30, 500, 3500)

mZP2 = TH1F("MU__zp2000", "", 30, 500, 3500)
eZP2 = TH1F("EL__zp2000", "", 30, 500, 3500)

mZP3 = TH1F("MU__zp3000", "", 30, 500, 3500)
eZP3 = TH1F("EL__zp3000", "", 30, 500, 3500)

# Fill Plots:
writeplot(z15FileName, lumi*z15xs/z15n, mZP15, "EventMass", "("+Fulltag+"&cuts[3]>0.&isGTt>0.)", "(1.0)")
writeplot(z15FileName, lumi*z15xs/z15n, eZP15, "EventMass", "("+Fulltag+"&cuts[0]>0.&isGTt>0.)", "(1.0)")

writeplot(z2FileName, lumi*z2xs/z2n, mZP2, "EventMass", "("+Fulltag+"&cuts[3]>0.&isGTt>0.)", "(1.0)")
writeplot(z2FileName, lumi*z2xs/z2n, eZP2, "EventMass", "("+Fulltag+"&cuts[0]>0.&isGTt>0.)", "(1.0)")

writeplot(z3FileName, lumi*z3xs/z3n, mZP3, "EventMass", "("+Fulltag+"&cuts[3]>0.&isGTt>0.)", "(1.0)")
writeplot(z3FileName, lumi*z3xs/z3n, eZP3, "EventMass", "("+Fulltag+"&cuts[0]>0.&isGTt>0.)", "(1.0)")

fout.Write()
fout.Save()
fout.Close()
