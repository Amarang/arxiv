import pickle
import gzip
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys, os

def web(filename,user="namin"):
    os.system("scp %s %s@uaf-6.t2.ucsd.edu:~/public_html/dump/ >& /dev/null" % (filename, user))
    print "Copied to uaf-6.t2.ucsd.edu/~%s/dump/%s" % (user, filename.split("/")[-1])

# basedir = "data/"
from config import *

fh = gzip.open(basedir+"combined_%s.pkl" % category,"rb")

d = pickle.load(fh)

authorCounts = []
summaryLength = []
for key in d:
    nauthors = len(d[key]["authors"])
    lensummary = len(d[key]["summary"])
    # lensummary = d[key]["summary"].lower().count(" surprising ")

    if nauthors > 20: continue
    authorCounts.append(nauthors)
    summaryLength.append(lensummary)

fh.close()


authorCounts = np.array(authorCounts)
summaryLength = np.array(summaryLength)

fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
ax.hist(authorCounts,20,color='green',alpha=0.8, range=[0,20])
fig.savefig("plots/authors.png", bbox_inches='tight')
web("plots/authors.png")

fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
ax.hist(summaryLength,30,color='green',alpha=0.8)
fig.savefig("plots/summaryLength.png", bbox_inches='tight')
web("plots/summaryLength.png")

fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
plt.xlabel("n authors")
plt.ylabel("len summary")
ax.hist2d(authorCounts,summaryLength,bins=20,norm=mpl.colors.LogNorm())
fig.savefig("plots/authors_vs_summarylength.png", bbox_inches='tight')
web("plots/authors_vs_summarylength.png")
