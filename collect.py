from bs4 import BeautifulSoup
import urllib, urllib2
import pickle
import gzip


def collectBetween(initial,final):
    nSteps = (final-initial)/nResults

    dPapers = {}

    for i in range(nSteps):

        startIndex = initial+nResults*i

        page = urllib2.urlopen("http://export.arxiv.org/api/query?search_query=cat:%s&start=%i&max_results=%i&sortBy=submittedDate&sortOrder=descending" % (category, startIndex, nResults) )
        data = page.read()

        bs = BeautifulSoup(data)

        nEntries = 0
        for entry in bs.findAll("entry"):
            nEntries += 1

            title = entry.title.text.replace("\n"," ")
            updated = entry.updated.text
            published = entry.published.text
            summary = entry.summary.text.replace("\n"," ")
            link = entry.id.text
            authors = [author.text.replace("\n","").encode('ascii',errors='ignore') for author in entry.findAll("author")]

            if link in dPapers: 
                print "DUPLICATE PAPER"
                print entry

            dPapers[link] = { 
                    "title": title,
                    "updated": updated,
                    "published": published,
                    "summary": summary,
                    "authors": authors,
                    }

        print "scanned %i entries from %i to %i (dPapers size:%i)" % (nEntries, startIndex, startIndex+nResults, len(dPapers.keys()))


    filename = "%spapers_%s_%03ik_%03ik.pkl" % (basedir,category,initial//1000,final//1000)
    fhout = gzip.open(filename,"wb")
    pickle.dump(dPapers, fhout)
    fhout.close()

    print "Saved %s" % filename

                 

if __name__ == '__main__':
    # category = "hep-th"
    # basedir = "data/"
    from config import *

    nResults = 500
    for  j in range(20):
        print j*5000, j*5000+5000
        collectBetween(j*5000, j*5000+5000)
