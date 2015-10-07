aahsl-title-count
=================

Series of scripts for compiling a de-duped title list of journals.

Scripts are to be run in numerical order, using source data as is modeled in the `samples/` folder. 

## Notes on data

### ISSN

The ISSN-L data is available from the [ISSN center](http://www.issn.org/services/online-services/access-to-issn-l-table/).

### Serials Solutions

Export all journals, with subjects in multiple-columns, in UTF-8, unjoined (as `report.csv`). Then scope the list to journals using the following command:
```
`grep -f ./ss-subject-list.txt report.csv > "SS title list journals subjects.csv"`
```
### UCLID

Acquire data in csv format using the included PGSQL queries. Filter to remove delimiters and retain only the first two ISSNs.

### Steps

1. Export titles all journals from SS
	Export all journals, with subjects in multiple-columns, in UTF-8, unjoined (as report.csv). Then scope the list to journals using the following command:
	```
		grep -f ./aahsl-title-count/ss-subject-list.txt report.csv > "SS title list journals subjects.csv"
	```
2. Run queries in PgAdmin
	-update year to current year
	-output as "UCLID title list.txt" and "UCLID title list2.txt" with \t as separator and no quoting
3. Join 2 files together with 
	```
	$ find . -maxdepth 1 -name "*.txt" | xargs -n 1 tail -n +2 > UCLID_combined.txt

	$ mv UCLID_combined.txt UCLID\ title\ list.txt
	```
4. make sure "SS title list journals subjects.csv" is in same dir as python scripts
	```
	$ python 1\ -\ SS\ parse\ and\ dedup.py 
	```
5. make sure "UCLID title list.txt" is in same dir as python scripts
	```
	$ python 2\ -\ UCLID\ cleanup.py 
	```
6. make sure "master index draft.txt" and "ISSN_to_ISSN-L_20120801.txt" are in same dir as python scripts
	```
	$ python 3\ -\ ISSN-L\ fix.py > master\ index\ ISSN\ fixed.txt

	```
7. remove two extra newline chars from end of file "master index ISSN fixed.txt"
	```
	python 4\ -\ dedup\ index\ builder.py > master\ index\ ISSN\ and\ title\ fixed.txt
	```
8. 
	```
	python 5\ -\ Super-duper-deduper\!.py 
	```