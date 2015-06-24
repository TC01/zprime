BASEDIR=${CURDIR}
ANALYSISDIR=${CURDIR}/working/
TREES=/srv/data

all: clean prepare semilep

semilep:
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/preselection.conf -p ${ANALYSISDIR}/preselection -t ${TREES} --no-wait
#	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/electron.conf -p ${ANALYSISDIR}/preselection/electrons --no-wait
#	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/muon.conf -p ${ANALYSISDIR}/preselection/muons --no-wait

# LEGACY

tagger:
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/preselection.conf -p ${ANALYSISDIR}/preselection -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/top_cut.conf -p ${ANALYSISDIR}/preselection/top_cut -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/top_cut.conf -p ${ANALYSISDIR}/top_cut -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/top_cut_jet1.conf -p ${ANALYSISDIR}/preselection/top_cut_jet1 -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/top_cut_jet2.conf -p ${ANALYSISDIR}/preselection/top_cut_jet2 -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/top_cut_jet3.conf -p ${ANALYSISDIR}/preselection/top_cut_jet3 -t ${TREES} --no-wait

analyze:
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/preselection.conf -p ${ANALYSISDIR}/preselection -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/top_cut.conf -p ${ANALYSISDIR}/preselection/top_cut -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/signal.conf -p ${ANALYSISDIR}/preselection/top_cut/signal -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/sideband.conf -p ${ANALYSISDIR}/preselection/top_cut/sideband -t ${TREES} --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/btag_loose.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/btag_loose -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/btag_loose/tprime_loose -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/btag_loose/tprime_mid -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/btag_loose/tprime_tight -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/btag_loose.conf -p ${ANALYSISDIR}/preselection/top_cut/sideband/btag_loose -t ${TREES} --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/btag_mid.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/btag_mid -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/btag_mid/tprime_loose -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/btag_mid/tprime_mid -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/btag_mid/tprime_tight -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/btag_mid.conf -p ${ANALYSISDIR}/preselection/top_cut/sideband/btag_mid -t ${TREES} --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/btag_tight.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/btag_tight -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/btag_tight/tprime_loose -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/btag_tight/tprime_mid -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/btag_tight/tprime_tight -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/btag_tight.conf -p ${ANALYSISDIR}/preselection/top_cut/sideband/btag_tight -t ${TREES} --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/wtag_loose.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/wtag_loose -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/wtag_loose/tprime_loose -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/wtag_loose/tprime_mid -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/wtag_loose/tprime_tight -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/wtag_loose.conf -p ${ANALYSISDIR}/preselection/top_cut/sideband/wtag_loose -t ${TREES} --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/wtag_mid.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/wtag_mid -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/wtag_mid/tprime_loose -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/wtag_mid/tprime_mid -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/wtag_mid/tprime_tight -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/wtag_mid.conf -p ${ANALYSISDIR}/preselection/top_cut/sideband/wtag_mid -t ${TREES} --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/wtag_tight.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/wtag_tight -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/wtag_tight/tprime_loose -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/wtag_tight/tprime_mid -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/wtag_tight/tprime_tight -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/wtag_tight.conf -p ${ANALYSISDIR}/preselection/top_cut/sideband/wtag_tight -t ${TREES} --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/top_loose.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/top_loose -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/top_loose/tprime_loose -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/top_loose/tprime_mid -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/top_loose/tprime_tight -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/top_loose.conf -p ${ANALYSISDIR}/preselection/top_cut/sideband/top_loose -t ${TREES} --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/top_mid.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/top_mid -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/top_mid/tprime_loose -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/top_mid/tprime_mid -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/top_mid/tprime_tight -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/top_mid.conf -p ${ANALYSISDIR}/preselection/top_cut/sideband/top_mid -t ${TREES} --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/top_tight.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/top_tight -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/top_tight/tprime_loose -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/top_tight/tprime_mid -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/top_cut/signal/top_tight/tprime_tight -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/new_sequence/top_tight.conf -p ${ANALYSISDIR}/preselection/top_cut/sideband/top_tight -t ${TREES} --no-wait

old_analyze:
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/preselection.conf -p ${ANALYSISDIR}/preselection -t ${TREES} --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_loose_w_loose_b_loose.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_loose  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_loose_w_loose_b_mid.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_mid  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_loose_w_loose_b_tight.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_tight  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_loose_w_mid_b_loose.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_loose  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_loose_w_mid_b_mid.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_mid  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_loose_w_mid_b_tight.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_tight  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_loose_w_tight_b_loose.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_loose  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_loose_w_tight_b_mid.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_mid  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_loose_w_tight_b_tight.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_tight  --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_mid_w_loose_b_loose.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_loose  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_mid_w_loose_b_mid.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_mid  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_mid_w_loose_b_tight.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_tight  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_mid_w_mid_b_loose.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_loose  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_mid_w_mid_b_mid.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_mid  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_mid_w_mid_b_tight.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_tight  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_mid_w_tight_b_loose.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_loose  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_mid_w_tight_b_mid.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_mid  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_mid_w_tight_b_tight.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_tight  --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_tight_w_loose_b_loose.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_loose  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_tight_w_loose_b_mid.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_mid  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_tight_w_loose_b_tight.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_tight  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_tight_w_mid_b_loose.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_loose  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_tight_w_mid_b_mid.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_mid  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_tight_w_mid_b_tight.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_tight  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_tight_w_tight_b_loose.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_loose  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_tight_w_tight_b_mid.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_mid  --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/t_tight_w_tight_b_tight.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_tight  --no-wait

