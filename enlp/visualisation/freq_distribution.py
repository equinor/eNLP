"""
Contains functions for visualisation of text
"""

import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud


def wordcloud_plot(token_list, colormap='rainbow', ax=None):
    """ Word cloud of tokens

    Parameters
    ----------
    token_list : :obj:`list`
        list of tokens, can be obtained from nlp_tools.to_list()
    colormap : :obj:`str`
        colormap object, see predifened colormaps at https://matplotlib.org/examples/color/colormaps_reference.html
        [optional, default = 'rainbow']
    ax : :obj:`matplotlib.axes.Axis`
        Axis object for figure

    Returns
    -------
    fig : :obj:`matplotlib.figure.Figure`
        Figure object line plot of word counts
    ax : :obj:`matplotlib.axes.Axis`
        Axis object for figure

    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 15))
    else:
        fig = None

    wordcloud = WordCloud(width=1500, height=1200, margin=0,
                          colormap=colormap,
                          collocations=False).generate(' '.join(token_list))

    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")

    return fig, ax


def dist_plot_detailed(word_counts, log=False, ax=None):
    """ Frequency count of tokens in a SMALL Corpus (<50 unique tokens) with words on the x-axis

    Parameters
    ----------
    word_counts : :obj:`list`
        sorted list of words and their respective frequency, can be obtained from nlp_distributions.count()
    log : :obj:`bool`
        make y axis logarithmic [optional, default = False]
    ax : :obj:`matplotlib.axes.Axis`
        Axis object for figure

    Returns
    -------
    fig : :obj:`matplotlib.figure.Figure`
        Figure object line plot of word counts
    ax : :obj:`matplotlib.axes.Axis`
        Axis object for figure

    Notes
    -----
    If there are more than 50 unique tokens then the plot will be too busy and may crash your machine while computing

    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 15))
    else:
        fig = None

    words = [str(w[0]) for w in word_counts]
    counts = np.asarray([w[1] for w in word_counts])

    # print (len(words))
    # print (len(counts))


    if log:
        ax.semilogy(range(len(words)),counts)
        ax.set_title('Log. Word Frequencies')
        ax.set_ylabel('Log. word count')
    else:
        ax.plot(range(len(words)),counts)
        ax.set_title('Word Frequencies')
        ax.set_ylabel('Word count')

    ax.grid(True)

    ax.set_xticks(range(len(words)))
    ax.set_xticklabels(words, rotation=90)
    ax.set_xlabel('Words')

    return fig, ax


def dist_plot(word_counts, log=False, shade_singles=True, shade_top25=True, ax=None):
    """ Frequency count of tokens

    Parameters
    ----------
    word_counts : :obj:`list`
        sorted list of words and their respective frequency, can be obtained from nlp_distributions.count()
    log : :obj:`bool`
        make y axis logarithmic [optional, default = False]
    shade_singles : :obj:`bool`
        shade area on graph where token counts are 1 [optional, default = True]
    shade_top25 : :obj:`bool`
        shade area on graph where tokens count for top quarter of tokens [optional, default = True]
    ax : :obj:`matplotlib.axes.Axis`
        Axis object for figure

    Returns
    -------
    fig : :obj:`matplotlib.figure.Figure`
        Figure object line plot of word counts
    ax : :obj:`matplotlib.axes.Axis`
        Axis object for figure

    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 15))
    else:
        fig = None

    counts = np.asarray([w[1] for w in word_counts])

    # ax.set_xticklabels(ax.get_xticklabels(True), rotation=90)
    ax.set_xlabel('Index of word')
    ax.grid(True)

    if shade_singles:
        ax.axvspan(min(np.argwhere(counts == 1.)), max(np.argwhere(counts == 1.)), alpha=0.5,
                    color='lightblue', label='single-occurance')
        ax.legend()

    if shade_top25:
        num_words = sum(counts)
        words_cum_sum = np.cumsum(counts)
        top25 = num_words / 4.
        # last_top25_ind = max(np.argwhere(words_cum_sum <= top25))
        ax.axvspan(min(np.argwhere(words_cum_sum <= top25)), max(np.argwhere(words_cum_sum <= top25)),
                    alpha=0.5, color='red', label='25% of occurances')
        ax.legend()

    if log:
        ax.semilogy(counts, color='k')
        ax.set_title('Log. Word Frequencies')
        ax.set_ylabel('Log. word count')
    else:
        ax.plot(counts, color='k')
        ax.set_title('Word Frequencies')
        ax.set_ylabel('Word count')

    return fig, ax
