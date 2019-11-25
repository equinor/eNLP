"""
Contains functions for sentiment analysis
"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

def vader_sentiment_strength(textlist):
    """Compute sentiment strength of ENGLISH texts

    Using the nltk implementation of the VADER approach devised by: Hutto, C.J. & Gilbert, E.E. (2014).
    VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International
    Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

    Parameters
    ----------
    textlist : :obj:`list`
        list of text strings, each of which are to be analysed

    Returns
    -------
        polarity_scores : :obj:`pandas.DataFrame`
            Dataframe of the polarity score - positive values are positive valence, negative value are negative
            valence. See cited paper for more details on scoring


    Example
    -------
        >>> positive_text = 'I love your carefree nature.'
        >>> negative_text = 'I abhor hostility.'
        >>> textlist = [positive_text, negative_text]
        >>> print (vader_sentiment_strength(textlist))
        compound  negative  neutral  positive                          text
        0    0.7845       0.0    0.225     0.775  I love your carefree nature.
        1   -0.7579       1.0    0.000     0.000            I abhor hostility.

    """
    sid = SentimentIntensityAnalyzer()

    result_dicts = []
    for text in textlist:
        # print(text)
        ss = sid.polarity_scores(text)
        result = {'text': text,
                  'positive': ss['pos'],
                  'negative': ss['neg'],
                  'neutral': ss['neu'],
                  'compound': ss['compound']
                  }
        result_dicts.append(result)

    polarity_scores = pd.DataFrame(result_dicts)

    return polarity_scores
