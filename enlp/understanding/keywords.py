"""
Contains functions for keyword extraction
"""

from rake_nltk import Rake
import string


def keyphrase_list(text,
                   language = 'english',
                   stopwords = [],
                   min_phrase_len=1,
                   max_phrase_len=2,
                   with_scores = True):
    """Extract keywords from a piece of text

    Parameters
    ----------
    text : :obj:`str`
        text string from which to extract keywords
    language : :obj:`str`
        language of text, must work with nltk
    stopwords : :obj:`list`
       list of stopwords to consider when extracting keywords
    min_phrase_len : :obj:`int`
        minimum token length key phrase can be
    max_phrase_len : :obj:`int`
        maximum token length key phrase can be
    with_scores : :obj:`bool`
        whether to return phrases with score or not, default is True



    Returns
    -------
        r : :obj:`list`
            List of keyphrases


    """

    # Create rake object
    r = Rake(language = language,
             stopwords = stopwords,
             punctuations = string.punctuation,
             min_length = min_phrase_len,
             max_length = max_phrase_len
             )

    r.extract_keywords_from_text(text)

    if with_scores:
        return r.rank_list
    else:
        return r.ranked_phrases





