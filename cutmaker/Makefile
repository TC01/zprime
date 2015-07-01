BASEDIR=${CURDIR}
ANALYSISDIR=${CURDIR}/working/
TREES=/srv/data

all: clean prepare tprime

tprime:
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/preselection.conf -p ${ANALYSISDIR}/tprime/ -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_lepton.conf -p ${ANALYSISDIR}/tprime/lep_loose/ --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/tprime/lep_loose/one_loose_wtag --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_btag.conf -p ${ANALYSISDIR}/tprime/lep_loose/one_loose_btag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/tprime/lep_loose/one_loose_btag/one_loose_wtag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_400.conf -p ${ANALYSISDIR}/tprime/lep_loose/one_loose_btag/one_loose_wtag/had_tprime_400 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_800.conf -p ${ANALYSISDIR}/tprime/lep_loose/one_loose_btag/one_loose_wtag/had_tprime_800 --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_2btag.conf -p ${ANALYSISDIR}/tprime/lep_loose/two_loose_btag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_400.conf -p ${ANALYSISDIR}/tprime/lep_loose/two_loose_btag/had_tprime_400 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_800.conf -p ${ANALYSISDIR}/tprime/lep_loose/two_loose_btag/had_tprime_800 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/tprime/lep_loose/two_loose_btag/one_loose_wtag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_400.conf -p ${ANALYSISDIR}/tprime/lep_loose/two_loose_btag/one_loose_wtag/had_tprime_400 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_800.conf -p ${ANALYSISDIR}/tprime/lep_loose/two_loose_btag/one_loose_wtag/had_tprime_800 --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/inverted_btag.conf -p ${ANALYSISDIR}/tprime/lep_loose/inverted_btag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/tprime/lep_loose/inverted_btag/one_loose_wtag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_400.conf -p ${ANALYSISDIR}/tprime/lep_loose/inverted/one_loose_wtag/had_tprime_400 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_800.conf -p ${ANALYSISDIR}/tprime/lep_loose/inverted/one_loose_wtag/had_tprime_800 --no-wait

sideband:
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_top.conf -p ${ANALYSISDIR}/tprime/two_loose_btag/one_loose_wtag/had_top --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_top.conf -p ${ANALYSISDIR}/tprime/one_loose_btag/one_loose_wtag/had_top --no-wait

bprime:
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/preselection.conf -p ${ANALYSISDIR}/bprime/ -t ${TREES}/bprime --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/bprime/one_loose_wtag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_btag.conf -p ${ANALYSISDIR}/bprime/one_loose_btag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_2btag.conf -p ${ANALYSISDIR}/bprime/two_loose_btag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/bprime/one_loose_btag/one_loose_wtag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/bprime/two_loose_btag/one_loose_wtag --no-wait



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
