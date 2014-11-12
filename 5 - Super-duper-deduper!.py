# -*- coding: utf-8 -*-
index = open("master index ISSN and title fixed.txt").read().split("\n")
index.pop(-1)

#build and index to idendity ISSN dups (dedup title, fulltitle, ISSN, bib #)
ISSNDedupDictionary = {}
titleDedupDictionary = {}

#check for ISSN in dictionary - if not, add & flag 0 for not deduped - if present flag 1 for deduped; if no ISSN add to title dictionary
for row in index:
	line = row.split("\t")
	if line[2]:
		if line[2] in ISSNDedupDictionary:
			ISSNDedupDictionary[line[2]][4] = 1
		else:
			line.append(0)
			ISSNDedupDictionary[line[2]] = line
	else:
		titleDedupDictionary[line[0]] = line

#add unmatched items from ISSN diction to title dictionary:
for key in ISSNDedupDictionary:
	if ISSNDedupDictionary[key][4]:
		pass
	else:
		titleDedupDictionary[ISSNDedupDictionary[key][0]] = ISSNDedupDictionary[key]

results = []
for key in ISSNDedupDictionary:
	if ISSNDedupDictionary[key][4]:
		results.append("\t".join(ISSNDedupDictionary[key][0:4]))
for key in titleDedupDictionary:
	results.append("\t".join(titleDedupDictionary[key][0:4]))

output = open("AAHSL final list.txt", "w")
print>>output, "\n".join(results)
