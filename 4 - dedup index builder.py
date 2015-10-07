# -*- coding: utf-8 -*-
import re

index = open("master index ISSN fixed.txt").read().split("\n")

results = []


for row in index:
	line = row.split("\t")
	controlledTitle = re.sub("[\(\)\[\],\./:\-;\?'=]", " ", line[0])
	controlledTitle = re.sub(" {2,}", " ", controlledTitle)
	controlledTitle = re.sub("^ +", "", controlledTitle)
	controlledTitle = re.sub(" +$", "", controlledTitle)
	controlledTitle = re.sub("(^[Tt]he )|(^[Aa] )|(^[Aa]n )|(^[Ll][ae]s? )", "", controlledTitle)
	print "%s\t%s\t%s\t%s" % (controlledTitle.lower(), line[0], line[1].lower(), line[2])

#output = open("master index ISSN and title fixed.txt", "w")
#print>>output, "\n".join(results)
