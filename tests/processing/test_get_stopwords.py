import pytest
from spacy.lang.en.stop_words import STOP_WORDS as STOP_WORDS_EN
from spacy.lang.nb.stop_words import STOP_WORDS as STOP_WORDS_NB

# Explicitly set path so don't need to run setup.py - if we have multiple copies of the code we would otherwise need
# to setup a separate environment for each to ensure the code pointers are correct.
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from enlp.processing.stdtools import get_stopwords


def test_get_stopwords_english():
    # arrange - get stopwords outwith function
    stops_en_direct = list(STOP_WORDS_EN)
    
    # act - get functions idea of stopwords
    stopwords_func, stopwords_nb_func, stopwords_en_func = get_stopwords()
    
    # assert
    assert stops_en_direct == stopwords_en_func


def test_get_stopwords_norwegian():
    # arrange - get stopwords outwith function
    stops_nb_direct = list(STOP_WORDS_NB)

    # act - get functions idea of stopwords
    stopwords_func, stopwords_nb_func, _ = get_stopwords()

    # assert
    assert stops_nb_direct == stopwords_nb_func


def test_get_stopwords_full():
    # arrange - get stopwords outwith function
    stops_en_direct = list(STOP_WORDS_EN)
    stops_nb_direct = list(STOP_WORDS_NB)

    stopwords = stops_en_direct + stops_nb_direct
    stopwords_direct = [str(i) for i in stopwords]

    # act - get functions idea of stopwords
    stopwords_func, stopwords_nb_func, _ = get_stopwords()

    # assert
    assert stopwords_direct == stopwords_func
