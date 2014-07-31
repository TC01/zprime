BASEDIR=${CURDIR}
ANALYSISDIR=${CURDIR}/working/
TREES=/uscms_data/d3/bjr/zprime/hadronic/trees/

all: clean prepare analyze

analyze:
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
	cd ${ANALYSISDIR}/marclib/
	patch ${ANALYSISDIR}/marclib/OneCut.py < ${BASEDIR}/patch/onecut.patch
	patch ${ANALYSISDIR}/marclib/SimpleCutSequencer.py < ${BASEDIR}/patch/sequencer.patch

clean:
	rm -rf ${ANALYSISDIR}