#	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/hadronic_looser.conf -p ${ANALYSISDIR}/preselection/hadronic_looser --no-wait
#	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/hadronic_tighter.conf -p ${ANALYSISDIR}/preselection/hadronic_tighter --no-wait
#	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime.conf -p ${ANALYSISDIR}/preselection/hadronic_looser/test_tprime --no-wait
#	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/hadronic_tighter/test_tprime_tight --no-wait

tprime:
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_mid/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_mid.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_mid/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_tight/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_tight.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_tight/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_loose/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_loose.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_loose/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_mid/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_mid.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_mid/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_tight/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_tight.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_tight/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_loose/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_loose.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_loose/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_mid/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_mid.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_mid/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_tight/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_tight.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_tight/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_loose.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_loose/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_loose.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_loose/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_mid/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_mid.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_mid/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_tight/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_tight.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_tight/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_loose/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_loose.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_loose/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_mid/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_mid.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_mid/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_tight/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_tight.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_tight/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_loose/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_loose.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_loose/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_mid/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_mid.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_mid/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_tight/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_tight.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_tight/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_tight.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_loose/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_loose.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_loose/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_mid/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_mid.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_mid/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_tight/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_tight.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_tight/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_loose/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_loose.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_loose/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_mid/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_mid.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_mid/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_tight/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_tight.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_tight/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_loose/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_loose.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_loose/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_mid/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_mid.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_mid/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_tight/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_tight.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_tight/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_mid.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_loose/tprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_loose.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_loose/bprime --no-wait

sidebands:
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_mid_b_mid_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_mid_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_mid_b_mid_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_mid_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_mid_b_mid_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_mid_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_mid_b_tight_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_tight_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_mid_b_tight_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_tight_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_mid_b_tight_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_tight_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_mid_b_loose_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_loose_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_mid_b_loose_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_loose_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_mid_b_loose_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_loose_w_mid_b_loose_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_tight_b_mid_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_mid_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_tight_b_mid_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_mid_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_tight_b_mid_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_mid_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_tight_b_tight_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_tight_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_tight_b_tight_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_tight_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_tight_b_tight_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_tight_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_tight_b_loose_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_loose_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_tight_b_loose_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_loose_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_tight_b_loose_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_loose_w_tight_b_loose_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_loose_b_mid_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_mid_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_loose_b_mid_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_mid_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_loose_b_mid_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_mid_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_loose_b_tight_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_tight_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_loose_b_tight_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_tight_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_loose_b_tight_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_tight_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_loose_b_loose_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_loose_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_loose_b_loose_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_loose_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_loose_w_loose_b_loose_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_loose_w_loose_b_loose_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_mid_b_mid_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_mid_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_mid_b_mid_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_mid_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_mid_b_mid_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_mid_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_mid_b_tight_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_tight_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_mid_b_tight_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_tight_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_mid_b_tight_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_tight_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_mid_b_loose_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_loose_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_mid_b_loose_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_loose_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_mid_b_loose_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_tight_w_mid_b_loose_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_tight_b_mid_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_mid_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_tight_b_mid_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_mid_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_tight_b_mid_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_mid_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_tight_b_tight_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_tight_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_tight_b_tight_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_tight_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_tight_b_tight_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_tight_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_tight_b_loose_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_loose_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_tight_b_loose_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_loose_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_tight_b_loose_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_tight_w_tight_b_loose_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_loose_b_mid_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_mid_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_loose_b_mid_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_mid_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_loose_b_mid_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_mid_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_loose_b_tight_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_tight_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_loose_b_tight_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_tight_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_loose_b_tight_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_tight_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_loose_b_loose_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_loose_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_loose_b_loose_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_loose_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_tight_w_loose_b_loose_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_tight_w_loose_b_loose_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_mid_b_mid_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_mid_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_mid_b_mid_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_mid_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_mid_b_mid_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_mid_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_mid_b_tight_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_tight_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_mid_b_tight_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_tight_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_mid_b_tight_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_tight_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_mid_b_loose_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_loose_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_mid_b_loose_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_loose_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_mid_b_loose_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_mid_w_mid_b_loose_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_tight_b_mid_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_mid_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_tight_b_mid_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_mid_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_tight_b_mid_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_mid_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_tight_b_tight_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_tight_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_tight_b_tight_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_tight_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_tight_b_tight_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_tight_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_tight_b_loose_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_loose_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_tight_b_loose_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_loose_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_tight_b_loose_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_mid_w_tight_b_loose_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_loose_b_mid_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_mid_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_loose_b_mid_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_mid_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_loose_b_mid_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_mid_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_loose_b_tight_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_tight_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_loose_b_tight_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_tight_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_loose_b_tight_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_tight_sideband_bw --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_loose_b_loose_sideband_b.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_loose_sideband_b --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_loose_b_loose_sideband_w.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_loose_sideband_w --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/t_mid_w_loose_b_loose_sideband_bw.conf -p ${ANALYSISDIR}/preselection/t_mid_w_loose_b_loose_sideband_bw --no-wait

prepare:
	mkdir ${ANALYSISDIR}
	cp ${BASEDIR}/analyzer.py ${ANALYSISDIR}
	cp -r ${BASEDIR}/marclib/ ${ANALYSISDIR}
	cp -r ${BASEDIR}/formatter/ ${ANALYSISDIR}
	cd ${ANALYSISDIR}/marclib/
	patch ${ANALYSISDIR}/marclib/OneCut.py < ${BASEDIR}/patch/onecut.patch
	patch ${ANALYSISDIR}/marclib/SimpleCutSequencer.py < ${BASEDIR}/patch/sequencer.patch
	patch ${ANALYSISDIR}/marclib/anadist.py < ${BASEDIR}/patch/anadist.patch
	patch ${ANALYSISDIR}/marclib/AnaStep.py < ${BASEDIR}/patch/anastep.patch

clean:
	rm -rf ${ANALYSISDIR}
