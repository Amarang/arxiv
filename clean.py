import pickle
import gzip

# category = "hep-th"
# basedir = "data/"
from config import *

fh = gzip.open(basedir+"combined_%s.pkl" % category,"rb")

d = pickle.load(fh)

fhout = open(basedir+"summaries_%s.txt" % category, "w")

for key in d:
    fhout.write(d[key]["summary"] + "\n")

fhout.close()

