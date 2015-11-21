## Extract Database URLs from the NAR database issues 

First we need to extract the database list from the NAR database issues. Below is the list of database issue from 2004 to 2015. Each issue contains a list of articles. 

- [2004](http://nar.oxfordjournals.org/content/32/suppl_1.toc)
- [2005](http://nar.oxfordjournals.org/content/vol33/suppl_1/index.dtl)
- [2006](http://nar.oxfordjournals.org/content/vol34/suppl_1/index.dtl)
- [2007](http://nar.oxfordjournals.org/content/vol35/suppl_1/index.dtl)
- [2008](http://nar.oxfordjournals.org/content/vol36/suppl_1/index.dtl)
- [2009](http://nar.oxfordjournals.org/content/vol37/suppl_1/index.dtl)
- [2010](http://nar.oxfordjournals.org/content/vol38/suppl_1/index.dtl)
- [2011](http://nar.oxfordjournals.org/content/vol39/suppl_1/index.dtl)
- [2012](http://nar.oxfordjournals.org/content/vol40/issueD1/index.dtl)
- [2013](http://nar.oxfordjournals.org/content/vol41/issueD1/index.dtl)
- [2014](http://nar.oxfordjournals.org/content/vol42/issueD1/index.dtl)
- [2015](http://nar.oxfordjournals.org/content/vol43/issueD1/index.dtl)

The article page contains abstract text and the link to the database. The first appearance date of a database will be approximated as the year of the issue that it was published. Unfortunately the link to the database is not formatted and it could be potentially difficult to extract them.

`html` folder contains the script and downloaded article page. Most abstracts contains a well-formatted URLs in them. `html/urllist_exceptions.py` is written to capture those abstracts without a well-formatted URLs. These abstracts with exceptions are manually edited to contain a well-formatted URLs and stored under `html/exceptions` folder.

## Issues with database articles

Below is a list of issues that I noticed while processing these links.

- Links with different ownership. For example, `_content_38_suppl_1_D765.abstract` describes a database, named [BioDrugScreen](http://biodrugscreen.org). The link is alive, but the clearly the current page is not what the article described.
- Links with multiple appearance. For example, `DDBJ` and `MetaCyc` database appears multiple times with slight update.
- Links with IP address. ARE YOU KIDDING ME????
- Links with websites that have moved to a new domain. For example, ProTherm has moved to a new domain name from http://gibk26.bse.kyutech.ac.jp/jouhou/Protherm/protherm.html to http://www.abren.net/protherm

## Determining the last appearance date of a website

Given the issues above, it could be difficult to correctly identify the "last appearance date". What could be a best strategy to achieve this?

![Determining the last appearance of a website][diagram]

[diagram]: diagram.png width=400px

