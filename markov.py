import markovify # pip install markovify
import gzip, pickle

loadModel=False

def dump(d, filename):
    fhout = gzip.open(filename,"wb")
    pickle.dump(d, fhout)

def load(filename):
    fh = gzip.open(filename,"rb")
    return pickle.load(fh)


# basedir="data/"
# category = "hep-th"
from config import *

if not loadModel:
    with open(basedir+"summaries_%s.txt" % category) as f:
        text = f.read()

    text_model = markovify.Text(text, state_size=3)
    chain_json = text_model.chain.to_json()

    dump(chain_json, "data/model_json.pkl")
else:
    text_model = markovify.Text.from_chain( load("data/model_json.pkl") )


for i in range(100):
    sent = text_model.make_sentence(max_overlap_total=6)
    print sent
    print

