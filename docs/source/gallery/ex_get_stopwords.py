"""
Removing Stopwords
==================
XXX
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as pltgs

from enlp.processing.stdtools import get_stopwords

plt.close('all') # very important for read the docs to avoid it crashing due to memory

###############################################################################
# Some text

# act - get functions idea of stopwords
stopwords_func, stopwords_nb_func, stopwords_en_func = get_stopwords()

print (stopwords_en_func[:5])