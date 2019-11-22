import pytest

# Explicitly set path so don't need to run setup.py - if we have multiple copies of the code we would otherwise need
# to setup a separate environment for each to ensure the code pointers are correct.
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from enlp.understanding.linguistic import pos_tag

import spacy


@pytest.fixture(scope="module")
def norwegian_language_model():
    return spacy.load('nb_dep_ud_sm')


@pytest.fixture(scope="module")
def english_language_model():
    return spacy.load('en_core_web_md')


def test_pos_tag_simple(english_language_model):

    # arange
    text = 'the quick brown fox jumped over the lazy dog'
    model = english_language_model

    # act
    tags = pos_tag(model,text)

    # assert
    assert tags == ['DET', 'ADJ', 'ADJ', 'NOUN', 'VERB', 'ADP', 'DET', 'ADJ', 'NOUN']


# ENGLISH
@pytest.mark.parametrize("english_language_model,text,expectedoutput",
                          [pytest.param(english_language_model,
                                        "The quick brown fox jumped over the lazy dog.",
                                        ['DET', 'ADJ', 'ADJ', 'NOUN', 'VERB', 'ADP', 'DET', 'ADJ', 'NOUN', 'PUNCT'],
                                        id='en_test_1'),
                           pytest.param(english_language_model,
                                        "It was a tiring day, so tiring he fell asleep on the train and missed his stop.",
                                        ['PRON', 'VERB', 'DET', 'ADJ', 'NOUN', 'PUNCT', 'ADV', 'ADJ', 'PRON', 'VERB',
                                         'ADJ', 'ADP', 'DET','NOUN', 'CCONJ', 'VERB', 'ADJ', 'NOUN', 'PUNCT'],
                                        id='en_test_2'),
                           pytest.param(english_language_model,
                                        "I better have passed that test - it is 90 percent of the class grade.",
                                        ['PRON', 'ADV', 'VERB', 'VERB', 'DET', 'NOUN', 'PUNCT', 'PRON', 'VERB', 'NUM',
                                         'NOUN', 'ADP', 'DET','NOUN', 'NOUN', 'PUNCT'],
                                        id='en_test_3'),
                           ],
                         indirect=['english_language_model'],
                         )
def test_pos_tag_en(english_language_model, text, expectedoutput):
    """
    tests that account for:
        - punctuation
        - pronouns
        - capital letters
    """

    # arange - no arange necessary

    # act
    tags = pos_tag(english_language_model, text)

    # assert
    assert tags == expectedoutput


# NORWEGIAN
@pytest.mark.parametrize("norwegian_language_model,text,expectedoutput",
                          [pytest.param(norwegian_language_model,
                                        "Den raske brune reven hoppet over den late hunden.",
                                        ['DET', 'ADJ', 'ADJ', 'NOUN', 'VERB', 'ADP', 'DET', 'ADJ', 'NOUN', 'PUNCT'],
                                        id='no_test_1'),
                           pytest.param(norwegian_language_model,
                                        "Han hadde vært uforsiktig og skåret seg i fingeren.",
                                        ['PRON', 'AUX', 'AUX', 'ADJ', 'CCONJ', 'VERB', 'PRON', 'ADP', 'NOUN', 'PUNCT'],
                                        id='no_test_2'),
                           pytest.param(norwegian_language_model,
                                        "Krana tåler maks 100 kilo.",
                                        ['NOUN', 'VERB', 'ADJ', 'NUM', 'NOUN', 'PUNCT'],
                                        id='no_test_3'),
                           ],
                         indirect=['norwegian_language_model'],
                         )
def test_pos_tag_no(norwegian_language_model, text, expectedoutput):
    """
    tests that account for:
        - punctuation
        - pronouns
        - capital letters
    """

    # arange - no arange necessary

    # act
    tags = pos_tag(norwegian_language_model, text)

    # assert
    assert tags == expectedoutput
#
