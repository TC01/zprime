#!/usr/bin/env python

import os
import shutil
import sys

import ROOT

def main();

	cutFlows = []

	# Let's use os.getcwd() for now.
	for path, dir, files in os.walk(os.getcwd()):
		for file in files:
			if file == 'output.log':
				print path

if __name__ == '__main__':
	main()
