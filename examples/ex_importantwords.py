"""
TF-IDF Important Words
======================
The following example compute tf-idf of words in a document to determine the most important words.

NOTE: This is an example to show how to run the procedure however due to the small dataset used
the results are likely to be non-sensical.
"""

import enlp.understanding.distributions as dists
import enlp.processing.stdtools as stdt
import spacy

###############################################################################
# Load example text

with open("example_data/en_historynlp.txt", "r") as file:
    text=file.read()

###############################################################################
# Preprocess text - for this example we have a very small corpus to allow the documentation
# to build therefore we will split the single document into paragraphs for processing to
# imitate multiple document input and we will also remove stopwords as the text is too small
# for the tf-idf computation to handle them. For normal procedures you should NOT remove stopwords
# prior to computing tf-idf scores.

# Split text into paragraphs to imitate documents
paragraphs = text.split('\n\n')
# Remove \n and replace with space
paragraphs = [p.replace('\n',' ') for p in paragraphs]

# Because example text is small, remove stopwords as they'll influence tf-idf scores
en = spacy.load('en_core_web_md')
stopwords, stops_nb, stops_en = stdt.get_stopwords()
paragraphs = [stdt.rm_stopwords(en, p, stops_en) for p in paragraphs]


###############################################################################
# Compute tf-idf scores and determine most important words across full corpus

scores = dists.compute_tfidf(paragraphs)
print (dists.important_words_per_corpus(scores))

###############################################################################
# Determine most important words per document (or for this example, per paragraph)
iw_p_d = dists.important_words_per_doc(scores)

for i, iw in enumerate(iw_p_d):
    print ('Paragraph %i important words: ' %int(i+1))
    print (iw)