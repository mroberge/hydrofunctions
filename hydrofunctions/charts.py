# -*- coding: utf-8 -*-

"""
hydrofunctions.charts
~~~~~~~~~~~~~~~~~~~~~

This module contains charting functions for Hydrofunctions.

-----
"""
# Recommended that I use this line to avoid errors in TravisCI
# See https://matplotlib.org/faq/howto_faq.html
# Basically, matplotlib usually uses an 'X11 connection' by default; Travis CI
# does not have this configured, so you need to set your backend explicitly.
from __future__ import absolute_import, print_function, division, unicode_literals
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import numpy as np


def flow_duration(Qdf, xscale='logit', yscale='log', ylabel='Stream Discharge (m³/s)', symbol='.', legend=True, legend_loc='best', title=''):
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

        ylabel (str, default: 'Stream Discharge (m³/s)'): The label for the Y axis.

        xlabel (not implemented)

        symbol (str, '.' | ','): formatting symbol for points.

            * point: '.' (default)
            * pixel point: ','
            * circle: 'o'
            * triangle up: '^'

            See https://matplotlib.org/api/markers_api.html for full list of
            point formatters.

        legend (bool, default: True): whether the legend should be plotted.

        legend_loc (str, default: 'best'): the location of the legend.

            * 'best': Automatically choose the option below with the least overlap.
            * 'upper left', 'upper right', 'lower left', 'lower right': place the legend at the corresponding corner of the axes/figure.
            * 'upper center', 'lower center', 'center left', 'center right': place the legend at the center of the corresponding edge of the axes/figure.
            * 'center': place the legend at the center of the axes/figure.
            * The location can also be a 2-tuple giving the coordinates of the lower-left corner of the legend in axes coordinates.

        title (str, default: ''): text to use as a figure title. If no text
            is provided, no title will be created (default).

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
    for column in Qdf.columns.values:
        ax.plot(x.loc[:,column], y.loc[:,column], symbol, label=column)
    ax.set_xscale(xscale)
    ax.set_yscale(yscale)
    ax.set_ylabel(ylabel)
    if legend:
        ax.legend(loc=legend_loc)
    if title:
        ax.title.set_text(title)
    # A pyplot bug causes a valueError value if the xlabel is set.
    #ax.set_xlabel('Probability of Exceedence')
    ax.xaxis.set_minor_formatter(NullFormatter())
    return fig, ax


