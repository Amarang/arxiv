from bs4 import BeautifulSoup
import urllib, urllib2
import pickle
import gzip
import os
import copy

from config import *
# category = "hep-th"
# basedir = "data/"

filenames = os.listdir(basedir)

dOut = {}
for filename in filenames:
    if not filename.startswith("papers_%s_" % category): continue

    fh = gzip.open(basedir+filename,"rb")
    d = pickle.load(fh)
    fh.close()
    for key in d:
        dOut[key] = copy.deepcopy(d[key])

    d.clear()

fhout = gzip.open(basedir+"combined_%s.pkl" % category,"wb")
pickle.dump(dOut, fhout)
