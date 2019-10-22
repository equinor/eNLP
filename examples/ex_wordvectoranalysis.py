"""
Word Vector Analysis
====================
The following example illustrates how to find most similar words, simple word vector maths and how to
visualise similar words in a compressed vector space.

"""
import matplotlib.pyplot as plt
plt.close('all') # very important for read the docs to avoid it crashing due to memory

import enlp.understanding.vectors as vts
from enlp.visualisation.word_vectors import similar_words

###############################################################################
# Download vectors - this can be swapped with loading your own vectors

import gensim.downloader as api

model = api.load("word2vec-google-news-300")  # download the model and return as object ready for use
wvs = model.wv #load the vectors from the model

###############################################################################
# Most similar word to happy

print (vts.similar_words(wvs, 'happy', n=5))

###############################################################################
# Most similar word to zebra

print (vts.similar_words(wvs, 'zebra', n=5))

###############################################################################
# Vector Maths - Past tense of walk?

# ran - run + walk
pwords = ['ran', 'walk']
nwords = ['run']
print (vts.vector_maths(wvs, pwords=pwords, nwords=nwords))

###############################################################################
# Vector Maths - Female equivalent of king?

# Woman - Man + King = ???
pwords = ['woman', 'king']
nwords = ['man']
print (vts.vector_maths(wvs, pwords=pwords, nwords=nwords))

###############################################################################
# Vector Maths - Country of which Edinburgh is the capital?

# Norway - Oslo + Edinburgh
pwords = ['Norway', 'Edinburgh']
nwords = ['Oslo']
print (vts.vector_maths(wvs, pwords=pwords, nwords=nwords))


###############################################################################
# Visualising vectors

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
similar_words(wvs, 'pizza', ax=ax1)
ax1.set_title('Most similar words to pizza')
similar_words(wvs, 'pasta', ax=ax2)
ax2.set_title('Most similar words to pasta')
plt.tight_layout()