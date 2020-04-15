import pytest

from enlp.processing.stdtools import nltk_stem_no
import spacy


@pytest.fixture(scope="module")
def norwegian_language_model():
    return spacy.load('nb_dep_ud_sm')


# SIMPLE TESTS - lower case, no numbers
@pytest.mark.parametrize("norwegian_language_model,text,expectedoutput",
                         [pytest.param(norwegian_language_model,
                                       'den raske brune reven hoppet over den late hunden',
                                       "den rask brun rev hopp over den lat hund",
                                       id='no_test1_simple'),
                          pytest.param(norwegian_language_model,
                                       'eiken er sterk og gir også skygge',
                                       "eik er sterk og gir også skygg",
                                       id='no_test2_simple'),
                          ],
                         indirect=['norwegian_language_model'],
                         )

def test_stemming_simple(norwegian_language_model, text, expectedoutput):
    # arange - not needed

    # act
    stemmed_text = nltk_stem_no(norwegian_language_model, text)

    # assert
    assert stemmed_text == expectedoutput


# COMPLEX TESTS - mixed case, punctuation, numbers
@pytest.mark.parametrize("norwegian_language_model,text,expectedoutput",
                         [pytest.param(norwegian_language_model,
                                       'Katter og hunder hater hverandre.',
                                       "katt og hund hat hverandr.",
                                       id='no_test1_complex'),
                          pytest.param(norwegian_language_model,
                                       'Krana tåler maks 100 kilo.',
                                       "kran tål maks 100 kilo.",
                                       id='no_test2_complex'),
                          ],
                         indirect=['norwegian_language_model'],
                         )
def test_stemming_complex(norwegian_language_model, text, expectedoutput):
    # arange - not needed

    # act
    stemmed_text = nltk_stem_no(norwegian_language_model, text)

    # assert
    assert stemmed_text == expectedoutput