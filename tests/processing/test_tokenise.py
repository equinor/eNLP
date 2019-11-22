import pytest
import spacy

from enlp.processing.stdtools import tokenise


@pytest.fixture(scope="module")
def norwegian_language_model():
    return spacy.load('nb_dep_ud_sm')


@pytest.fixture(scope="module")
def english_language_model():
    return spacy.load('en_core_web_md')

# ENGLISH
@pytest.mark.parametrize("english_language_model,text,expectedoutput",
                         [pytest.param(english_language_model,
                                       'the quick brown fox jumped over the lazy dog',
                                       ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog'],
                                       id='en_test1_simple'),
                          pytest.param(english_language_model,
                                       'oak is strong and also gives shade',
                                       ['oak', 'is', 'strong', 'and', 'also', 'gives', 'shade'],
                                       id='en_test2_simple'),
                          ],
                         indirect=['english_language_model'],
                         )
def test_tokenise_en(english_language_model, text, expectedoutput):
    # arange - not needed

    # act
    list = tokenise(english_language_model, text)

    # assert
    assert list == expectedoutput


# NORWEGIAN
@pytest.mark.parametrize("norwegian_language_model,text,expectedoutput",
                         [pytest.param(norwegian_language_model,
                                       'den raske brune reven hoppet over den late hunden',
                                       ['den', 'raske', 'brune', 'reven', 'hoppet', 'over', 'den', 'late', 'hunden'],
                                       id='no_test1_simple'),
                          pytest.param(norwegian_language_model,
                                       'eiken er sterk og gir også skygge',
                                       ['eiken', 'er', 'sterk', 'og', 'gir', 'også', 'skygge'],
                                       id='no_test2_simple'),
                          ],
                         indirect=['norwegian_language_model'],
                         )
def test_tokenise_no(norwegian_language_model, text, expectedoutput):
    # arange - not needed

    # act
    list = tokenise(norwegian_language_model, text)

    # assert
    assert list == expectedoutput
