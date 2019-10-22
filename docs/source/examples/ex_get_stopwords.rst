.. note::
    :class: sphx-glr-download-link-note

    Click :ref:`here <sphx_glr_download_examples_ex_get_stopwords.py>` to download the full example code
.. rst-class:: sphx-glr-example-title

.. _sphx_glr_examples_ex_get_stopwords.py:


Removing Stopwords
==================
XXX


.. code-block:: default


    # Import necessary packages
    from enlp.processing.stdtools import get_stopwords, rm_stopwords, tokenise
    import enlp.understanding.distributions as dists
    import spacy
    import pandas as pd

    import matplotlib.pyplot as plt
    plt.close('all') # very important for read the docs to avoid it crashing due to memory








Load text to be processed and the appropriate language model


.. code-block:: default


    # Load text file
    with open("example_data/en_historynlp.txt", "r") as file:
        text=file.read()
    print (text)

    # Load spacy language model
    langmodel = spacy.load('en_core_web_md')






.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    The history of natural language processing generally started in the 1950s, although work can be found from earlier
    periods. In 1950, Alan Turing published an article titled "Computing Machinery and Intelligence" which proposed what is
    now called the Turing test as a criterion of intelligence.

    The Georgetown experiment in 1954 involved fully automatic translation of more than sixty Russian sentences into
    English. The authors claimed that within three or five years, machine translation would be a solved problem.[2]
    However, real progress was much slower, and after the ALPAC report in 1966, which found that ten-year-long research had
    failed to fulfill the expectations, funding for machine translation was dramatically reduced. Little further research
    in machine translation was conducted until the late 1980s, when the first statistical machine translation systems were
    developed.

    Some notably successful natural language processing systems developed in the 1960s were SHRDLU, a natural language
    system working in restricted "blocks worlds" with restricted vocabularies, and ELIZA, a simulation of a Rogerian
    psychotherapist, written by Joseph Weizenbaum between 1964 and 1966. Using almost no information about human thought or
    emotion, ELIZA sometimes provided a startlingly human-like interaction. When the "patient" exceeded the very small
    knowledge base, ELIZA might provide a generic response, for example, responding to "My head hurts" with "Why do you say
    your head hurts?".

    During the 1970s, many programmers began to write "conceptual ontologies", which structured real-world information into
    computer-understandable data. Examples are MARGIE (Schank, 1975), SAM (Cullingford, 1978), PAM (Wilensky, 1978),
    TaleSpin (Meehan, 1976), QUALM (Lehnert, 1977), Politics (Carbonell, 1979), and Plot Units (Lehnert 1981). During this
    time, many chatterbots were written including PARRY, Racter, and Jabberwacky.

    Up to the 1980s, most natural language processing systems were based on complex sets of hand-written rules. Starting in
    the late 1980s, however, there was a revolution in natural language processing with the introduction of machine
    learning algorithms for language processing. This was due to both the steady increase in computational power (see
    Moore's law) and the gradual lessening of the dominance of Chomskyan theories of linguistics (e.g. transformational
    grammar), whose theoretical underpinnings discouraged the sort of corpus linguistics that underlies the machine-
    learning approach to language processing.[3] Some of the earliest-used machine learning algorithms, such as decision
    trees, produced systems of hard if-then rules similar to existing hand-written rules. However, part-of-speech tagging
    introduced the use of hidden Markov models to natural language processing, and increasingly, research has focused on
    statistical models, which make soft, probabilistic decisions based on attaching real-valued weights to the features
    making up the input data. The cache language models upon which many speech recognition systems now rely are examples of
    such statistical models. Such models are generally more robust when given unfamiliar input, especially input that
    contains errors (as is very common for real-world data), and produce more reliable results when integrated into a
    larger system comprising multiple subtasks.

    Many of the notable early successes occurred in the field of machine translation, due especially to work at IBM
    Research, where successively more complicated statistical models were developed. These systems were able to take
    advantage of existing multilingual textual corpora that had been produced by the Parliament of Canada and the European
    Union as a result of laws calling for the translation of all governmental proceedings into all official languages of
    the corresponding systems of government. However, most other systems depended on corpora specifically developed for the
    tasks implemented by these systems, which was (and often continues to be) a major limitation in the success of these
    systems. As a result, a great deal of research has gone into methods of more effectively learning from limited amounts
    of data.

    Recent research has increasingly focused on unsupervised and semi-supervised learning algorithms. Such algorithms are
    able to learn from data that has not been hand-annotated with the desired answers, or using a combination of annotated
    and non-annotated data. Generally, this task is much more difficult than supervised learning, and typically produces
    less accurate results for a given amount of input data. However, there is an enormous amount of non-annotated data
    available (including, among other things, the entire content of the World Wide Web), which can often make up for the
    inferior results if the algorithm used has a low enough time complexity to be practical.

    In the 2010s, representation learning and deep neural network-style machine learning methods became widespread in
    natural language processing, due in part to a flurry of results showing that such techniques[4][5] can achieve state-of
    -the-art results in many natural language tasks, for example in language modeling,[6] parsing,[7][8] and many others.
    Popular techniques include the use of word embeddings to capture semantic properties of words, and an increase in
    end-to-end learning of a higher-level task (e.g., question answering) instead of relying on a pipeline of separate
    intermediate tasks (e.g., part-of-speech tagging and dependency parsing). In some areas, this shift has entailed
    substantial changes in how NLP systems are designed, such that deep neural network-based approaches may be viewed as a
    new paradigm distinct from statistical natural language processing. For instance, the term neural machine translation
    (NMT) emphasizes the fact that deep learning-based approaches to machine translation directly learn sequence-to-sequence
    transformations, obviating the need for intermediate steps such as word alignment and language modeling that were used
    in statistical machine translation (SMT).




