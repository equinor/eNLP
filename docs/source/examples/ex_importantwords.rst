.. note::
    :class: sphx-glr-download-link-note

    Click :ref:`here <sphx_glr_download_examples_ex_importantwords.py>` to download the full example code
.. rst-class:: sphx-glr-example-title

.. _sphx_glr_examples_ex_importantwords.py:


TF-IDF Important Words
======================
The following example compute tf-idf of words in a document to determine the most important words.

NOTE: This is an example to show how to run the procedure however due to the small dataset used
the results are likely to be non-sensical.


.. code-block:: default


    import enlp.understanding.distributions as dists
    import enlp.processing.stdtools as stdt
    import spacy







Load example text


.. code-block:: default


    with open("example_data/en_historynlp.txt", "r") as file:
        text=file.read()







Preprocess text - for this example we have a very small corpus to allow the documentation
to build therefore we will split the single document into paragraphs for processing to
imitate multiple document input and we will also remove stopwords as the text is too small
for the tf-idf computation to handle them. For normal procedures you should NOT remove stopwords
prior to computing tf-idf scores.


.. code-block:: default


    # Split text into paragraphs to imitate documents
    paragraphs = text.split('\n\n')
    # Remove \n and replace with space
    paragraphs = [p.replace('\n',' ') for p in paragraphs]

    # Because example text is small, remove stopwords as they'll influence tf-idf scores
    en = spacy.load('en_core_web_md')
    stopwords, stops_nb, stops_en = stdt.get_stopwords()
    paragraphs = [stdt.rm_stopwords(en, p, stops_en) for p in paragraphs]








Compute tf-idf scores and determine most important words across full corpus


.. code-block:: default


    scores = dists.compute_tfidf(paragraphs)
    print (dists.important_words_per_corpus(scores))





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    translation     0.106192
    language        0.104992
    machine         0.097584
    systems         0.084293
    learning        0.073622
    natural         0.073411
    data            0.072888
    processing      0.069336
    annotated       0.060897
    research        0.057194
    models          0.054165
    intelligence    0.047994
    turing          0.047994
    eliza           0.047706
    developed       0.046281
    statistical     0.046008
    results         0.043832
    algorithms      0.041982
    real            0.040207
    written         0.039370
    dtype: float64



Determine most important words per document (or for this example, per paragraph)


.. code-block:: default

    iw_p_d = dists.important_words_per_doc(scores)

    for i, iw in enumerate(iw_p_d):
        print ('Paragraph %i important words: ' %int(i+1))
        print (iw)



.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    Paragraph 1 important words: 
    [('intelligence', 0.3839490826316703), ('turing', 0.3839490826316703), ('1950', 0.19197454131583516), ('published', 0.19197454131583516), ('criterion', 0.19197454131583516)]
    Paragraph 2 important words: 
    [('translation', 0.4934936045135249), ('machine', 0.3461480988917147), ('research', 0.17307404944585736), ('automatic', 0.13647639974751505), ('report', 0.13647639974751505)]
    Paragraph 3 important words: 
    [('eliza', 0.38165016476739877), ('human', 0.2544334431782659), ('head', 0.2544334431782659), ('hurts', 0.2544334431782659), ('restricted', 0.2544334431782659)]
    Paragraph 4 important words: 
    [('lehnert', 0.30226595960857494), ('1978', 0.30226595960857494), ('politics', 0.15113297980428747), ('conceptual', 0.15113297980428747), ('units', 0.15113297980428747)]
    Paragraph 5 important words: 
    [('models', 0.3292843790366923), ('language', 0.2989594688746548), ('processing', 0.24913289072887895), ('rules', 0.2357425166457776), ('input', 0.19757062742201537)]
    Paragraph 6 important words: 
    [('systems', 0.3483663777692584), ('corpora', 0.24826980544342042), ('result', 0.24826980544342042), ('translation', 0.17954688342718525), ('developed', 0.17954688342718525)]
    Paragraph 7 important words: 
    [('annotated', 0.48717309177353224), ('data', 0.30890696094816483), ('supervised', 0.24358654588676612), ('non', 0.24358654588676612), ('algorithms', 0.20414453611150032)]
    Paragraph 8 important words: 
    [('language', 0.25791453933888686), ('neural', 0.24405216992987602), ('deep', 0.24405216992987602), ('machine', 0.2063316314711095), ('learning', 0.2063316314711095)]




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  10.994 seconds)


.. _sphx_glr_download_examples_ex_importantwords.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download

     :download:`Download Python source code: ex_importantwords.py <ex_importantwords.py>`



  .. container:: sphx-glr-download

     :download:`Download Jupyter notebook: ex_importantwords.ipynb <ex_importantwords.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
