"""
Visualising Word Counts
=======================
The following example takes a raw extract of norwegian texts, removes stopwords and lemmatizes prior to analysing the
distribution of the words in the text.
"""

import enlp.visualisation.freq_distribution as viz
import enlp.understanding.distributions as dists
import enlp.processing.stdtools as nlp
import spacy
import matplotlib.pyplot as plt

plt.close('all') # very important for read the docs to avoid it crashing due to memory

###############################################################################
# Load Spacy's Norwegian language model and the example text
langmodel = spacy.load('nb_dep_ud_sm')
with open("example_data/no_den_stygge_andungen.txt", "r") as file:
    text=file.read()

###############################################################################
# Make  strings into list of tokens and count them
word_list = nlp.tokenise(langmodel,text)
counts = dists.freq_dist(word_list)

###############################################################################
# Visualise
fig,(ax1,ax2) = plt.subplots(1, 2, figsize=(10, 5))
viz.dist_plot_detailed(counts[:25], ax=ax1)  # Detailed distribution of top 25 tokens
viz.dist_plot(counts, log=True, ax=ax2)  # Full distribution of corpus
plt.show()