#!/usr/bin/env python

# A tool to do further processing on the efficiency results.

import copy
import optparse
import os
import shutil
import sys

class Efficiency:
	
	def __init__(self, start, end):
		self.start = start
		self.end = end
		try:
			self.percentage = (float(end) / float(start)) * 10
		except:
			self.percentage = 0.0

	def __str__(self):
		return "Efficiency: " + str(self.start) + " to " + str(self.end) + " with " + str(self.percentage) + "%"
	
	def __repr__(self):
		return self.__str__()

class CutSample:
	
	def __init__(self, name):
		self.name = name
		self.cutnames = []
		self.efficiencies = []
		
	def __str__(self):
		result = "Cuts for sample " + self.name + "\n"
		result += "----------------------------------\n" 
		for i in xrange(len(self.cutnames)):
			result += self.cutnames[i] + ":\n    " + str(self.efficiencies[i]) + "\n"
		result += "\n" + str(self.makeFinalEfficiency())
		return result
	
	def __repr__(self):
		return self.__str__()
		
	def insert(self, cutname, efficiency):
		self.cutnames.append(cutname)
		self.efficiencies.append(efficiency)
		
	def get(self, cutname):
		index = self.cutnames.index(cutname)
		if index != -1:
			return self.efficiencies[index]
		else:
			return None
		
	def makeFinalEfficiency(self):
		start = self.efficiencies[0].start
		end = self.efficiencies[len(self.cutnames) - 1].end
		return Efficiency(start, end)
		
	def add(self, child):
		if child.name != self.name:
			raise RuntimeError("Tried to add two cut samples together, " + self.name + ", " + child.name)
		self.cutnames = self.cutnames + child.cutnames
		self.efficiencies = self.efficiencies + child.efficiencies
		return self

def transformName(name):
	# Until I fix some stupid formatlib bug...
	validNames = ['ttbar', 'qcd', 'singletop', 'wjets', 'signal']
	newName = name
	for root in validNames:
		if name[0:len(root)] == root:
			break
		elif root in name:
			name = name[name.find(root):]
			break
	return name

def formatOutput(analysis):
	# Get the names of the cuts from cuts.order.
	cutsOrder = os.path.join(analysis, 'cuts.order')
	if not os.path.exists(cutsOrder):
		cutsOrder = os.path.join(analysis, 'cuts.conf')
	cutlines = []
	cutnames = []
	with open(cutsOrder, 'rb') as orderfile:
		for line in orderfile:
			if '#' != line[0]:
				cutlines.append(line)
				cutname = line.split(':')[0]
				if 'Added cut ' in cutname:
					cutname = cutname[len('Added cut '):]
				cutnames.append(cutname)
	
	# Now iterate through the output text file and build an object.
	samples = {}
	with open(os.path.join(analysis, 'output.txt')) as outputLog:
		sample = None
		index = 0
		for line in outputLog:
			if "Applying cut to " == line[:len("Applying cut to ")]:
				name = line[len("Applying cut to "):].rstrip(':\n')
				name = transformName(name)
				sample = CutSample(name)
				samples[name] = sample
				index = 0
			if 'Original:' in line:
				original = line[len("Original: "):line.find(" events")]
				final = line[line.find("new has: ") + len("new has: "):line.rfind(" events")]
				try:
					original = int(original)
					final = int(final)
				except:
					print "Error: oh no! Something has gone wrong! Yay unhelpful errors!"
					sys.exit(1)
				efficiency = Efficiency(original, final)
				samples[name].insert(cutnames[index], efficiency)
				samples.update()
				index += 1

	return samples

def addSamples(parents, children):
	new = {}
	for name, parent in parents.iteritems():
		result = parent.add(children[name])
		new[name] = result
		new.update()
	return new

def main():
	# Get the root directory from arguments or use current.
	try:
		root = sys.argv[1]
	except IndexError:
		root = os.getcwd()
	root = os.path.abspath(root)

	# Make sure the directory exists and has an output.log.
	if not os.path.exists(root):
		print "Error: directory " + root + " does not exist, exiting."
		sys.exit(1)
	if not os.path.exists(os.path.join(root, "output.log")):
		print "Error: directory " + root + " is not a zprime analysis output directory."
	
	analysisDirs = []
	for path, dir, files in os.walk(root):
		if 'output.log' in files:
			analysisDirs.append(path)
		
	analysisObjects = {}
	for analysis in analysisDirs:
		print "Processing " + analysis
		analysisObject = formatOutput(analysis)
		analysisObjects[analysis] = analysisObject
		
	for analysis in analysisDirs:
		print "Writing output for " + analysis
		
		steps = [root]
		dirs = analysis[len(root):].split('/')
		newRoot = root
		for stepDir in dirs:
			if stepDir == '':
				continue
			newRoot = os.path.join(newRoot, stepDir)
			steps.append(newRoot)
			
		# Now that we have an array of step objects, step through them!
		outputDict = analysisObjects[steps[0]]
		for step in steps[1:]:
			outputDict = addSamples(copy.deepcopy(outputDict), analysisObjects[step])
		with open(os.path.join(analysis, 'efficiencies.txt'), 'wb') as results:
			for sample, efficiencies in outputDict.iteritems():
				results.write(str(efficiencies) + '\n\n')

if __name__ == '__main__':
	main()