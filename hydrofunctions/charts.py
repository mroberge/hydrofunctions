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


def flow_duration(Qdf):
    """Creates a flow duration chart from a dataframe of discharges.
    """
    rank = Qdf.rank(ascending=False, pct=True)
    x = rank
    y = Qdf
    fig, ax1 = plt.subplots(1, 1)
    ax1.plot(x, y, '.')
    ax1.set_xscale('logit')
    ax1.set_yscale('log')
    ax1.set_xlabel('Probability of Exceedence')
    ax1.xaxis.set_minor_formatter(NullFormatter())
    return fig, ax1
