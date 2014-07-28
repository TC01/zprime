BASEDIR=${CURDIR}
ANALYSISDIR=${CURDIR}/working/
TREES=/uscms_data/d3/bjr/zprime/hadronic/trees/

all: clean prepare analyze

analyze:
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/preselection.conf -p ${ANALYSISDIR}/preselection -t ${TREES} --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/hadronic_looser.conf -p ${ANALYSISDIR}/preselection/hadronic_looser --no-wait
	${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/hadronic_looser.conf -p ${ANALYSISDIR}/preselection/hadronic_tighter --no-wait

prepare:
	mkdir ${ANALYSISDIR}
	cp ${BASEDIR}/analyzer.py ${ANALYSISDIR}
	cp -r ${BASEDIR}/marclib/ ${ANALYSISDIR}
	cd ${ANALYSISDIR}/marclib/
	patch ${ANALYSISDIR}/marclib/OneCut.py < ${BASEDIR}/patch/onecut.patch
	patch ${ANALYSISDIR}/marclib/SimpleCutSequencer.py < ${BASEDIR}/patch/sequencer.patch

clean:
	rm -rf ${ANALYSISDIR}
