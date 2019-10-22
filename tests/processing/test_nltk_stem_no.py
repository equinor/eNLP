import pytest

from enlp.processing.stdtools import nltk_stem_no
import spacy


@pytest.fixture(scope="module")
def norwegian_language_model():
    return spacy.load('nb_dep_ud_sm')


# SIMPLE TESTS - lower case, no numbers
@pytest.mark.parametrize("langModel,text,expectedOutput", [
    pytest.param(norwegian_language_model(),
                 'den raske brune reven hoppet over den late hunden',
                 "den rask brun rev hopp over den lat hund",
                 id='no_test1_simple'),
    pytest.param(norwegian_language_model(),
                 'eiken er sterk og gir også skygge',
                 "eik er sterk og gir også skygg",
                 id='no_test2_simple'),
])

def test_stemming_simple(langModel, text, expectedOutput):
    # arange - not needed

    # act
    stemmed_text = nltk_stem_no(langModel, text)

    # assert
    assert stemmed_text == expectedOutput


# COMPLEX TESTS - mixed case, punctuation, numbers
@pytest.mark.parametrize("langModel,text,expectedOutput", [
    pytest.param(norwegian_language_model(),
                 'Katter og hunder hater hverandre.',
                 "katt og hund hat hverandr.",
                 id='no_test1_complex'),
    pytest.param(norwegian_language_model(),
                 'Krana tåler maks 100 kilo.',
                 "kran tål maks 100 kilo.",
                 id='no_test2_complex'),
])
def test_stemming_complex(langModel, text, expectedOutput):
    # arange - not needed

    # act
    stemmed_text = nltk_stem_no(langModel, text)

    # assert
    assert stemmed_text == expectedOutput