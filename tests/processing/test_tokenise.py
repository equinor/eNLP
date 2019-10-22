import pytest
import spacy

from enlp.processing.stdtools import tokenise


@pytest.fixture(scope="module")
def norwegian_language_model():
    return spacy.load('nb_dep_ud_sm')

@pytest.fixture(scope="module")
def english_language_model():
    return spacy.load('en_core_web_md')


# SIMPLE TESTS - lower case, no punctuation, no numbers
@pytest.mark.parametrize("langModel,text,expectedOutput", [
    pytest.param(english_language_model(),
                 'the quick brown fox jumped over the lazy dog',
                 ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog'],
                 id='en_test1_simple'),
    pytest.param(english_language_model(),
                 'oak is strong and also gives shade',
                 ['oak', 'is', 'strong', 'and', 'also', 'gives', 'shade'],
                 id='en_test2_simple'),
    pytest.param(norwegian_language_model(),
                 'den raske brune reven hoppet over den late hunden',
                 ['den', 'raske', 'brune', 'reven', 'hoppet', 'over', 'den', 'late', 'hunden'],
                 id='no_test1_simple'),
    pytest.param(norwegian_language_model(),
                 'eiken er sterk og gir også skygge',
                 ['eiken', 'er', 'sterk', 'og', 'gir', 'også', 'skygge'],
                 id='no_test2_simple'),
])
def test_tokenise_simple(langModel, text, expectedOutput):
    # arange - not needed

    # act
    list = tokenise(langModel, text)

    # assert
    assert list == expectedOutput
