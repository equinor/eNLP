"""
Contains functions for generating & saving custom spacy language models
"""
import spacy

def add_vectors_to_langmod(wvs, mod_lang):
    """ Add word vectors to language model

    Parameters
    ----------
    wvs : :obj:`gensim model`
        Trained word vector model
    mod_lang  : :obj:`str`
        language of model to be created

    Returns
    -------
        nlp : :obj:`spacy.lang`
            SpaCy language model with new word vectors incorporated
    """

    # Init blank spacy nlp object
    nlp = spacy.blank(mod_lang)

    # Loop through range of all indexes, get words associated with each index.
    keys = []
    for idx in range(len(wvs.index2word)):
        keys.append(wvs.index2word[idx])

    # Set the vectors for our nlp object to the google news vectors
    nlp.vocab.vectors = spacy.vocab.Vectors(data=wvs.syn0, keys=keys)

    return nlp


def save_spacy_model(model, path):
    """ Save spacy model to file

    Parameters
    ----------
    model : :obj:`spacy.lang`
        SpaCy language model
    path  : :obj:`str`
        file path to save model

    Returns
    -------
    """

    model.to_disk(path)

    return None