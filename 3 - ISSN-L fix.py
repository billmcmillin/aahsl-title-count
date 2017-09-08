# -*- coding: utf-8 -*-
import re

index = open("master index draft.txt").read()

##apply ISSN-L fix
#ISSNTable = open("ISSN-to-ISSN-L_20120801.txt").read().split("\n")
#for row in ISSNTable:
#	line = row.split("\t")
#	index = re.sub(line[0], line[1], index)

##alternate ISSN-L fix
issnDict = {}
ISSNTable = open("data/20170828.ISSN-to-ISSN-L.txt").read().split("\n")
ISSNTable.pop()
for row in ISSNTable:
	row = row.split("\t")
	issnDict[row[0]] = row[1]

finalIndex = []
workingIndex = index.split("\n")
for row in workingIndex:
	print(row)
	fields = row.split("\t")
	try:
		fields[1] = issnDict[fields[1]]
		fields = "\t".join(fields)
		print fields
		next
	except:
		fields = "\t".join(fields)
		print fields
		next
	finally:
		finalIndex.append(fields)
		next

output = open("master index ISSN and title fixed.txt", "w")
print>>output, "\n".join(finalIndex)
