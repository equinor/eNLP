import pytest
import spacy

from enlp.processing.stdtools import tokenise, retain_spaces


@pytest.fixture(scope="module")
def english_language_model():
    return spacy.load('en_core_web_md')


# TESTS - removing space at end of sentence before punctuation point
@pytest.mark.parametrize("langModel,text,expectedOutput", [
    pytest.param(english_language_model(),
                 'This is my first sentence. This is my second sentence.',
                 'This is my first sentence. This is my second sentence.',
                 id='retainspaces_doublesent'),
    pytest.param(english_language_model(),
                 'How does the retain sentences function handle question marks?',
                 'How does the retain sentences function handle question marks?',
                 id='retainspaces_questionmark'),
    pytest.param(english_language_model(),
                 'I am 1.76 meters tall.',
                 'I am 1.76 meters tall.',
                 id='retainspaces_realnumber'),
    pytest.param(english_language_model(),
                 'Woohoo! The tests are running!',
                 'Woohoo! The tests are running!',
                 id='retainspaces_exclamationmark'),
])
def test_retainspaces(langModel, text, expectedOutput):
    # arange - not needed

    # act
    tokens = tokenise(langModel, text)
    raw_str = ' '.join(tokens)
    new_text = retain_spaces(raw_str)

    # assert
    assert new_text == expectedOutput
