import pytest

# Explicitly set path so don't need to run setup.py - if we have multiple copies of the code we would otherwise need
# to setup a separate environment for each to ensure the code pointers are correct.
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from enlp.pipeline import NLPPipeline
from enlp.processing.stdtools import get_stopwords
import spacy


@pytest.fixture(scope="module")
def english_stopwords():
    stopwords, stops_nb, stops_en = get_stopwords()
    return stops_en

@pytest.fixture(scope="module")
def norwegian_stopwords():
    stopwords, stops_nb, stops_en = get_stopwords()
    return stops_nb

@pytest.fixture(scope="module")
def all_stopwords():
    stopwords, stops_nb, stops_en = get_stopwords()
    return stopwords

@pytest.fixture(scope="module")
def norwegian_language_model():
    return spacy.load('nb_dep_ud_sm')

@pytest.fixture(scope="module")
def english_language_model():
    return spacy.load('en_core_web_md')

def test_remove_stopwords_simple(english_language_model, all_stopwords):

    # arange
    text = 'to be or not to be'
    model = english_language_model

    # act
    new_text = NLPPipeline(model, text).rm_stopwords(stopwords=all_stopwords).text

    # assert
    assert new_text == ""
