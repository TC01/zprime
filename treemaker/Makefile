.PHONY: all plugins

all:	plugins

plugins:
	cp -rv plugins/* ${CMSSW_BASE}/src/Treemaker/Treemaker/python/plugins/

config:
	# This is the template command to 'make' a config file (note that the exact directory should change once I fix treemaker).
	# Add -d for the data ntuples.
	treemaker-config -t tree -p zprime.list -f /eos/uscms/store/user/eminizer/TT_Mtt-1000toInf_CT10_TuneZ2star_8TeV-powheg-tauola/
	mv *.cfg configs/
