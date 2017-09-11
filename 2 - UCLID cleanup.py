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

with open('UCLID_combined_fixed.txt', 'rb') as f:
	reader = csv.reader(f, delimiter='\t')
	for row in reader:
		line = re.split('\\\\t', row[0])
		titleFlag = 1
		if line[1]:
			title = re.sub("^\|a", "", line[1])
			title = re.sub(":\|.*", "", title)
			title = re.sub("\|[a-z]*", "", title)
			titleFlag = 0
		if titleFlag:
			if(len(line) > 2):
				if title.lower() in ambigious:
					title = title + " " + line[5]
				else:
					title = line[2]
		title = re.sub("\[electronic resource\]", "", title)
		title = re.sub("\[microform\]", "", title)
		title = re.sub("\([Oo]nline\)", "", title)
		title = re.sub("\(CD\-ROM\)", "", title)
		title = re.sub(" : Online\)", "", title)
		title = re.sub("&", "and", title)
		issn = re.sub("^\|a","", line[2])
		issn2 = re.sub("\|[0-9a-z]", "\t", issn)
		print title.strip() + "\t" + issn + "\t" + issn2
	sys.stdout = orig_stdout
fOut.close()
