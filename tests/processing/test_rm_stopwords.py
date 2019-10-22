import pytest

# Explicitly set path so don't need to run setup.py - if we have multiple copies of the code we would otherwise need
# to setup a separate environment for each to ensure the code pointers are correct.
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from enlp.processing.stdtools import get_stopwords, rm_stopwords

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

def test_remove_stopwords_simple():

    # arange
    text = 'to be or not to be'
    model = english_language_model()

    # act
    new_text = rm_stopwords(model,text,all_stopwords())

    # assert
    assert new_text == ""



# SIMPLE TESTS - lower case, no punctuation, no numbers
@pytest.mark.parametrize("langModel,text,stopwords_list,expectedOutput", [
    pytest.param(english_language_model(),
                 'the quick brown fox jumped over the lazy dog',
                 english_stopwords(),
                 "quick brown fox jumped lazy dog",
                 id='en_test1_simple'),
    pytest.param(english_language_model(),
                 'oak is strong and also gives shade',
                 english_stopwords(),
                 "oak strong gives shade",
                 id='en_test2_simple'),
    pytest.param(norwegian_language_model(),
                 'den raske brune reven hoppet over den late hunden',
                 norwegian_stopwords(),
                 "raske brune reven hoppet late hunden",
                 id='no_test1_simple'),
    pytest.param(norwegian_language_model(),
                 'eiken er sterk og gir også skygge',
                 norwegian_stopwords(),
                 "eiken sterk gir skygge",
                 id='no_test2_simple'),
])

def test_remove_stopwords_default(langModel, text, stopwords_list, expectedOutput):

    # arange - not needed

    # act
    new_text = rm_stopwords(langModel, text, stopwords_list)

    # assert
    assert new_text == expectedOutput



# COMPLEX TESTS - mixed case, punctuation, numbers
@pytest.mark.parametrize("langModel,text,stopwords_list,expectedOutput", [
    pytest.param(english_language_model(),
                 'Cats and dogs each hate the other.',
                 english_stopwords(),
                 "Cats dogs hate.",
                 id='en_test1_complex'),
    pytest.param(english_language_model(),
                 'I better have passed that test - it is 90 percent of the class grade.',
                 english_stopwords(),
                 "better passed test - 90 percent class grade.",
                 id='en_test2_complex'),
    pytest.param(norwegian_language_model(),
                 'Katter og hunder hater hverandre.',
                 norwegian_stopwords(),
                 "Katter hunder hater hverandre.",
                 id='no_test1_complex'),
    pytest.param(norwegian_language_model(),
                 'Krana tåler maks 100 kilo.',
                 norwegian_stopwords(),
                 "Krana tåler maks 100 kilo.",
                 id='no_test2_complex'),
])
def test_remove_stopwords_default(langModel, text, stopwords_list, expectedOutput):

    # arange - not needed

    # act
    new_text = rm_stopwords(langModel, text, stopwords_list)

    # assert
    assert new_text == expectedOutput

# USING ENGLISH & NORWEGIAN STOPWORDS
@pytest.mark.parametrize("langModel,text,stopwords_list,expectedOutput", [
    pytest.param(english_language_model(),
                 'the quick brown fox jumped over the lazy dog',
                 all_stopwords(),
                 "quick brown fox jumped lazy dog",
                 id='en_test1_mixed'),
    pytest.param(norwegian_language_model(),
                 'den raske brune reven hoppet over den late hunden',
                 all_stopwords(),
                 "raske brune reven hoppet late hunden",
                 id='no_test1_mixed'),
])
def test_remove_stopwords_default(langModel, text, stopwords_list, expectedOutput):

    # arange - not needed

    # act
    new_text = rm_stopwords(langModel, text, stopwords_list)

    # assert
    assert new_text == expectedOutput