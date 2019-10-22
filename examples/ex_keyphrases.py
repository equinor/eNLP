"""
Keyphrase Extraction (English)
==============================
The following example uses a python implementation of the Rapid Automatic Keyword Extraction algorithm to extract
keyphrases from a text.
"""

import pandas as pd
from enlp.processing.stdtools import get_stopwords
from enlp.understanding.keywords import keyphrase_list

###############################################################################
# Load example text and get stopwords

with open("example_data/en_historynlp.txt", "r") as file:
    text=file.read()

all_stopwords, stopwords_nb, stopwords_en = get_stopwords()

###############################################################################
# Extract keyphrases

keyphrases = keyphrase_list(text,
                            stopwords=stopwords_en,
                            )

print (pd.DataFrame(keyphrases, columns=['score', 'keyphrase']).head(10))