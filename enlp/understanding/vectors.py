"""
Contains functions for computing & analysing word and document vectors
"""

import gensim
import nltk


def word_vectors(docs, sg=0, mc=0, sz=300, wnd=5, epochs=10):
    """ Compute word vectors from corpus


    Parameters
    ----------
    docs : :obj:`list`
        list of texts (documents)
    sg  : :obj:`int`
        Training algorithm: 1 for skip-gram; otherwise CBOW.
    mc  : :obj:`int`
        Ignores all words with total frequency lower than this.
    sz  : :obj:`int`
        Dimensionality of the word vectors.
    wnd  : :obj:`int`
        Maximum distance between the current and predicted word within a sentence.
    epochs  : :obj:`int`
        number of epochs for training

    Returns
    -------
        wvs : :obj:`gensim.model`
            Trained word vector model
    """
    tokenised_sents = [nltk.word_tokenize(sent) for sent in docs]

    wvs = gensim.models.Word2Vec(tokenised_sents, sg=sg, min_count=mc, size=sz, window=wnd)
    wvs.train(tokenised_sents, total_examples=len(tokenised_sents), epochs=epochs)

    return wvs


def similar_words(wvs, word, n=10):
    """ Find similar words to word


    Parameters
    ----------
    word : :obj:`str`
        word to find most similar vectors, note it must be within vocabulary
    wvs : :obj:`gensim.model`
        Trained word vector model
    n  : :obj:`int`
        Number of similar words to return.

    Returns
    -------
        most_similar : :obj:`list`
            list of most similar words and their distance
    """
    most_similar = wvs.wv.most_similar(positive=word, topn=n)

    return most_similar


def vector_maths(wvs, pwords=None, nwords=None, n=1):
    """ Perform word vector maths


    Parameters
    ----------
    wvs : :obj:`gensim.model`
        Trained word vector model
    pwords : :obj:`list`
        list of positive words
    nwords : :obj:`list`
        list of negative words
    n  : :obj:`int`
        Number of close words to return.

    Returns
    -------
        most_similar : :obj:`list`
            list of most similar words and their distance
    """

    most_similar = wvs.wv.most_similar(positive = pwords,
                                       negative = nwords,
                                       topn=n)
    return most_similar


def save_vectors(wvs, fname, binary=True):
    """ Save word vector model to file

    Parameters
    ----------
    wvs : :obj:`gensim.model`
        Trained word vector model
    fname : :obj:`snr`
        Filename
    binary : :obj:`bool`
        save as binary

    Returns
    -------
    """

    wvs.wv.save_word2vec_format(fname, binary=binary)

    return None


def load_vectors(fname, binary=True):
    """ Load word vector model from file

    Parameters
    ----------
    fname : :obj:`snr`
        Filename
    binary : :obj:`bool`
        was model saved in binary format

    Returns
    -------
    wvs : :obj:`gensim.model`
        Word vector model

    """

    wvs = gensim.models.KeyedVectors.load_word2vec_format(fname, binary=binary)

    return wvs

