#!/usr/bin/env python

def getPrimeName(string):
	if "tight" in string:
		return "tight"
	elif "loose" in string:
		return "loose"
	else:
		return "mid"

def main():
	top_loose = "jet[X]mass>130&&jet[X]mass<230"
	top_mid = "jet[X]tau32<0.75&&jet[X]mass>130&&jet[X]mass<230"
	top_tight = "jet[X]tau32<0.55&&jet[X]mass>130&&jet[X]mass<230"

	w_loose = "jet[X]mass>70&&jet[X]mass<100"
	w_mid = "jet[X]tau21<0.75&&jet[X]mass>70&&jet[X]mass<100"
	w_tight = "jet[X]tau21<0.5&&jet[X]mass>70&&jet[X]mass<100"

	bottom_loose = "jet[X]csv>0.333&&jet[X]mass<50"
	bottom_mid = "jet[X]csv>0.679&&jet[X]mass<50"
	bottom_tight = "jet[X]csv>0.9&&jet[X]mass<50"
	

	top_cuts = {'t_loose':top_loose, 't_mid':top_mid, 't_tight':top_tight}
	w_cuts = {'w_loose':w_loose, 'w_mid':w_mid, 'w_tight':w_tight}
	bottom_cuts = {'b_loose':bottom_loose, 'b_mid':bottom_mid, 'b_tight':bottom_tight}

	tmakefile_line = "${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_[E].conf -p ${ANALYSISDIR}/preselection/[Q]/tprime --no-wait"
	bmakefile_line = "${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_[E].conf -p ${ANALYSISDIR}/preselection/[Q]/bprime --no-wait"
	for t_name, top_cut in top_cuts.iteritems():
		for w_name, w_cut in w_cuts.iteritems():
			for b_name, bottom_cut in bottom_cuts.iteritems():
				filename = t_name + "_" + w_name + "_" + b_name + ".conf"
				cutfile = open('../cuts/' + filename, 'wb')
				cutfile.write(t_name + ": " + top_cut + "&&!(" + w_cut + ")\n")
				cutfile.write(w_name + ": " + w_cut + "&&!(" + top_cut + ")\n")
				cutfile.write(b_name + ": " + bottom_cut + "\n")
				cutfile.close()
				print "\t" + tmakefile_line.replace("[Q]", t_name + "_" + w_name + "_" + b_name).replace("[E]", getPrimeName(t_name))
				print "\t" + bmakefile_line.replace("[Q]", t_name + "_" + w_name + "_" + b_name).replace("[E]", getPrimeName(b_name))

if __name__ == '__main__':
	main()
