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
