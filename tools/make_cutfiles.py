#!/usr/bin/env python

import os

def getPrimeName(string):
	if "tight" in string:
		return "tight"
	elif "loose" in string:
		return "loose"
	else:
		return "mid"

def writeCutfile(filename, t_name, top_cut, w_name, w_cut, b_name, bottom_cut):
	with open(filename, 'wb') as cutfile:
		cutfile.write(t_name + ": " + top_cut + "&&!(" + w_cut + ")\n")
		cutfile.write(w_name + ": " + w_cut + "&&!(" + top_cut + ")\n")
		cutfile.write(b_name + ": " + bottom_cut + "\n")
	return

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

	# Try to make a directory for sidebands cuts if it doesn't exist.
	try:
		os.mkdir("../cuts/sidebands/")
	except:
		pass

	makefile_line = "${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/sidebands/[Q]_[S].conf -p ${ANALYSISDIR}/preselection/[Q]_[S] --no-wait"
	tmakefile_line = "${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/tprime_[E].conf -p ${ANALYSISDIR}/preselection/[Q]/tprime --no-wait"
	bmakefile_line = "${ANALYSISDIR}/analyzer.py -f ${BASEDIR}/cuts/bprime_[E].conf -p ${ANALYSISDIR}/preselection/[Q].bprime --no-wait"
	for t_name, top_cut in top_cuts.iteritems():
		for w_name, w_cut in w_cuts.iteritems():
			for b_name, bottom_cut in bottom_cuts.iteritems():
				filename = t_name + "_" + w_name + "_" + b_name
				path = os.path.join(os.path.abspath("../"), "cuts", filename) + ".conf"
				writeCutfile(path, t_name, top_cut, w_name, w_cut, b_name, bottom_cut)

				# Create sideband cutfiles.
				sideband_b = os.path.join(os.path.abspath('../'), 'cuts', 'sidebands', filename) + '_sideband_b.conf'
				writeCutfile(sideband_b, t_name, top_cut, w_name, w_cut, b_name, "INV " + bottom_cut)
				sideband_w = os.path.join(os.path.abspath('../'), 'cuts', 'sidebands', filename) + '_sideband_w.conf'
				writeCutfile(sideband_w, t_name, top_cut, w_name, "INV " + w_cut, b_name, bottom_cut)
				sideband_bw = os.path.join(os.path.abspath('../'), 'cuts', 'sidebands', filename) + '_sideband_bw.conf'
				writeCutfile(sideband_bw, t_name, top_cut, w_name, "INV " + w_cut, b_name, "INV " + bottom_cut)

				# Print lines to add to the makefile.
				#print "\t" + tmakefile_line.replace("[Q]", t_name + "_" + w_name + "_" + b_name).replace("[E]", getPrimeName(t_name))
				#print "\t" + bmakefile_line.replace("[Q]", t_name + "_" + w_name + "_" + b_name).replace("[E]", getPrimeName(b_name))
				print "\t" + makefile_line.replace("[Q]", t_name + "_" + w_name + "_" + b_name).replace("[S]", "sideband_b")
				print "\t" + makefile_line.replace("[Q]", t_name + "_" + w_name + "_" + b_name).replace("[S]", "sideband_w")
				print "\t" + makefile_line.replace("[Q]", t_name + "_" + w_name + "_" + b_name).replace("[S]", "sideband_bw")
				print "\n"


if __name__ == '__main__':
	main()
