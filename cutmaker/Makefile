BASEDIR=${CURDIR}
ANALYSISDIR=${CURDIR}/working/
TREES=/srv/data

all: clean prepare tprime bprime

tprime:
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/preselection.conf -p ${ANALYSISDIR}/tprime/ -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/tprime/one_loose_wtag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_btag.conf -p ${ANALYSISDIR}/tprime/one_loose_btag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_2btag.conf -p ${ANALYSISDIR}/tprime/two_loose_btag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/tprime/one_loose_btag/one_loose_wtag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/tprime/two_loose_btag/one_loose_wtag --no-wait

bprime:
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/preselection.conf -p ${ANALYSISDIR}/bprime/ -t ${TREES}/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/bprime/one_loose_wtag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_btag.conf -p ${ANALYSISDIR}/bprime/one_loose_btag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_2btag.conf -p ${ANALYSISDIR}/bprime/two_loose_btag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/bprime/one_loose_btag/one_loose_wtag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/bprime/two_loose_btag/one_loose_wtag --no-wait




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


prepare:
	mkdir ${ANALYSISDIR}
	cp ${BASEDIR}/analyzer.py ${ANALYSISDIR}
	cp -r ${BASEDIR}/marclib/ ${ANALYSISDIR}
	cp -r ${BASEDIR}/formatter/ ${ANALYSISDIR}
	cd ${ANALYSISDIR}/marclib/
#	patch ${ANALYSISDIR}/marclib/OneCut.py < ${BASEDIR}/patch/onecut.patch
#	patch ${ANALYSISDIR}/marclib/SimpleCutSequencer.py < ${BASEDIR}/patch/sequencer.patch
#	patch ${ANALYSISDIR}/marclib/anadist.py < ${BASEDIR}/patch/anadist.patch
#	patch ${ANALYSISDIR}/marclib/AnaStep.py < ${BASEDIR}/patch/anastep.patch

clean:
	rm -rf ${ANALYSISDIR}
