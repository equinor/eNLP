eNLP
====

This python library is a collection of common Natural Language Processing functions ranging from processing to
visualisation. The purpose of the package is to collect commonly used functions into a single location and provide a
simple approach for processing and understanding of textual data.

A number of example usages can be found in `eNLP gallery <https://cebirnie92.github.io/eNLP_docs/examples/index.html>`_,
whilst publications whose research used the package are detailed in the
`publications section <https://cebirnie92.github.io/eNLP_docs/publications.html>`_

Language Processing
-------------------
The library has functions for basic language processing, some homemade functions, for example for punctuation removal,
and other functions that leverage on the open-source packages of:

    - `NLTK <https://nltk.readthedocs.io/en/latest/>`_
    - `spaCy <https://spacy.io/>`_

These functions have been wrote such that they can be called individually or strung together to make a processing
pipeline. For example, to remove punctuation and perform a lemmatization of the remaining tokens, an NLP pipeline can be
set up as so,

.. code-block:: python

    from enlp.pipeline import NLPPipeline
    import spacy

    langmodel = spacy.load('en_core_web_md')
    text = "Some exciting text to be processed - ensure the language matches the spacy model"

    processed_text = NLPPipeline(langmodel, text)
    processed_text.rm_punctuation().spacy_lemmatize()

The processed  text can be accessed via

.. code-block:: python

    processed_text.text


Understanding
-------------

The library also has a number of functions for language understanding, such as word vector creation, sentiment analysis,
topic modelling and key word extraction. As well as the packages mentioned above, these functions leverage on the
open-source packages of:

    - `gensim <https://gensim.readthedocs.io/en/latest/>`_
    - `scikit-learn <https://scikit-learn.org/stable/>`_
    - `rake-nltk <https://csurfer.github.io/rake-nltk/_build/html/index.html>`_

Visualisation
-------------
Finally, functions are provided for visualisation - bar plots for visualisation alongside commonly used word clouds. As
well as the packages mentioned above, these functions leverage on the open-source packages of:

    - `wordcloud <https://amueller.github.io/word_cloud/index.html>`_


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Getting started:

   installation.rst
   design_decisions.rst
   examples/index.rst

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Reference documentation:

   api/index.rst

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Getting involved:

   Contributing      <contributing.rst>
   Credits           <credits.rst>
   Publications      <publications.rst>

