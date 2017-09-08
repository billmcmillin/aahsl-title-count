# -*- coding: utf-8 -*-

##Load SS file and Parse CSV
import csv
import re

ssFilename = "SS title list journals subjects.csv"
ssFile = open(ssFilename, "r")
ssReader = csv.reader(ssFile, delimiter='\t')

##Work through SS file and save title
ssIndex = {}
for row in ssReader:
	row[0] = re.sub("&", "and", row[0])
	if row[2]:
		ssIndex[row[0]] = row[9]
		continue
	elif row[10]:
		ssIndex[row[0]] = row[10]
		continue
	else:
		ssIndex[row[1]] = ""

results = []
for row in ssIndex:
	line = "%s\t%s\t" % (row, ssIndex[row])
	results.append(line)

output = open("SS title list parsed and deduped.txt", "w")
print>>output, "\n".join(results)
