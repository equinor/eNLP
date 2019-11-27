"""
Contains functions for natural language processing
"""

import string
from nltk.stem.snowball import SnowballStemmer


def get_stopwords():
    """Get list of Norwegian and English stopwords.

    Get stopwords list from Spacy for Norwegian and English, returning each list separately as well as a combined list

    Returns
    -------
        stopwords : :obj:`list`
            lists of combination of Norwegian and English stopwords, Norwegian stopwords, English stopwords
        stops_nb : :obj:`list`
            lists of Norwegian stopwords
        stops_en : :obj:`list`
            lists of English stopwords

    Notes
    -----
    This has assumed both norwegian and english language models have been downloaded

    Examples
    --------
        >>> stopwords_all, stopwords_norwegian, stopwords_english = get_stopwords()
        >>> print(stopwords[:5])
        ['therein', 'neither', 'indeed', 'whereby', 'yourself']

    """

    from spacy.lang.en.stop_words import STOP_WORDS
    stops_en = list(STOP_WORDS)

    from spacy.lang.nb.stop_words import STOP_WORDS
    stops_nb = list(STOP_WORDS)

    stopwords = stops_en + stops_nb
    stopwords = [str(i) for i in stopwords]

    return stopwords, stops_nb, stops_en


def rm_stopwords(model, text, stopwords):
    """Remove stopwords from string.


    Parameters
    ----------
    model : :obj:`spacy.lang`
        SpaCy language model
    text : :obj:`str`
        text string on which to remove stopwords
    stopwords : :obj:`list`
       list of stopwords to remove

    Returns
    -------
        updated_text : :obj:`str`
            Updated version of input string with stopwords (and possibly punctuation) removed

    Notes
    -----
    String output is to allow piping between functions to return words as a list use: tokenise(rm_stopwords(...))

    Examples
    --------
        >>> import spacy
        >>> lang_mod = spacy.load('nb_dep_ud_sm')
        >>> text = 'Den raske brune reven hoppet over den late hunden.'
        >>> stopwords_all, stopwords_norwegian, stopwords_english = get_stopwords()
        >>> print (rm_stopwords(lang_mod, text, stopwords_all))
        raske brune reven hoppet late hunden.

    """

    # Remove stopwords
    tokens = [t.string.strip() for t in model(text) if t.string.lower().strip() not in stopwords]

    # Join string back together
    updated_text = ' '.join(tokens)

    # If not removing punctuation that retain original spacing around punctuation, i.e. 'end.' not 'end .'
    #updated_text = ' '.join(updated_text.split())
    updated_text = retain_spaces(updated_text)

    return updated_text


def rm_punctuation(model, text):
    """Return string free of punctuation

    Parameters
    ----------
    model : :obj:`spacy.lang`
        SpaCy language model
    text : :obj:`str`
        text string on which to remove stopwords

    Returns
    -------
        updated_text : :obj:`str`
            Updated version of input string where punctuation has been removed

    Notes
    -----
    String output is to allow piping between functions to return words as a list use: to_list(remove_punctuation(...))

    Examples
    --------
        >>> import spacy
        >>> lang_mod = spacy.load('en_core_web_md')
        >>> text = 'I better have passed that test - it is 90 percent of the class grade.'
        >>> print (rm_punctuation(lang_mod, text))
        I better have passed that test it is 90 percent of the class grade

    """
    tokens = [t.string.strip() for t in model(text) if t.string.lower().strip() not in string.punctuation]
    updated_text = ' '.join(tokens)
    return updated_text


def spacy_lemmatize(model, text):
    """Return string of lemmatized text

    Lemmatization is the process of reducing the different forms of a word to one single form, for example,
    reducing "builds", "building", or "built" to the lemma "build"

    Parameters
    ----------
    model : :obj:`spacy.lang`
        SpaCy language model
    text : :obj:`str`
        text string on which to remove stopwords

    Returns
    -------
        updated_text : :obj:`str`
            Updated version of input string where words have been lemmatized

    Notes
    -----
    String output is to allow piping between functions to return words as a list use: to_list(lemmatize(...))

    Examples
    --------
        >>> import spacy
        >>> lang_mod = spacy.load('nb_dep_ud_sm')
        >>> text = 'Den raske brune reven hoppet over den late hunden.'
        >>> print (spacy_lemmatize(lang_mod,text))
        'den rask brun rev hoppe over den lat hund.'

    """


    lemma_tx = [t.text if t.lemma_ == '-PRON-' else t.lemma_
          for t in model(text)
          ]

    updated_text = ' '.join(lemma_tx)
    updated_text = retain_spaces(updated_text)


    return updated_text


