.PHONY: all plugins

all:	plugins

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

	mv *.cfg configs/
