"""
Removing Stopwords
==================
XXX
"""

# Import necessary packages
from enlp.processing.stdtools import get_stopwords, rm_stopwords, tokenise
import enlp.understanding.distributions as dists
import spacy
import pandas as pd

import matplotlib.pyplot as plt
plt.close('all') # very important for read the docs to avoid it crashing due to memory


###############################################################################
# Load text to be processed and the appropriate language model

# Load text file
with open("example_data/en_historynlp.txt", "r") as file:
    text=file.read()
print (text)

# Load spacy language model
langmodel = spacy.load('en_core_web_md')


###############################################################################
# Get stopwords: the stopwords function will get all english and norwegian stopwords

stopwords_func, stopwords_nb_func, stopwords_en_func = get_stopwords()
print (stopwords_en_func[:5])

###############################################################################
# Remove english stopwords

processed_text = rm_stopwords(langmodel, text, stopwords_en_func)
print (processed_text)

###############################################################################
# Now that the stopwords have been removed then the sentences no longer make much sense. Therefore, an alternative to
# viewing the text output is to look at the distribution of the remaining text


orig_top10 = pd.DataFrame(dists.freq_dist(tokenise(langmodel, text)), columns=['token', 'count'])
pr_top10 = pd.DataFrame(dists.freq_dist(tokenise(langmodel, processed_text)), columns=['token', 'count'])

print ("ORIGINAL - top 10 words")
print (orig_top10.head(10))
print (" ")
print ("PROCESSED - top 10 words")
print (pr_top10.head(10))