# -*- coding: utf-8 -*-
"""
charts.py

Charting functions for Hydrofunctions.
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

# I don't need these yet, but soon...
import bokeh
import seaborn


def flow_duration(Qdf, xscale='logit', yscale='log', ylabel='Discharge', symbol='.'):
    """Creates a flow duration chart from a dataframe of discharges.

    Args:
        Qdf (dataframe): a dataframe of discharge values.
            * Values should be arranged in columns
            * No sorting necessary
            * Rows do not need an index
            * If more than one column, each column will be added as a\
                separate color to the chart.
            * Only include columns with discharge values; no metadata

        xscale ('logit' | 'linear'): Type of x scale for plotting probabilities
            default is 'logit', so that each standard deviation is nearly the
            same distance on the x scale. 'linear' is the other option.

        yscale ('log' | 'linear'): The type of y scale for plotting discharge.
            Default is 'log'.

        ylabel (str, default: 'Discharge'): The label for the Y axis.

        xlabel (not implemented)

        symbol (str, '.' | ','): formatting symbol for points.
            * point: '.' (default)
            * pixel point: ','
            * circle: 'o'
            * triangle up: '^'

            See https://matplotlib.org/api/markers_api.html for full list of
            point formatters.

    Returns:
        fig (matplotlib.figure.Figure):
            a matplotlib figure. This will plot immediately in a Jupyter
            notebook if the command '%matplotlib inline' was previously issued.
            The figure may also be altered after it is returned.

        ax (matplotlib.axes.Axes):
            a matplotlib chart. This may be altered after it is returned.

    """
    rank = Qdf.rank(ascending=False, pct=True)
    x = rank
    y = Qdf
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y, symbol)
    ax.set_xscale(xscale)
    ax.set_yscale(yscale)
    ax.set_ylabel(ylabel)
    # A pyplot bug causes a valueError value if the xlabel is set.
    #ax.set_xlabel('Probability of Exceedence')
    ax.xaxis.set_minor_formatter(NullFormatter())
    return fig, ax
