BASEDIR=${CURDIR}
ANALYSISDIR=${CURDIR}/working/
TREES=/eos/uscms/store/user/bjr/trees/

all: clean prepare tprime

tprime:
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/preselection.conf -p ${ANALYSISDIR}/tprime/ -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/leptop.conf -p ${ANALYSISDIR}/tprime/leptop/ --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_400.conf -p ${ANALYSISDIR}/tprime/leptop/had_tprime_400 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_600.conf -p ${ANALYSISDIR}/tprime/leptop/had_tprime_600 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_800.conf -p ${ANALYSISDIR}/tprime/leptop/had_tprime_800 --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/tprime/leptop/one_loose_wtag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_400.conf -p ${ANALYSISDIR}/tprime/leptop/one_loose_wtag/had_tprime_400 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_600.conf -p ${ANALYSISDIR}/tprime/leptop/one_loose_wtag/had_tprime_600 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_800.conf -p ${ANALYSISDIR}/tprime/leptop/one_loose_wtag/had_tprime_800 --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_btag.conf -p ${ANALYSISDIR}/tprime/leptop/one_loose_btag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/tprime/leptop/one_loose_btag/one_loose_wtag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_400.conf -p ${ANALYSISDIR}/tprime/leptop/one_loose_btag/one_loose_wtag/had_tprime_400 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_600.conf -p ${ANALYSISDIR}/tprime/leptop/one_loose_btag/one_loose_wtag/had_tprime_600 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_800.conf -p ${ANALYSISDIR}/tprime/leptop/one_loose_btag/one_loose_wtag/had_tprime_800 --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_2btag.conf -p ${ANALYSISDIR}/tprime/leptop/two_loose_btag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_400.conf -p ${ANALYSISDIR}/tprime/leptop/two_loose_btag/had_tprime_400 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_600.conf -p ${ANALYSISDIR}/tprime/leptop/two_loose_btag/had_tprime_600 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_800.conf -p ${ANALYSISDIR}/tprime/leptop/two_loose_btag/had_tprime_800 --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/tprime/leptop/two_loose_btag/one_loose_wtag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_400.conf -p ${ANALYSISDIR}/tprime/leptop/two_loose_btag/one_loose_wtag/had_tprime_400 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_600.conf -p ${ANALYSISDIR}/tprime/leptop/two_loose_btag/one_loose_wtag/had_tprime_600 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_800.conf -p ${ANALYSISDIR}/tprime/leptop/two_loose_btag/one_loose_wtag/had_tprime_800 --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/inverted_btag.conf -p ${ANALYSISDIR}/tprime/leptop/inverted_btag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/tprime/leptop/inverted_btag/one_loose_wtag --no-wait


tprime_anyjets:
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/preselection_any.conf -p ${ANALYSISDIR}/tprime/leptop_any/ -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_400.conf -p ${ANALYSISDIR}/tprime/leptop_any/had_tprime_400 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_600.conf -p ${ANALYSISDIR}/tprime/leptop_any/had_tprime_600 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_800.conf -p ${ANALYSISDIR}/tprime/leptop_any/had_tprime_800 --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/tprime/leptop_any/one_loose_wtag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_400.conf -p ${ANALYSISDIR}/tprime/leptop_any/one_loose_wtag/had_tprime_400 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_600.conf -p ${ANALYSISDIR}/tprime/leptop_any/one_loose_wtag/had_tprime_600 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_800.conf -p ${ANALYSISDIR}/tprime/leptop_any/one_loose_wtag/had_tprime_800 --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_btag.conf -p ${ANALYSISDIR}/tprime/leptop_any/one_loose_btag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/tprime/leptop_any/one_loose_btag/one_loose_wtag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_400.conf -p ${ANALYSISDIR}/tprime/leptop_any/one_loose_btag/one_loose_wtag/had_tprime_400 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_600.conf -p ${ANALYSISDIR}/tprime/leptop_any/one_loose_btag/one_loose_wtag/had_tprime_600 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_800.conf -p ${ANALYSISDIR}/tprime/leptop_any/one_loose_btag/one_loose_wtag/had_tprime_800 --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_2btag.conf -p ${ANALYSISDIR}/tprime/leptop_any/two_loose_btag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_400.conf -p ${ANALYSISDIR}/tprime/leptop_any/two_loose_btag/had_tprime_400 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_600.conf -p ${ANALYSISDIR}/tprime/leptop_any/two_loose_btag/had_tprime_600 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_800.conf -p ${ANALYSISDIR}/tprime/leptop_any/two_loose_btag/had_tprime_800 --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/tprime/leptop_any/two_loose_btag/one_loose_wtag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_400.conf -p ${ANALYSISDIR}/tprime/leptop_any/two_loose_btag/one_loose_wtag/had_tprime_400 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_600.conf -p ${ANALYSISDIR}/tprime/leptop_any/two_loose_btag/one_loose_wtag/had_tprime_600 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_800.conf -p ${ANALYSISDIR}/tprime/leptop_any/two_loose_btag/one_loose_wtag/had_tprime_800 --no-wait

	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/inverted_btag.conf -p ${ANALYSISDIR}/tprime/leptop_any/inverted_btag --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/loose_wtag.conf -p ${ANALYSISDIR}/tprime/leptop_any/inverted_btag/one_loose_wtag --no-wait

extra:
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_400.conf -p ${ANALYSISDIR}/tprime/leptop/inverted_btag/one_loose_wtag/had_tprime_400 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_600.conf -p ${ANALYSISDIR}/tprime/leptop/inverted_btag/one_loose_wtag/had_tprime_600 --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_tprime_800.conf -p ${ANALYSISDIR}/tprime/leptop/inverted_btag/one_loose_wtag/had_tprime_800 --no-wait

sideband:
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_top.conf -p ${ANALYSISDIR}/tprime/leptop/two_loose_btag/one_loose_wtag/had_top --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/had_top.conf -p ${ANALYSISDIR}/tprime/leptop/one_loose_btag/one_loose_wtag/had_top --no-wait

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
