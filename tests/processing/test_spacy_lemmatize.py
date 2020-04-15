import pytest

# Explicitly set path so don't need to run setup.py - if we have multiple copies of the code we would otherwise need
# to setup a separate environment for each to ensure the code pointers are correct.
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from enlp.processing.stdtools import spacy_lemmatize

import spacy

@pytest.fixture(scope="module")
def norwegian_language_model():
    return spacy.load('nb_dep_ud_sm')

@pytest.fixture(scope="module")
def english_language_model():
    return spacy.load('en_core_web_md')


def test_lemmatize_simple(norwegian_language_model):
    
    # arange
    text='den raske brune reven hoppet over den late hunden'
    model = norwegian_language_model
    
    # act
    lemmad_text = spacy_lemmatize(model, text)
    
    #assert 
    assert lemmad_text == "den rask brun rev hoppe over den lat hund"


# ENGLISH
@pytest.mark.parametrize("english_language_model,text,expectedoutput",
                         [pytest.param(english_language_model,
                                       'the quick brown fox jumped over the lazy dog',
                                       "the quick brown fox jump over the lazy dog",
                                       id='en_test1_simple'),
                          pytest.param(english_language_model,
                                       'oak is strong and also gives shade',
                                       "oak be strong and also give shade",
                                       id='en_test2_simple'),
                          pytest.param(english_language_model,
                                       'Cats and dogs each hate the other.',
                                       "cat and dog each hate the other.",
                                       id='en_test1_complex'),
                          pytest.param(english_language_model,
                                       'I better have passed that test - it is 90 percent of the class grade.',
                                       "I better have pass that test - it be 90 percent of the class grade.",
                                       id='en_test2_complex'),
                          ],
                         indirect=['english_language_model'],
                         )
def test_lemmatize_simple(english_language_model, text, expectedoutput):

    # arange - not needed

    # act
    lemmad_text = spacy_lemmatize(english_language_model, text)

    #assert
    assert lemmad_text == expectedoutput


# NORWEGIAN
@pytest.mark.parametrize("norwegian_language_model,text,expectedoutput",
                         [pytest.param(norwegian_language_model,
                                       'den raske brune reven hoppet over den late hunden',
                                       "den rask brun rev hoppe over den lat hund",
                                       id='no_test1_simple'),
                          pytest.param(norwegian_language_model,
                                       'eiken er sterk og gir også skygge',
                                       "eike er sterk og gire også skygge",
                                       id='no_test2_simple'),
                          pytest.param(norwegian_language_model,
                                       'Katter og hunder hater hverandre.',
                                       "katte og hund hate hverandre.",
                                       id='no_test1_complex'),
                          pytest.param(norwegian_language_model,
                                       'Krana tåler maks 100 kilo.',
                                       "krana tåle maks 100 kilo.",
                                       id='no_test2_complex'),
                          ],
                         indirect=['norwegian_language_model'],
                         )
def test_lemmatize_no(norwegian_language_model, text, expectedoutput):
    # arange - not needed

    # act
    lemmad_text = spacy_lemmatize(norwegian_language_model, text)

    # assert
    assert lemmad_text == expectedoutput