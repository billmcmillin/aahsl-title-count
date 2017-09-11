# -*- coding: utf-8 -*-
import re, sys

orig_stdout = sys.stdout
fOut = file('master index ISSN and title fixed.txt', 'w')
sys.stdout = fOut

index = open("master index ISSN fixed.txt").read().split("\n")

for row in index:
	line = row.split("\t")
	controlledTitle = re.sub("[\(\)\[\],\./:\-;\?'=]", " ", line[0])
	controlledTitle = re.sub(" {2,}", " ", controlledTitle)
	controlledTitle = re.sub("^ +", "", controlledTitle)
	controlledTitle = re.sub(" +$", "", controlledTitle)
	controlledTitle = re.sub("(^[Tt]he )|(^[Aa] )|(^[Aa]n )|(^[Ll][ae]s? )", "", controlledTitle)
	print "%s\t%s\t%s\t%s" % (controlledTitle.lower(), line[0], line[1].lower(), line[2])


sys.stdout = orig_stdout
fOut.close()

