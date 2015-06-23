.PHONY: all plugins

all:	plugins config run
run:	singletop ttbar data

plugins:
	cp -rv plugins/* ${CMSSW_BASE}/src/Treemaker/Treemaker/python/plugins/

config:
	# TTbar	
	treemaker-config --split-by 5 -t tree -p zprime.list -f /eos/uscms/store/user/eminizer/TTJets_FullLeptMGDecays_8TeV-madgraph/
	treemaker-config --split-by 5 -t tree -p zprime.list -f /eos/uscms/store/user/eminizer/TTJets_SemiLeptMGDecays_8TeV-madgraph/

	# Singletop
	treemaker-config -t tree -p zprime.list -f /eos/uscms/store/user/eminizer/T_s-channel_TuneZ2star_8TeV-powheg-tauola/
	treemaker-config -t tree -p zprime.list -f /eos/uscms/store/user/eminizer/T_t-channel_TuneZ2star_8TeV-powheg-tauola/
	treemaker-config -t tree -p zprime.list -f /eos/uscms/store/user/eminizer/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/
	treemaker-config -t tree -p zprime.list -f /eos/uscms/store/user/eminizer/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/
	treemaker-config -t tree -p zprime.list -f /eos/uscms/store/user/eminizer/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/
	treemaker-config -t tree -p zprime.list -f /eos/uscms/store/user/eminizer/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/

	# Data
	treemaker-config -t tree -p zprime.list -d --split-into 50 /eos/uscms/store/user/osherson/SingleMu/
	treemaker-config -t tree -p zprime.list -d --split-into 50 /eos/uscms/store/user/osherson/SingleElectron/

	# Gstar
	treemaker-config -t tree -p zprime.list /eos/uscms/store/user/bjr/ntuples/gstar/Gstar_Semilep_1500GeV_WMLM
	treemaker-config -t tree -p zprime.list /eos/uscms/store/user/bjr/ntuples/gstar/Gstar_Semilep_1500GeV_WMLP  
	treemaker-config -t tree -p zprime.list /eos/uscms/store/user/bjr/ntuples/gstar/Gstar_Semilep_1500GeV_WPLM  
	treemaker-config -t tree -p zprime.list /eos/uscms/store/user/bjr/ntuples/gstar/Gstar_Semilep_1500GeV_WPLP  
	treemaker-config -t tree -p zprime.list /eos/uscms/store/user/bjr/ntuples/gstar/Gstar_Semilep_2000GeV_WMLM
	treemaker-config -t tree -p zprime.list /eos/uscms/store/user/bjr/ntuples/gstar/Gstar_Semilep_2000GeV_WMLP  
	treemaker-config -t tree -p zprime.list /eos/uscms/store/user/bjr/ntuples/gstar/Gstar_Semilep_2000GeV_WPLM  
	treemaker-config -t tree -p zprime.list /eos/uscms/store/user/bjr/ntuples/gstar/Gstar_Semilep_2000GeV_WPLP  
	treemaker-config -t tree -p zprime.list /eos/uscms/store/user/bjr/ntuples/gstar/Gstar_Semilep_3000GeV_WMLM
	treemaker-config -t tree -p zprime.list /eos/uscms/store/user/bjr/ntuples/gstar/Gstar_Semilep_3000GeV_WMLP  
	treemaker-config -t tree -p zprime.list /eos/uscms/store/user/bjr/ntuples/gstar/Gstar_Semilep_3000GeV_WPLM  
	treemaker-config -t tree -p zprime.list /eos/uscms/store/user/bjr/ntuples/gstar/Gstar_Semilep_3000GeV_WPLP  

	# WJets
	treemaker-config --split-by 10 -t tree -p zprime.list /eos/uscms/store/user/eminizer/WJetsToLNu_13TeV-madgraph-pythia8-tauola/

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
	treemaker-condor -fr configs/T_s-channel_TuneZ2star_8TeV-powheg-tauola.cfg
	treemaker-condor -fr configs/T_t-channel_TuneZ2star_8TeV-powheg-tauola.cfg
	treemaker-condor -fr configs/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola.cfg
	treemaker-condor -fr configs/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola.cfg
	treemaker-condor -fr configs/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola.cfg
	treemaker-condor -fr configs/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola.cfg

ttbar:
	treemaker-condor -fr configs/TTJets_FullLeptMGDecays_8TeV-madgraph.cfg
	treemaker-condor -fr configs/TTJets_SemiLeptMGDecays_8TeV-madgraph.cfg

data:
	treemaker-condor -fr configs/SingleMu.cfg
	treemaker-condor -fr configs/SingleElectron.cfg

gstar:
	treemaker-condor -fr configs/Gstar_Semilep_1500GeV_WMLM.cfg
	treemaker-condor -fr configs/Gstar_Semilep_1500GeV_WMLP.cfg
	treemaker-condor -fr configs/Gstar_Semilep_1500GeV_WPLM.cfg
	treemaker-condor -fr configs/Gstar_Semilep_1500GeV_WPLP.cfg
	treemaker-condor -fr configs/Gstar_Semilep_2000GeV_WMLM.cfg
	treemaker-condor -fr configs/Gstar_Semilep_2000GeV_WMLP.cfg
	treemaker-condor -fr configs/Gstar_Semilep_2000GeV_WPLM.cfg
	treemaker-condor -fr configs/Gstar_Semilep_2000GeV_WPLP.cfg
	treemaker-condor -fr configs/Gstar_Semilep_3000GeV_WMLM.cfg
	treemaker-condor -fr configs/Gstar_Semilep_3000GeV_WMLP.cfg
	treemaker-condor -fr configs/Gstar_Semilep_3000GeV_WPLM.cfg
	treemaker-condor -fr configs/Gstar_Semilep_3000GeV_WPLP.cfg

wjets:
	treemaker-condor -fr configs/WJetsToLNu_13TeV-madgraph-pythia8-tauola.cfg

qcd:
	treemaker-condor -fr configs/QCD_170-300_v1.cfg
	treemaker-condor -fr configs/QCD_300-470_v1.cfg
	treemaker-condor -fr configs/QCD_470-600_v1.cfg
	treemaker-condor -fr configs/QCD_600-800_v1.cfg
	treemaker-condor -fr configs/QCD_800-1000_v1.cfg
	treemaker-condor -fr configs/QCD_1000-1400_v1.cfg
	treemaker-condor -fr configs/QCD_1400-1800_v1.cfg
	treemaker-condor -fr configs/QCD_1800_v1.cfg
