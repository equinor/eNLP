"""
Topic Modelling
===============
The following example shows how to generate a topic model from a corpus and then determine the topic of a
new document.

NOTE: This is an example to show how to run the procedure however due to the small dataset used
the results are likely to be non-sensical.
"""

import enlp.understanding.topics as tp
import enlp.processing.stdtools as stdt
import spacy

###############################################################################
# Load example text and get stopwords

with open("example_data/en_nlptexts.txt", "r") as file:
    text=file.read()

all_stopwords, stopwords_nb, stopwords_en = stdt.get_stopwords()


###############################################################################
# Preprocess text - for this example we have a very small corpus to allow the documentation
# to build therefore we will split the single document into paragraphs for processing to
# imitate multiple document input and we will also remove stopwords and punctuation  as the text is too small.

# Split text into paragraphs to imitate documents
docs = text.split('\n\n')
# Remove \n and replace with space
docs = [d.replace('\n',' ') for d in docs]

# Because example text is small, remove stopwords and punctuation
en = spacy.load('en_core_web_md')
stopwords, stops_nb, stops_en = stdt.get_stopwords()
docs = [stdt.rm_punctuation(en,stdt.rm_stopwords(en, d, stops_en)) for d in docs]

###############################################################################
# Create topic model & visualise keywords per topic

tp_model, dictionary = tp.bow_topic_modelling(docs,no_topics=3)
# print topics
tp.print_topic_words(tp_model)

###############################################################################
# Determine the topic of a new document

fake_doc = 'This is a sentence about the importance of artificial intelligence.'
doc_topics = tp.determine_topics(fake_doc, tp_model, dictionary)

# Visualise the top topics for the document
print (doc_topics.sort_values(['score']).head())