aahsl-title-count
=================

Series of scripts for compiling a de-duped title list of journals.

Scripts are to be run in numerical order, using source data as is modeled in the `samples/` folder. 

## Notes on data

### ISSN

The ISSN-L data is available from the [ISSN center](http://www.issn.org/services/online-services/access-to-issn-l-table/).

### Serials Solutions

Export all journals, with subjects in multiple-columns, in UTF-8, unjoined (as `report.csv`). Then scope the list to journals using the following command:

`grep -f ./ss-subject-list.txt report.csv > "SS title list journals subjects.csv"`

### UCLID

Acquire data in csv format using the included PGSQL queries. Filter to remove delimiters and retain only the first two ISSNs.