def nltk_stem_no(model, text):
    """Return string of stemmed text using NLTK's Norwegian snowball stemmer

    Stemming is a technique to remove affixes from a word, ending up with the stem.
    For example, the stem of cooking is cook.

    Parameters
    ----------
    model : :obj:`spacy.lang`
        SpaCy language model
    text : :obj:`str`
        text string on which to remove stopwords

    Returns
    -------
        updated_text : :obj:`str`
            Updated version of input string where words have been stemmed

    Notes
    -----
    String output is to allow piping between functions to return words as a list use: to_list(stem_norwegian(...))

    Examples
    --------
        >>> import spacy
        >>> lang_mod = spacy.load('nb_dep_ud_sm')
        >>> text = 'Den raske brune reven hoppet over den late hunden.'
        >>> print (nltk_stem_no(lang_mod,text))
        den rask brun rev hopp over den lat hund.

    """

    stemmer = SnowballStemmer("norwegian")

    stemmed_words = [stemmer.stem(t.string.strip()) for t in model(text)]


    updated_text = ' '.join(stemmed_words)
    updated_text = retain_spaces(updated_text)

    return updated_text


def tokenise(model,text):
    """Return list of tokens for a piece of text.

    A token is a string of contiguous characters between two spaces, or between a space and punctuation marks.
    A token can also be an integer, real, or a number with a colon (time, for example: 2:00).
    All other symbols are tokens themselves except apostrophes and quotation marks in a word (with no space),
    which in many cases symbolize acronyms or citations.

    Parameters
    ----------
    model : :obj:`spacy.lang`
        SpaCy language model
    text : :obj:`str`
        text string on which to remove stopwords

    Returns
    -------
        tokens : :obj:`list`
            List of tokens, list is ordered as tokens appear in sentence.

    Examples
    --------
        >>> import spacy
        >>> lang_mod = spacy.load('nb_dep_ud_sm')
        >>> text = 'Den raske brune reven hoppet over den late hunden.'
        >>> print (tokenise(lang_mod,text))
        ['Den', 'raske', 'brune', 'reven', 'hoppet', 'over', 'den', 'late', 'hunden', '.']

    """
    tokens = [t.string.strip() for t in model(text)]
    return tokens


def retain_spaces(processed):
    """Retaining spaces around punctuation at the end of a sentence

    Function for use when joining tokens and wishing to retain original spacing around punctuation.

    without function - lemma = 'the quick brown fox jump over the lazy dog .'

    with function - lemma = 'the quick brown fox jump over the lazy dog.'


    Parameters
    ----------
    processed : :obj:`str`
        processed text string

    Returns
    -------
        updated_text : :obj:`str`
            updated processed sentence to ensure same spacing around symbols as in original

    Notes
    -----
    Have only accounted for punctuation at the end of a sentence and not others, for example % or $ or # etc.

    Examples
    --------
        >>> tokens = ['Den', 'raske', 'brune', 'reven', 'hoppet', 'over', 'den', 'late', 'hunden', '.']
        >>> joined_tokens = ' '.join(tokens)
        >>> print ('Original: ', joined_tokens)
        >>> print ('Fixed spaces: ', retain_spaces(joined_tokens))
        Original:  Den raske brune reven hoppet over den late hunden .
        Fixed spaces:  Den raske brune reven hoppet over den late hunden.


    """

    i_to_rm = []
    char_list = [s for s in processed]

    for i, char in enumerate(processed):
        if i > 0 and char in ['.', '?', '!'] and processed[i - 1] == ' ':
            i_to_rm.append(i - 1)

    for index in sorted(i_to_rm, reverse=True):
        del char_list[index]

    # make new string removing blanks
    updated_text = ''.join(char_list)
    return updated_text
