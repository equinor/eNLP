"""
Contains functions for linguistic features of natural language understanding
"""


def pos_tag(model, text):
    """Return parts-of-speech for words in a peice of text.

    Part-of-speech tagging is the process of marking up a word in a text (corpus) as corresponding to a particular
    part of speech, based on both its definition and its context. A simplified form of this is commonly taught to
    children, in the identification of words as nouns, verbs, adjectives, adverbs, etc.

    Parameters
    ----------
    model : :obj:`spacy.lang`
        SpaCy language model
    text : :obj:`str`
        text string on which to remove stopwords

    Returns
    -------
        tags : :obj:`list`
            List of part of speech tags, list is ordered as tokens appear in sentence.

    Notes
    -----
    To get direct linking with words corresponding to tags use tokenise function to get word list in same order as PoS tags.

    Example
    -------
        >>> import spacy
        >>> import enlp.processing.stdtools as stdt
        >>> lang_mod = spacy.load('nb_dep_ud_sm')
        >>> text = 'Den raske brune reven hoppet over den late hunden.'
        >>> word_list = stdt.tokenise(lang_mod,text)
        >>> print (pos_tag(lang_mod,text))
        ['DET', 'ADJ', 'ADJ', 'NOUN', 'VERB', 'ADP', 'DET', 'ADJ', 'NOUN', 'PUNCT']

    """
    tags = [t.pos_ for t in model(text.lower())]
    return tags
