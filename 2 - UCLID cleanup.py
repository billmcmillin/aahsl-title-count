# -*- coding: utf-8 -*-
import re

##Clean up UCLID list - field in this order
##RECORD #(BIBLIO)	130	245	022|a	022|y	11?	240

#if 130 present, use only that
#if 245 is ambigious word, add 11?
#use first available well-formated ISSN

file = open("UCLID title list.txt").read().split("\r\n")

#remove first line
file.pop(0)

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

for row in file:
	title = ""
	issn = ""
	line = row.split("\t")
	titleFlag = 1
	if line[1]:
		title = line[1]
		titleFlag = 0
	if titleFlag:
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
	if line[3]:
		issn = line[3]
	elif line[4]:
		issn = line[4]
	else:
		issn = ""
	print title + "\t" + issn + "\t" + line[0]

#output = open("UCLID parsed.txt", "w")
#print>>output, "\n".join(results)
#output.close()
