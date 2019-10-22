"""
Contains functions for computing topics from a corpus and determining the topics of a sentence
"""

import gensim
import nltk
import pandas as pd


def bow_topic_modelling(docs, no_topics=10):
    """ LDA Topic Modelling with BoW

    Parameters
    ----------
    docs : :obj:`list`
        list of texts (documents)
    no_topics  : :obj:`int`
        number of topics to determine

    Returns
    -------
        bow_model : :obj:`gensim.model`
            topic model
        dictionary : :obj:`gensim dictionary`
            Bag-of-Words dictionary for corpus, important for determining topics of new documents
    """

    # MAKE DICTIONARY FROM CORPUS
    dictionary = gensim.corpora.Dictionary(nltk.word_tokenize(sentence) for sentence in docs)
    bow_corpus = [dictionary.doc2bow(doc) for doc in [nltk.word_tokenize(sentence) for sentence in docs]]

    bow_model = gensim.models.LdaMulticore(bow_corpus,
                                           num_topics=no_topics,
                                           id2word=dictionary)

    return bow_model, dictionary


def tfidf_topic_modelling(docs, no_topics=10):
    """ LDA Topic Modelling with TF-IDF

    Parameters
    ----------
    docs : :obj:`list`
        list of texts (documents)
    no_topics  : :obj:`int`
        number of topics to determine

    Returns
    -------
        tfidf_model : :obj:`gensim model`
            topic model
        dictionary : :obj:`gensim dictionary`
            Bag-of-Words dictionary for corpus, important for determining topics of new documents
    """

    # MAKE DICTIONARY FROM CORPUS
    dictionary = gensim.corpora.Dictionary(nltk.word_tokenize(sentence) for sentence in docs)
    bow_corpus = [dictionary.doc2bow(doc) for doc in [nltk.word_tokenize(sentence) for sentence in docs]]

    # Create tfidf corpus
    tfidf = gensim.models.TfidfModel(bow_corpus)
    tfidf_corpus = tfidf[bow_corpus]

    tfidf_model = gensim.models.LdaMulticore(tfidf_corpus,
                                             num_topics=no_topics,
                                             id2word=dictionary)

    return tfidf_model, dictionary


def print_topic_words(topic_model):
    """ Print words corresponding to topic modelling

    Parameters
    ----------
    topic_model : :obj:`gensim model`
            topic model

    Returns
    -------
        None
    """

    for idx, topic in topic_model.print_topics(-1):
        print ('Topic: {} \n Words: {}'.format(idx, topic))

    return None


def determine_topics(doc, topic_model, dictionary):
    """ determine document topics

    Determine topics of a document based on topics determined in topic modelling

    Parameters
    ----------
    docs : :obj:`str`
        document string
    topic_model : :obj:`gensim model`
        topic model
    dictionary : :obj:`gensim dictionary`
        Bag-of-Words dictionary for corpus, important for determining topics of new documents

    Returns
    -------
    topics_df : :obj:`pandas.DataFrame`
        dataframe of topic id and score

    """

    topics = topic_model.get_document_topics(bow=dictionary.doc2bow([doc]))
    topics_df = pd.DataFrame(topics, columns=['topic_no', 'score'])

    return topics_df