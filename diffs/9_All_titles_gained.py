# -*- coding: utf-8 -*-

#this year's totals
indexCurrentYear = open("AAHSL_final14.txt").read().split("\n")
indexCurrentYear.pop(-1)

#last year's totals
indexLastYear = open("AAHSL_final15.txt").read().split("\n")
indexLastYear.pop(-1)

#build and index to idendity ISSN dups (dedup title, fulltitle, ISSN, bib #)
ISSNDedupDictionaryCurrent = {}
titleDedupDictionaryCurrent = {}
ISSNDedupDictionaryLast = {}
titleDedupDictionaryLast = {}

#For this year - check for ISSN in dictionary - if not, add & flag 0 for not deduped  if no ISSN add to title dictionary
for row in indexCurrentYear:
	line = row.split("\t")
	#if it has an ISSN
	line[3] = 0
	if line[2]:
		#if it's already in the dictionary
		if line[2] in ISSNDedupDictionaryCurrent:
				#if it's been seen flag it with a 1
	 			ISSNDedupDictionaryCurrent[line[2]][2] = 1
	 	else:
	 		ISSNDedupDictionaryCurrent[line[2]] = line

	#if it has no ISSN, put it in the titleDedup dictionary			
	else:
	 	titleDedupDictionaryCurrent[line[0]] = line

##For last year - check for ISSN in dictionary - if not, add & flag 0 for not deduped  if no ISSN add to title dictionary

for row in indexLastYear:
	line = row.split("\t")
	#if it has an ISSN
	if line[2]:
		#if it's already in the dictionary
		if line[2] in ISSNDedupDictionaryLast:
				#if it's been seen flag it with a 1
	 			ISSNDedupDictionaryLast[line[2]][2] = 1
	 	else:
	 		ISSNDedupDictionaryLast[line[2]] = line

	#if it has no ISSN, put it in the titleDedup dictionary			
	else:
	 	titleDedupDictionaryLast[line[0]] = line

ISSNresults = []
titleresults = []
results = []

#if the item exists in both ISSN dictionaries, discard it, otherwise add it to the results
for key in ISSNDedupDictionaryLast:
	if not key in ISSNDedupDictionaryCurrent:
		results.append("\t".join(ISSNDedupDictionaryLast[key][0:3]))

#if the item exists in both title dictionaries, discard it, otherwise add it to the results
for key in titleDedupDictionaryLast:
	if not key in titleDedupDictionaryCurrent:
		results.append("\t".join(titleDedupDictionaryLast[key][0:3]))




output = open("All_titles_gained.txt", "w")
print>>output, "\n".join(results)
