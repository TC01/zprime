import os
import shutil

global_template = os.path.join("formatter", "post.tex")

def getCutNames(name):
	t_name = name[name.find("t_") + 2:name.find("t_") + 7]
	w_name = name[name.find("w_") + 2:name.find("w_") + 7]
	b_name = name[name.find("b_") + 2:name.find("b_") + 7]
	if "mid" in t_name:
		t_name = "mid"
	if "mid" in w_name:
		w_name = "mid"
	if "mid" in b_name:
		b_name = "mid"

	message = "The cuts were applied in the following sequence:\n" + "Cut 1: top jet (" + t_name + ")\nCut 2: W jet (" + w_name + ")\nCut 3: bottom jet (" + b_name + ")\n\n\n"
	return message

def processPrimeText(text, name):
	newlines = text.count('\n')
	newtext = ""
	lines = text.split('\n')
	flag = False
	for i in range(newlines):
		line = lines[i]
		if "Applying" in line:
			if "prime" in line:
				desc = line[line.find("prime_") + 6:]
			else:
				desc = line[line.find("b_") + 2:]
				desc = desc[desc.find("_") + 1:]
			newtext += "Applying cut to " + desc + ":\n"
		elif "Original" in line:
			working_length = len("-- Original Tree had ")
			newtext += "Original: " + line[working_length:-1] + ", new has: "
			if " 0 events" in line:
				flag = True
		elif "New" in line:
			working_length = len("-- New Tree has ")
			newtext += line[working_length:-1] +  ", efficiency is "
			if flag:
				flag = False
				newtext += "N/A.\n"
		elif "Efficiency" in line:
			working_length = len("--        Efficiency: ")
			newtext += line[working_length:-1] + ".\n"
		else:
			newtext += "\n"

	return newtext

def extractEventCount(lines, i):
	countline = lines[i+1]
	try:
		nextline = lines[i+2]
	except:
		nextline = ""
	
	while nextline.lstrip().rstrip() != "":
		countline = nextline
		i += 1
		try:
			nextline = lines[i+2]
		except:
			pass
	count = countline[countline.find("new has: ") + len("new has: "):]
	count = count[:count.find(" ")]
	count = int(count)
	return count

def getEventCounts(text):
	"""Returns a tuple of bkgcount, sigcounts containing the event counts."""
	lines = text.split("\n")
	sigcounts = {'1500':0, '2000':0, '3000':0}
	bkgcount = 0
	for i in range(len(lines)):
		line = lines[i]
		if line.lstrip().rstrip() == "":
			continue
		if "Applying cut" in line:
			if not "signal" in line:
				count = extractEventCount(lines, i)
				bkgcount += count
			else:
				count = extractEventCount(lines, i)
				if '1500' in line:
					sigcounts['1500'] += count
				elif '2000' in line:
					sigcounts['2000'] += count
				else:
					sigcounts['3000'] += count
	return bkgcount, sigcounts

def processText(text, name):
	text = processPrimeText(text, name)
	bkgcount, sigcounts = getEventCounts(text)
	#text = getCutNames(name) + text

	# Add summarized event counts for the last step of the analysis.
	text += "Number of background events = " + str(bkgcount) + "\n"
	text += "1500 GeV signal: num_sig = " + str(sigcounts['1500']) + ", num_sig / sqrt(num_bkg) = " + str(float(sigcounts['1500'])/float(bkgcount)) + "\n"
	text += "2000 GeV signal: num_sig = " + str(sigcounts['2000']) + ", num_sig / sqrt(num_bkg) = " + str(float(sigcounts['1500'])/float(bkgcount)) + "\n"
	text += "3000 GeV signal: num_sig = " + str(sigcounts['3000']) + ", num_sig / sqrt(num_bkg) = " + str(float(sigcounts['1500'])/float(bkgcount)) + "\n"

	return text

def doLogParsing(path, log="output.log"):
	name, sep, ext = log.partition(".")
	fullpath = os.path.join(path, log)
	newfile = os.path.join(path, name + ".txt")
	# Open the old log file, feed it into the processor, write to new file.
	with open(fullpath, 'rb') as object:
		text = object.read()
		text = processText(text, newfile)
		with open(newfile, 'wb') as object:
			object.write(text)

def doFormatting(name, path, template=global_template):
	"""Creates a latex source called post.tex in the working directory path."""
	
	if not os.path.exists(path):
		print "Error in libformatter."
		return

	# Copy the template into the path.
	shutil.copy(template, os.path.join(path, "post.tex"))

	# Find the right plot and make a copy called "analysis.png".
	imageFile = os.path.join(path, "plots", name) + ".png"
	shutil.copy(imageFile, os.path.join(path, "analysis.png"))

	# Do log parsing
	doLogParsing(path)

	# Invoke latex.
	curdir = os.getcwd()
	os.chdir(path)
	os.system("pdflatex post.tex")
	os.chdir(curdir)