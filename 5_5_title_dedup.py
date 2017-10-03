# -*- coding: utf-8 -*-
import re

index = open("AAHSL_issn_deduped.txt").read().split("\n")
index.pop()

#build and index to idendity ISSN dups (dedup title, fulltitle, ISSN, bib #)
titleDedupDictionary = {}

results = []

pattern = re.compile(r"\|.*")

for row in index:
	line = row.split("\t")
	if line[0]:
		if pattern.search(line[0]):
			title = pattern.sub("",line[0])
			line[0] = title
			print(title)
		if line[0] in titleDedupDictionary:
			pass
		else:
			results.append(row)
			titleDedupDictionary[line[0]] = 1

output = open("AAHSL final list.txt", "w")
print>>output, "\n".join(results)
