"""
Word Vector Creation
====================
The following example illustrates how to generate word vectors from a corpus, save them to file and also generate
a custom spacy language model with them.


"""

import enlp.understanding.vectors as vts

###############################################################################
# Load example text

with open("example_data/en_nlptexts.txt", "r") as file:
    text = file.read()

# Tiny bit of preprocessing to get rid of line breaks
docs = text.replace('\n\n','\n').replace('\n',' ')

###############################################################################
# Make word vectors

# input is a list of documents however for the example there is only 1 document
wvs = vts.word_vectors([docs])

###############################################################################
# Save word vectors to file

fname = "example_data/ex_wordvecs.bin"
vts.save_vectors(wvs, fname)

###############################################################################
# Just to show how you can load them back in

my_vecs = vts.load_vectors(fname)





