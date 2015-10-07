# -*- coding: utf-8 -*-

##Load SS file and Parse CSV
import csv
import re

ssFilename = "SS title list journals subjects.csv"
ssFile = open(ssFilename, "r")
ssReader = csv.reader(ssFile)

##Work through SS file and save title
ssIndex = {}
for row in ssReader:
	row[1] = re.sub("&", "and", row[1])
	if row[2]:
		ssIndex[row[1]] = row[2]
		continue
	elif row[3]:
		ssIndex[row[1]] = row[3]
		continue
	else:
		ssIndex[row[1]] = ""

results = []
for row in ssIndex:
	line = "%s\t%s\t" % (row, ssIndex[row])
	results.append(line)

output = open("SS title list parsed and deduped.txt", "w")
print>>output, "\n".join(results)