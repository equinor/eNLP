"""
Class for piping functions for natural language processing
"""

from enlp.processing.stdtools import *
from enlp.understanding.linguistic import pos_tag


class NLPPipeline(object):
    """Pipeline class for combining functions from nlp_tools

    Attributes
    ----------
    model : :obj:`spacy.lang`
        SpaCy language model
    text : :obj:`str`
        text string on which to perform processing
    pos : :obj:`list`
        list of Parts-of-Speech tags
    tokens : :obj:`list`
        list of tokens

    """
    def __init__(self, model, text):
        """__init__ method of nlp_pipeline class

        Parameters
        ----------
        model : :obj:`spacy.lang`
            SpaCy language model
        text : :obj:`str`
            text string on which to perform processing

        """
        self.model = model
        self.text = text

    def rm_punctuation(self, **kwargs):
        """remove punctuation from text
        """
        self.text = rm_punctuation(self.model, self.text)
        return self

    def rm_stopwords(self, **kwargs):
        """remove stopwords from text

        Notes
        -----
        List of stopwords can be obtained from stdtools.get_stopwords()

        """
        self.text = rm_stopwords(self.model, self.text, stopwords=kwargs['stopwords'])
        return self

    def spacy_lemmatize(self):
        """lemmatise text
        """
        self.text = spacy_lemmatize(self.model, self.text)
        return self

    def nltk_stem_no(self):
        """stem text
        """
        self.text = nltk_stem_no(self.model, self.text)
        return self

    def pos_tag(self):
        """get part-of-speech tags
        """
        self.pos = pos_tag(self.model, self.text)
        return self

    def tokenise(self):
        """tokenise text
        """
        self.tokens = tokenise(self.model, self.text)
        return self