def cycleplot(Qseries, cycle='diurnal', compare=None, y_label='Discharge (ft³/s)', legend=True, legend_loc='best', title=''):
    """Creates a chart to illustrate annual and diurnal cycles.

    This chart will use the pandas groupby method to plot the mean and median
    values for a time-indexed dataframe. It helps you identify diurnal patterns
    by plotting the mean and median values over 24 hours for a diurnal pattern,
    and over a year for annual patterns.

    This function will also use the 'compare' argument to create a series of
    charts to compare how well these cycles appear in different groups. For
    example, is the diurnal cycle more visible in December versus June? In this
    case, you would use::

        hf.cycleplot(myDataFrame, cycle='diurnal', compare = 'month')

    This will produce twelve charts, each covering 24 hours. A line will
    represent the mean values over 24 hours, another line represents the
    median, and two grey stripes represent the 0.4 to 0.6 quantile, and the
    0.2 to 0.8 quantile range.

    Args:
        Qseries (series): a Pandas series of discharge values.
            * Values should be arranged in columns
            * Should use a dateTimeIndex

        cycle (str): The period of the cycle to be illustrated, along with the
            method for binning. The options are:

            * diurnal (default): plots the values for a 24 hour cycle.
            * diurnal-smallest: uses the smallest increment of time \
            available to bin the time units for a 24 hour cycle.
            * diurnal-hour: uses hours to bin measurements for a 24-hour \
            cycle.
            * annual: plots values into a 365 day cycle.
            * annual-day: the annual cycle using 365 day-long bins.
            * annual-week: the annual cycle using 52 week-long bins.
            * annual-month: the annual cycle using 12 month-long bins.
            * weekly: a 7-day cycle using seven 24-hour long bins. Note \
            that unlike the others, this is not a natural cycle, and is \
            likely has anthropogenic origins.

        compare (str): The system for splitting the data into
            groups for a set of comparison charts.

            * None (default): No comparison will be made; only one chart.
            * month: twelve plots will be produced, one for each month.
            * weekday: seven plots will be produced, one for each day of \
            the week.
            * weekend: two plots will be produced, one for the five weekdays, \
            one for Saturday and Sunday.
            * night: two plots will be produced, one for night (6pm to 6am), \
            one for day (6am to 6pm).

        y_label (str): The label for the y axis.

        legend (bool, default: True): whether the legend should be plotted.

        legend_loc (str, default: 'best'): the location of the legend.

            * 'best': Automatically choose the option below with the least overlap.
            * 'upper left', 'upper right', 'lower left', 'lower right': place the legend at the corresponding corner of the axes/figure.
            * 'upper center', 'lower center', 'center left', 'center right': place the legend at the center of the corresponding edge of the axes/figure.
            * 'center': place the legend at the center of the axes/figure.
            * The location can also be a 2-tuple giving the coordinates of the lower-left corner of the legend in axes coordinates.

        title (str, default: ''): text to use as a figure title. If no text
            is provided, no title will be created (default).

    Returns:
        fig (matplotlib.figure.Figure):
            a matplotlib figure. This will plot immediately in a Jupyter
            notebook if the command '%matplotlib inline' was previously issued.
            The figure may also be altered after it is returned.

        ax (matplotlib.axes.Axes):
            an array of matplotlib charts. This may be altered after it is returned.

    Notes:
        inspired by: https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html
        Jake VanderPlas. 2016. Python Data Science Handbook. O'Reilly Media, Inc.'
    """



    if cycle == 'annual':
        # aggregate into 365 bins to show annual cycles. Same as annual-date
        cycleby = Qseries.index.dayofyear
        x_label = ' (day # of the year)'
    elif cycle == 'annual-date':
        cycleby = Qseries.index.dayofyear
        x_label = ' (day # of the year)'
    elif cycle == 'annual-week':
        # aggregate into 52 bins to show annual cycles.
        cycleby = Qseries.index.week
        x_label = ' (week # of the year)'
    elif cycle == 'annual-month':
        # aggregate into 12 binds to show annual cycles.
        cycleby = Qseries.index.month
        x_label = ' (month # of the year)'
    elif cycle == 'weekly':
        # aggregate into 7 bins to show week-long cycles.
        # Note: 7-day cycles are not natural cycles.
        cycleby = Qseries.index.weekday
        x_label = ' (day of the week, Monday = 0)'
    elif cycle == 'diurnal':
        # aggregate into 24 bins to show 24-hour daily (diurnal) cycles.
        cycleby = Qseries.index.hour
        x_label = ' (hour of the day)'
    elif cycle == 'diurnal-smallest':
        # Uses the smallest unit available in the time index to show 24-hour diurnal cycles.
        cycleby = Qseries.index.time
        x_label = ' (time of day)'
    elif cycle == 'diurnal-hour':
        # aggregate into 24 bins to show 24-hour daily (diurnal) cycles.
        cycleby = Qseries.index.hour
        x_label = ' (hour of the day)'
    else:
        print("The cycle label '", cycle, "' is not recognized as an option. Using cycle='diurnal' instead.")
        cycleby = Qseries.index.hour
        x_label = ' (hour of the day)'

    if compare is None:
        # Don't make a comparison plot.
        # TODO: This is a silly categorization to force all values in the index into the same category.
        compareby = np.where(Qseries.index.weekday < 20, 'A', 'B') #Since no comparison is desired, this puts all of the data into group A.
        sub_titles = ['']
    elif compare == 'month':
        # Break the time series into 12 months to compare to each other.
        compareby = Qseries.index.month
        sub_titles = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    elif compare == 'weekday':
        # Break the time series into 7 days of the week to compare to each other.
        compareby = Qseries.index.weekday
        sub_titles = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    elif compare == 'weekend':
        # Break the time series into 2 groups, Weekdays and Weekends for comparison.
        compareby = np.where(Qseries.index.weekday < 5, 'Weekday', 'Weekend')
        sub_titles = ['Weekdays', 'Weekends']
    elif compare == 'night':
        # Break the time series into 2 groups to compare day versus night.
        # TODO: This assumes the index hour is in local time, but it is in UTC time
        compareby = np.where((Qseries.index.hour >= 6) & (DF.index.hour < 19), 'Day', 'Night')
        sub_titles = ['Day', 'Night']
    else:
        print("The compare label '", compare, "' is not recognized as an option. Using compare=None instead.")
        compareby = np.where(Qseries.index.weekday < 20, 'A', 'B') #Since no comparison is desired, this puts all of the data into group A.
        sub_titles = ['data']

    selection = [compareby, cycleby]
    compare_list = list(np.unique(compareby))

    # group first by the compareby series, then by the cycle.
    grouped = Qseries.groupby(selection)

    #complicated_multiindex_DF_of_results = Qseries.groupby(selection).agg('mean', q2, q4, 'median', q6, q8)
