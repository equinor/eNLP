"""
NLP Pipeline
============
The following example takes a raw extract of norwegian texts, removes stopwords and lemmatizes prior to analysing the
distribution of the words in the text.
"""

import matplotlib.pyplot as plt
plt.close('all') # very important for read the docs to avoid it crashing due to memory

from enlp.processing.stdtools import get_stopwords, tokenise
from enlp.pipeline import NLPPipeline
from enlp.visualisation.freq_distribution import wordcloud_plot

import spacy



###############################################################################
# Load Spacy's Norwegian language model and the example text
langmodel = spacy.load('nb_dep_ud_sm')
with open("example_data/no_den_stygge_andungen.txt", "r") as file:
    text = file.read()
text = text.replace('\n', ' ')

###############################################################################
# Get a list of stopwords to be removed from the text

# Get stopwords
all_stopwords, stopwords_nb, stopwords_en = get_stopwords()

###############################################################################
# Using NLP pipeline class to create a processing workflow. The pipeline shall involve:
# - remove punctuation
# - remove stopwords
# - stem remaining words

# Initialise object
processed_text = NLPPipeline(langmodel, text)

# Run processing as a pipeline
processed_text.rm_punctuation().rm_stopwords(stopwords=all_stopwords).nltk_stem_no()

#############################################################################
# Compare text strings of firs 80 characters of the original and processed.

print ('Original: ', text[:80], '...')
print ('Processed: ', processed_text.text[:80], '...')


#############################################################################
# Wordcloud comparison between most common words
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
wordcloud_plot(tokenise(langmodel,text), ax=ax1)
wordcloud_plot(processed_text.tokenise().tokens, ax=ax2)
plt.tight_layout()


