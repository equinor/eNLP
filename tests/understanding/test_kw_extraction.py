import pytest
import spacy

import enlp.understanding.keywords as kw
import enlp.processing.stdtools as stdt


def test_keyphrase_extraction():
    # arange
    example_text = './examples/example_data/en_historynlp.txt'
    with open(example_text, "r") as file:
        text = file.read()

    all_stopwords, stopwords_nb, stopwords_en = stdt.get_stopwords()

    # act
    keyphrases = kw.keyphrase_list(text,
                                      stopwords=stopwords_en,
                                      with_scores=False,
                                      )

    # assert
    assert keyphrases[0] == "word embeddings"