#    results2 = Qseries.groupby(selection).agg(
#            mean=
#            Q2=
#            Q4=
#            Q5=
#            Q6=
#            Q8=
#            )
    # Why is this necessary? Pandas 0.25.0 won't let you do this:
    # grouped.quantile()  anymore. !?!
    def q2(x):
        return x.quantile(.2)
    def q4(x):
        return x.quantile(.4)
    def q6(x):
        return x.quantile(.6)
    def q8(x):
        return x.quantile(.8)

    mean = grouped.mean()
    Q2 = grouped.agg(q2)  #    Q2 = DF.groupby(selection).quantile(.2)
    Q4 = grouped.agg(q4)  #    Q4 = grouped.quantile(0.4)
    Q5 = grouped.median() #    Q5 = grouped.quantile(.5)
    Q6 = grouped.agg(q6)  #    Q6 = grouped.quantile(.6)
    Q8 = grouped.agg(q8)  #    Q8 = grouped.quantile(.8)

    Nplots = len(compare_list)
    fig, axs = plt.subplots(1, Nplots, figsize=(14, 6), sharey=True, sharex=True)
    if Nplots == 1:
        # If there is only one subplot, it gets returned as a single subplot instead of as a numpy array. In this case, we convert it to an array.
        axs = np.array([axs])

    for i, item in enumerate(compare_list):
        axs[i].plot(mean.loc[item], label='mean')
        # axs[i].plot(Q2.loc[item], label='20th percentile', color='black', linestyle='dotted', linewidth=2)
        axs[i].plot(Q5.loc[item], label='median', color='black', linestyle='dotted', linewidth=2)
        # axs[i].plot(Q8.loc[item], label='80th percentile', color='grey', linestyle='dashed', linewidth=1)
        axs[i].fill_between(Q2.loc[item].index, Q2.loc[item].values.flatten(), Q8.loc[item].values.flatten(), facecolor='grey', alpha=0.5)
        axs[i].fill_between(Q4.loc[item].index, Q4.loc[item].values.flatten(), Q6.loc[item].values.flatten(), facecolor='grey', alpha=0.5)
        axs[i].set_title(sub_titles[i])
        # axs[i].xaxis.set_major_locator(plt.MaxNLocator(4))
        # axs[i].xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H'))

    # Set the legend on either the ax or fig.
    if legend:
        axs[0].legend(loc=legend_loc, fancybox=True, framealpha=0.5)
    # fig.legend(loc='upper center', shadow=True, frameon=True, fancybox=True, framealpha=0.5)

    # Get the yaxis limits, set bottom to zero.
    ymin, ymax = axs[0].get_ylim()
    axs[0].set_ylim(0, ymax)
    axs[0].set_ylabel(y_label)
    axs[0].set_xlabel('Time' + x_label)
    plt.tight_layout()
    if title:
        fig.suptitle(title)

    return fig, axs
