# -*- coding: utf-8 -*-
import re, csv, sys

orig_stdout = sys.stdout
fOut = file('UCLID parsed.txt', 'w')
sys.stdout = fOut

##Clean up UCLID list - field in this order
##RECORD #(BIBLIO)	130	245	022|a	022|y	11?	240

#if 130 present, use only that
#if 245 is ambigious word, add 11?
#use first available well-formated ISSN

#remove first line
#file.pop(0)

results = []

ambigious = {
	'transactions' : "",
	'report' : "",
	'bulletin' : "",
	'health' : "",
	'membership roster' : "",
	'weekly report' : "",
	'annual report' : "",
	'verhandlungen' : "",
	'proceedings' : "",
	'annual directory' : "",
	'case records' : "",
	'research report' : "",
	'memoirs' : "",
	'health systems plan' : "",
	'annual implementation plan' : "",
	'minutes of meetings' : "",
	'transactions of the ... annual meeting' : "",
	'historical series' : "",
	'resource directory' : "",
	'bulletins' : "",
	'bulletins et mémoires' : "",
	'abstract of proceedings' : "",
	'annali' : "",
}

with open('UCLID_combined.txt', 'rb') as f:
	reader = csv.reader(f, delimiter='\t')
	for row in reader:
		line = re.split('\\\\t', row[0])
		titleFlag = 1
		if line[1]:
			title = line[1]
			titleFlag = 0
		if titleFlag:
			if(len(line) > 2):
				if line[2].lower() in ambigious:
					title = line[2] + " " + line[5]
				else:
					title = line[2]
		title = re.sub("\[electronic resource\]", "", title)
		title = re.sub("\[microform\]", "", title)
		title = re.sub("\([Oo]nline\)", "", title)
		title = re.sub("\(CD\-ROM\)", "", title)
		title = re.sub(" : Online\)", "", title)
		title = re.sub("&", "and", title)
		if(len(line) > 3):
			if line[3]:
				issn = line[3]
		else:
			issn = ""
		print title + "\t" + issn + "\t" + line[0] 
	
	sys.stdout = orig_stdout
fOut.close()
