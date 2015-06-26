.PHONY: all plugins

TREEMAKER_CONDOR=cd working && treemaker-condor -fr

all:	clean plugins config mc
run:	data mc
mc:		singletop ttbar qcd gstar wjets

clean:
	rm -rf working/
	rm -rf configs/*

plugins:
	cp -rv plugins/* ${CMSSW_BASE}/src/Treemaker/Treemaker/python/plugins/

config:
	# TTbar	
	treemaker-config --split-by 10 -t tree -p zprime.list -f /eos/uscms/store/user/eminizer/TTJets_FullLeptMGDecays_8TeV-madgraph/
	treemaker-config --split-by 10 -t tree -p zprime.list -f /eos/uscms/store/user/eminizer/TTJets_SemiLeptMGDecays_8TeV-madgraph/

	# Singletop
	treemaker-config --split-by 2 -t tree -p zprime_qcd.list --param weight=1.4579109943414589e-05 -f /eos/uscms/store/user/eminizer/T_s-channel_TuneZ2star_8TeV-powheg-tauola/
	treemaker-config --split-by 5 -t tree -p zprime_qcd.list --param weight=1.5007076475157035e-05 -f /eos/uscms/store/user/eminizer/T_t-channel_TuneZ2star_8TeV-powheg-tauola/
	treemaker-config --split-by 2 -t tree -p zprime_qcd.list --param weight=2.2338634162416761e-05 -f /eos/uscms/store/user/eminizer/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/
	treemaker-config -t tree -p zprime_qcd.list --param weight=1.2630917170331634e-05 -f /eos/uscms/store/user/eminizer/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/
	treemaker-config --split-by 2 -t tree -p zprime_qcd.list --param weight=1.5865042747763389e-05 -f /eos/uscms/store/user/eminizer/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/
	treemaker-config --split-by 2 -t tree -p zprime_qcd.list --param weight=2.2528675069914484e-05 -f /eos/uscms/store/user/eminizer/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/

	# Data
	treemaker-config -t tree -p zprime.list -d --split-into 25 /eos/uscms/store/user/osherson/SingleMu/
	treemaker-config -t tree -p zprime.list -d --split-into 25 /eos/uscms/store/user/osherson/SingleElectron/

	# Gstar
	treemaker-config -t tree -p zprime.list -n Gstar_Semilep_1500GeV /eos/uscms/store/user/bjr/ntuples/gstar/Gstar_Semilep_1500GeV/normal -o Gstar_Semilep_1500GeV --split-by 5
	treemaker-config -t tree -p zprime.list -n Gstar_Semilep_2000GeV /eos/uscms/store/user/bjr/ntuples/gstar/Gstar_Semilep_2000GeV/normal -o Gstar_Semilep_2000GeV --split-by 5
	treemaker-config -t tree -p zprime.list -n Gstar_Semilep_3000GeV /eos/uscms/store/user/bjr/ntuples/gstar/Gstar_Semilep_3000GeV/normal -o Gstar_Semilep_3000GeV --split-by 5

	# WJets
	treemaker-config --split-by 15 -t tree -p zprime.list /eos/uscms/store/user/bjr/ntuples/wjets/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball

	# QCD (weights were calculated to stupid orders of magnitude, I apologize).
	treemaker-config --split-by 10 -t tree -p zprime_qcd.list --param weight=0.0056896916667 /eos/uscms/store/user/asady1/QCD_170-300_v1/
	treemaker-config --split-by 5 -t tree -p zprime_qcd.list --param weight=0.0002932581667 /eos/uscms/store/user/asady1/QCD_300-470_v1/
	treemaker-config --split-by 5 -t tree -p zprime_qcd.list --param weight=2.8469774999999e-05 /eos/uscms/store/user/asady1/QCD_470-600_v1/
	treemaker-config --split-by 5 -t tree -p zprime_qcd.list --param weight=6.748025e-06 /eos/uscms/store/user/asady1/QCD_600-800_v1/
	treemaker-config --split-by 5 -t tree -p zprime_qcd.list --param weight=8.87509e-07 /eos/uscms/store/user/asady1/QCD_800-1000_v1/
	treemaker-config --split-by 5 -t tree -p zprime_qcd.list --param weight=3.68922e-07 /eos/uscms/store/user/asady1/QCD_1000-1400_v1/
	treemaker-config --split-by 5 -t tree -p zprime_qcd.list --param weight=1.6761175e-08 /eos/uscms/store/user/asady1/QCD_1400-1800_v1/
	treemaker-config --split-by 5 -t tree -p zprime_qcd.list --param weight=1.829005e-09 /eos/uscms/store/user/asady1/QCD_1800_v1/

	# QCD (weights were calculated to stupid orders of magnitude, I apologize).
	treemaker-config --split-by 5 -t tree -p zprime_qcd.list --param weight=0.0056896916667 /eos/uscms/store/user/asady1/QCD_170-300_v1/
	treemaker-config --split-by 5 -t tree -p zprime_qcd.list --param weight=0.0002932581667 /eos/uscms/store/user/asady1/QCD_300-470_v1/
	treemaker-config --split-by 5 -t tree -p zprime_qcd.list --param weight=2.8469774999999e-05 /eos/uscms/store/user/asady1/QCD_470-600_v1/
	treemaker-config --split-by 5 -t tree -p zprime_qcd.list --param weight=6.748025e-06 /eos/uscms/store/user/asady1/QCD_600-800_v1/
	treemaker-config --split-by 5 -t tree -p zprime_qcd.list --param weight=8.87509e-07 /eos/uscms/store/user/asady1/QCD_800-1000_v1/
	treemaker-config --split-by 5 -t tree -p zprime_qcd.list --param weight=3.68922e-07 /eos/uscms/store/user/asady1/QCD_1000-1400_v1/
	treemaker-config --split-by 5 -t tree -p zprime_qcd.list --param weight=1.6761175e-08 /eos/uscms/store/user/asady1/QCD_1400-1800_v1/
	treemaker-config --split-by 5 -t tree -p zprime_qcd.list --param weight=1.829005e-09 /eos/uscms/store/user/asady1/QCD_1800_v1/

	mv *.cfg configs/

singletop:
	mkdir -p working
	$(TREEMAKER_CONDOR) ../configs/T_s-channel_TuneZ2star_8TeV-powheg-tauola.cfg
	$(TREEMAKER_CONDOR) ../configs/T_t-channel_TuneZ2star_8TeV-powheg-tauola.cfg
	$(TREEMAKER_CONDOR) ../configs/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola.cfg
	$(TREEMAKER_CONDOR) ../configs/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola.cfg
	$(TREEMAKER_CONDOR) ../configs/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola.cfg
	$(TREEMAKER_CONDOR) ../configs/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola.cfg

ttbar:
	mkdir -p working
	$(TREEMAKER_CONDOR) ../configs/TTJets_FullLeptMGDecays_8TeV-madgraph.cfg
	$(TREEMAKER_CONDOR) ../configs/TTJets_SemiLeptMGDecays_8TeV-madgraph.cfg

data:
	mkdir -p working
	$(TREEMAKER_CONDOR) ../configs/SingleMu.cfg
	$(TREEMAKER_CONDOR) ../configs/SingleElectron.cfg

gstar:
	mkdir -p working
	$(TREEMAKER_CONDOR) ../configs/Gstar_Semilep_1500GeV.cfg
	$(TREEMAKER_CONDOR) ../configs/Gstar_Semilep_2000GeV.cfg
	$(TREEMAKER_CONDOR) ../configs/Gstar_Semilep_3000GeV.cfg

wjets:
	mkdir -p working
	$(TREEMAKER_CONDOR) ../configs/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball.cfg

qcd:
	mkdir -p working
	$(TREEMAKER_CONDOR) ../configs/QCD_170-300_v1.cfg
	$(TREEMAKER_CONDOR) ../configs/QCD_300-470_v1.cfg
	$(TREEMAKER_CONDOR) ../configs/QCD_470-600_v1.cfg
	$(TREEMAKER_CONDOR) ../configs/QCD_600-800_v1.cfg
	$(TREEMAKER_CONDOR) ../configs/QCD_800-1000_v1.cfg
	$(TREEMAKER_CONDOR) ../configs/QCD_1000-1400_v1.cfg
	$(TREEMAKER_CONDOR) ../configs/QCD_1400-1800_v1.cfg
	$(TREEMAKER_CONDOR) ../configs/QCD_1800_v1.cfg
