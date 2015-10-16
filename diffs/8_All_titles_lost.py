# -*- coding: utf-8 -*-

indexCurrentYear = open("AAHSL_final15.txt").read().split("\n")
indexCurrentYear.pop(-1)

indexLastYear = open("AAHSL_final14.txt").read().split("\n")
indexLastYear.pop(-1)

# indexCurrentYear = open("test1.txt").read().split("\r")
# indexCurrentYear.pop(-1)

# indexLastYear = open("test2.txt").read().split("\r")
# indexLastYear.pop(-1)

#build and index to idendity ISSN dups (dedup title, fulltitle, ISSN, bib #)
ISSNDedupDictionaryCurrent = {}
titleDedupDictionaryCurrent = {}
ISSNDedupDictionaryLast = {}
titleDedupDictionaryLast = {}

#line[1] is ISSN
#check for ISSN in dictionary - if not, add & flag 0 for not deduped - if present flag 1 for deduped; if no ISSN add to title dictionary
for row in indexCurrentYear:
	line = row.split("\t")
	#if it has an ISSN
	if line[2]:
			if line[2] in ISSNDedupDictionaryCurrent:
	 			ISSNDedupDictionaryCurrent[line[2]][2] = 1
			else:
				line.append(0)
	 			ISSNDedupDictionaryCurrent[line[2]] = line

	#if it has no ISSN, put it in the titleDedup dictionary			
	else:
	 	titleDedupDictionaryCurrent[line[0]] = line
	

#add unmatched items from ISSN diction to title dictionary:
for key in ISSNDedupDictionaryCurrent:
 	if ISSNDedupDictionaryCurrent[key][1]:
 		pass

 	else:
 		titleDedupDictionaryCurrent[ISSNDedupDictionaryCurrent[key][0]] = ISSNDedupDictionaryCurrent[key]


for row in indexLastYear:
	line = row.split("\t")
	#if it has an ISSN
	if line[2]:
			if line[1] in ISSNDedupDictionaryLast:
	 			ISSNDedupDictionaryLast[line[2]][2] = 1
			else:
				line.append(0)
	 			ISSNDedupDictionaryLast[line[2]] = line
	#if it has no ISSN, put it in the titleDedup dictionary			
	else:
	 	titleDedupDictionaryLast[line[0]] = line

#add unmatched items from ISSN diction to title dictionary:
for key in ISSNDedupDictionaryLast:
 	if ISSNDedupDictionaryLast[key][1]:
 		pass

 	else:
 		titleDedupDictionaryLast[ISSNDedupDictionaryLast[key][0]] = ISSNDedupDictionaryLast[key]

ISSNresults = []
results = []
#if the item exists in both dictionaries, discard it, otherwise add it to the results
for key in ISSNDedupDictionaryLast:
	if not (key in ISSNDedupDictionaryCurrent):
		ISSNresults.append("\t".join(ISSNDedupDictionaryLast[key][0:2]))

for key in titleDedupDictionaryLast:
	if not (titleDedupDictionaryLast[key][0] in titleDedupDictionaryCurrent):
		if not (titleDedupDictionaryLast[key][0] in ISSNresults):
			results.append("\t".join(titleDedupDictionaryLast[key][0:3]))

for item in ISSNresults:
	print item

output = open("All_titles_lost.txt", "w")
print>>output, "\n".join(results)