Get stopwords: the stopwords function will get all english and norwegian stopwords


.. code-block:: default


    stopwords_func, stopwords_nb_func, stopwords_en_func = get_stopwords()
    print (stopwords_en_func[:5])





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    ['take', 'except', 'using', 'ca', 'from']



Remove english stopwords


.. code-block:: default


    processed_text = rm_stopwords(langmodel, text, stopwords_en_func)
    print (processed_text)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    history natural language processing generally started 1950s , work found earlier  periods. 1950 , Alan Turing published article titled " Computing Machinery Intelligence " proposed  called Turing test criterion intelligence.  Georgetown experiment 1954 involved fully automatic translation Russian sentences  English. authors claimed years , machine translation solved problem.[2 ]  , real progress slower , ALPAC report 1966 , found - year - long research  failed fulfill expectations , funding machine translation dramatically reduced. Little research  machine translation conducted late 1980s , statistical machine translation systems  developed.  notably successful natural language processing systems developed 1960s SHRDLU , natural language  system working restricted " blocks worlds " restricted vocabularies , ELIZA , simulation Rogerian  psychotherapist , written Joseph Weizenbaum 1964 1966. information human thought  emotion , ELIZA provided startlingly human - like interaction. " patient " exceeded small  knowledge base , ELIZA provide generic response , example , responding " head hurts " "  head hurts? ".  1970s , programmers began write " conceptual ontologies " , structured real - world information  computer - understandable data. Examples MARGIE ( Schank , 1975 ) , SAM ( Cullingford , 1978 ) , PAM ( Wilensky , 1978 ) ,  TaleSpin ( Meehan , 1976 ) , QUALM ( Lehnert , 1977 ) , Politics ( Carbonell , 1979 ) , Plot Units ( Lehnert 1981 ).  time , chatterbots written including PARRY , Racter , Jabberwacky.  1980s , natural language processing systems based complex sets hand - written rules. Starting  late 1980s , , revolution natural language processing introduction machine  learning algorithms language processing. steady increase computational power (  Moore 's law ) gradual lessening dominance Chomskyan theories linguistics ( e.g. transformational  grammar ) , theoretical underpinnings discouraged sort corpus linguistics underlies machine-  learning approach language processing.[3 ] earliest - machine learning algorithms , decision  trees , produced systems hard - rules similar existing hand - written rules. , - - speech tagging  introduced use hidden Markov models natural language processing , increasingly , research focused  statistical models , soft , probabilistic decisions based attaching real - valued weights features  making input data. cache language models speech recognition systems rely examples  statistical models. models generally robust given unfamiliar input , especially input  contains errors ( common real - world data ) , produce reliable results integrated  larger system comprising multiple subtasks.  notable early successes occurred field machine translation , especially work IBM  Research , successively complicated statistical models developed. systems able  advantage existing multilingual textual corpora produced Parliament Canada European  Union result laws calling translation governmental proceedings official languages  corresponding systems government. , systems depended corpora specifically developed  tasks implemented systems , ( continues ) major limitation success  systems. result , great deal research gone methods effectively learning limited amounts  data.  Recent research increasingly focused unsupervised semi - supervised learning algorithms. algorithms  able learn data hand - annotated desired answers , combination annotated  non - annotated data. Generally , task difficult supervised learning , typically produces  accurate results given input data. , enormous non - annotated data  available ( including , things , entire content World Wide Web ) ,  inferior results algorithm low time complexity practical.  2010s , representation learning deep neural network - style machine learning methods widespread  natural language processing , flurry results showing techniques[4][5 ] achieve state -  -the - art results natural language tasks , example language modeling,[6 ] parsing,[7][8 ].  Popular techniques include use word embeddings capture semantic properties words , increase  end - - end learning higher - level task ( e.g. , question answering ) instead relying pipeline separate  intermediate tasks ( e.g. , - - speech tagging dependency parsing ). areas , shift entailed  substantial changes NLP systems designed , deep neural network - based approaches viewed  new paradigm distinct statistical natural language processing. instance , term neural machine translation  ( NMT ) emphasizes fact deep learning - based approaches machine translation directly learn sequence - - sequence  transformations , obviating need intermediate steps word alignment language modeling  statistical machine translation ( SMT ). 



Now that the stopwords have been removed then the sentences no longer make much sense. Therefore, an alternative to
viewing the text output is to look at the distribution of the remaining text


.. code-block:: default



    orig_top10 = pd.DataFrame(dists.freq_dist(tokenise(langmodel, text)), columns=['token', 'count'])
    pr_top10 = pd.DataFrame(dists.freq_dist(tokenise(langmodel, processed_text)), columns=['token', 'count'])

    print ("ORIGINAL - top 10 words")
    print (orig_top10.head(10))
    print (" ")
    print ("PROCESSED - top 10 words")
    print (pr_top10.head(10))



.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    ORIGINAL - top 10 words
      token  count
    0     ,     68
    1           57
    2   the     40
    3    of     39
    4     .     29
    5     -     29
    6     a     20
    7   and     19
    8    to     19
    9    in     18
 
    PROCESSED - top 10 words
          token  count
    0         ,     68
    1               56
    2         .     29
    3         -     29
    4         (     16
    5         )     16
    6  language     14
    7         "     12
    8   machine     11
    9   systems     11




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  21.887 seconds)


.. _sphx_glr_download_examples_ex_get_stopwords.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download

     :download:`Download Python source code: ex_get_stopwords.py <ex_get_stopwords.py>`



  .. container:: sphx-glr-download

     :download:`Download Jupyter notebook: ex_get_stopwords.ipynb <ex_get_stopwords.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
