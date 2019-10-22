"""
Contains functions for visualisation of text
"""

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


def freq_dist(tokens):
    """ Count frequency of tokens

    Parameters
    ----------
    tokens : :obj:`list`
        list of tokens to be analysed, note these may include punctuation

    Returns
    -------
        count : :obj:`list`
            sorted list of words and their respective frequency, i.e. list of tuples (word,count)

    Notes
    -----
    If words are originally in string format use stdtools.tokenise() to convert to input format

    Examples
    --------
        >>> words=['aa','sd','re','aa','er','hg','sd','le','ot','tr','tr']
        >>> print(freq_dist(words)[:5]) # top 5 words
        [('aa', 2), ('sd', 2), ('tr', 2), ('re', 1), ('er', 1)]
    """

    fdist = nltk.FreqDist(tokens)
    count = fdist.most_common(len(tokens))

    return count


def compute_tfidf(text_list, doc_ids=None):
    """ Compute tfidf

    Parameters
    ----------
    text_list : :obj:`list`
        list of texts (documents)
    doc_ids : :obj:`list`
        list of document ids for indexing results

    Returns
    -------
        scores : :obj:`pandas.DataFrame`
            pandas dataframe where every word is a feature and every document is an observation

    Notes
    -----
    For a large corpus or a large number of documents it is better to use the scikit-learn transformer directly
    to take advantage of the sparse matrix procedures


    """

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(text_list)

    words = vectorizer.get_feature_names()
    doc_dicts = []

    for i, doc_scores in enumerate(X):
        doc_dict = dict()
        for w_i, w_v in enumerate(doc_scores.toarray()[0]):
            doc_dict.update({words[w_i]: w_v})
        doc_dicts.append(doc_dict)

    scores = pd.DataFrame(doc_dicts)

    if doc_ids:
        scores.index = doc_ids

    return scores


def important_words_per_corpus(scores, n=10):
    """ Based on tfidf scores, return most important words per corpus

    Parameters
    ----------
    scores : :obj:`pandas.DataFrame`
            pandas dataframe where every word is a feature and every document is an observation, computed
            by compute_tfidf method
    n  : :obj:`int`
        number of important words to return

    Returns
    -------
    imp_words : :obj:`list`
        list of tuples of important word and their average tfidf score across the corpus

    """

    imp_words = scores.mean().sort_values(ascending=False)[:20]

    return imp_words


def important_words_per_doc(scores, doc_id=None, n=5):
    """ Based on tfidf scores, return most important words per document

        Parameters
        ----------
        scores : :obj:`pandas.DataFrame`
                pandas dataframe where every word is a feature and every document is an observation, computed
                by compute_tfidf method
        doc_ids : :obj:`list`
            list of document ids for indexing results, default is to compute for all documents

        Returns
        -------
        imp_words : :obj:`list`
            list of doc lists where doc list contains tuples of important word and its score in the document

        """
    if not doc_id:
        doc_id = list(scores.index)

    imp_words = []
    for d_id in doc_id:
        #print('Document: %s' % str(d_id))
        doc_scores = scores.loc[d_id].sort_values(ascending=False)

        d_imp_words = []

        for k, v in doc_scores[:n].iteritems():
            d_imp_words.append((k, v)
                               )
        imp_words.append(d_imp_words)

    return imp_words
