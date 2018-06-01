# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 10:45:29 2018

@author: Marty

pastebin.py

This file is not meant to be included in any merge with Develop!
As the name implies, this is just a dump where I can store useful code
from my notebooks in one central location for later development.

1) Paste new code from the notebooks into this module.

2) If I choose to develop some code further:
    - move it into an official module
    - add tests
    - add documentation & example notebooks
    ==> OPTION 1: create a branch off of paste-bin with a descriptive name
            - delete this module (pastebin.py)
            - merge the new branch with the Develop branch
            - Keep adding stuff to the paste-bin branch; repeat
    ==> OPTION 2: Create a branch off of Develop
            - Cut and paste new files and modules from paste-bin branch into the new branch
            - Keep adding stuff to the paste-bin branch; repeat
"""
from __future__ import absolute_import, print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
from scipy.ndimage.filters import minimum_filter1d, generic_filter
from scipy.ndimage.measurements import label
from scipy.signal import argrelextrema
from scipy import signal


def cleanDF(DF):
    DF = pd.DataFrame(DF.iloc[:, 0])
    cols = DF.columns.values
    for i, col in enumerate(cols):
        cols[i] = col[5:-12]  # This works for siteID's of different lengths.
    DF.columns = cols
    print(DF.columns)
    return DF


def QQplot(A, B, scale='log', ylabel='Discharge', symbol='.'):
    """Creates a QQ chart from two series of discharges with the same time index.
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
    # Set sizes
    left = bottom = 0.1
    width = ABheight = 0.7
    Bheight = 0.2
    divider = 0.05

    Adim = [left, bottom + ABheight + divider + Bheight + divider, width, Bheight]
    Bdim = [left, bottom + ABheight + divider, width, Bheight]
    ABdim = [left, bottom, width, ABheight]

    # Set figure size and subplot sizes
    # plt.figure(1)
    fig = plt.figure(1, figsize=(19, 14))
    axAB = plt.axes(ABdim)
    axA = plt.axes(Adim)
    axA.set_yscale(scale)
    axB = plt.axes(Bdim, sharey=axA)

    # Create the plots
    axAB.plot(A, B, symbol)
    axA.plot(A)  # Plot A using its index, which should be a datetimeindex
    axB.plot(B)  # Plot B using its index, which should be a datetimeindex

    # fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    # fig.set_size_inches(8, 10)
    # ax1()
    # ax1.plot(Qx)
    # ax2.plot(Qy)
    # ax3.plot(Qx, Qy, symbol)
    # ax.set_xscale(xscale)
    # ax.set_yscale(yscale)
    # ax.set_ylabel(ylabel)
    # ax.legend()
    # A pyplot bug causes a valueError value if the xlabel is set.
    # ax.set_xlabel('Probability of Exceedence')
    # ax.xaxis.set_minor_formatter(NullFormatter())
    return fig, (axAB, axA, axB)


def xcorr(x, y1, y2):
    npts = max(len(x), len(y1), len(y2))
    print('number of points: ', npts)
    lags = np.arange(-npts + 1, npts)
    # np.correlate returns nan if any nan are present.
    # replace nan with 0, mean, or interpolate
    # It is faster to calculate y1.mean() than np.nanmean(y1), so only do it if  you need to. 
    # Do this for st dev too,
    # or maybe I should just simplify things and not worry about performance just yet.
    if (np.any(np.isnan(y1))):
        print("replacing nan's in y1 with 0")
        y1 = np.nan_to_num(y1)
        assert(not np.any(np.isnan(y1)))

    if (np.any(np.isnan(y2))):
        print("replacing nan's in y2 with 0")
        y2 = np.nan_to_num(y2)
        assert(not np.any(np.isnan(y2)))

    y1mean = y1.mean()
    y2mean = y2.mean()
    print('y1mean: ', y1mean)
    print('y2mean: ', y2mean)

    # Subtract mean from value; but don't include all of our padded zeros, use orig values but ignore nans.
    ccov = np.correlate(y1 - y1mean, y2 - y2mean, mode='full')
    # matplotlib also has an acorr and xcorr plot for autocorrelation and xcorrelation, with some additional features, like
    # detrending.
    assert(not np.any(np.isnan(ccov)))
    ccor = ccov / (npts * np.nanstd(y1) * np.nanstd(y2))
    assert(not np.any(np.isnan(ccor)))

    maxlag = lags[np.argmax(ccor)]
    maxccor = np.max(ccor)
    print("The second array must be shifted by a lag of {0} to match the first array.".format(maxlag))
    print("The maximum correlation is {0}.".format(maxccor))

    fig, axs = plt.subplots(nrows=3, figsize=(12, 14))
    fig.subplots_adjust(hspace=0.2)
    axs[0].plot(x, y1, 'blue', label='y1')
    axs[0].legend(loc='upper right')

    axs[1].plot(x, y2, 'red', label='y2')
    axs[1].legend(loc='upper right')

    axs[2].plot([0, 0], [-1, 1], color='r', linestyle='-', linewidth=1)
    axs[2].plot(lags, ccor, label='correlation')
    axs[2].plot(maxlag, maxccor,'r+', markersize=12, markeredgewidth=1, label='max')
    axs[2].set_ylim(-1.1, 1.1)
    axs[2].set_ylabel('cross-correlation')
    axs[2].set_xlabel('lag of y1 relative to y2')
    axs[2].legend(loc='upper right', ncol=2)

    return maxlag

def longdisplay(DF):
    """Temporarily display the entirety of a large dataframe.
    
    See: 
        https://pandas.pydata.org/pandas-docs/stable/generated/pandas.option_context.html
        
    
    Usage:
        hf.longdisplay(my_data)
    """
    with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
        # display is from Ipython, and is automatically imported.
        display(DF)


def local_minimum_filter(ts, size):
    """USGS HYSEP local minimum method
        https://github.com/dadelforge/baseflow-separation/blob/master/physep/hysep.py
        It might be possible to modify this procedure by using signal.find_peaks()
        to find the troughs, and then connect them with a curved line instead.

        The USGS HYSEP local minimum method as described in `Sloto & Crouse, 1996`_.

    .. _Slot & Crouse, 1996:
        Sloto, Ronald A., and Michele Y. Crouse. “HYSEP: A Computer Program for Streamflow Hydrograph Separation and 
        Analysis.” USGS Numbered Series. Water-Resources Investigations Report. Geological Survey (U.S.), 1996. 
        http://pubs.er.usgs.gov/publication/wri964040.

    :param size:
    :param ts:
    :return:
    """

    origin = int(size) / 2
    baseflow_min = pd.Series(generic_filter(ts, _local_minimum, footprint=np.ones(size)), index=ts.index)
    baseflow = baseflow_min.interpolate(method='linear')
    # interpolation between values may lead to baseflow > streamflow
    errors = (baseflow > ts)
    while errors.any():
        print('hello world')
        error_labelled, n_features = label(errors)
        error_blocks = [ts[error_labelled == i] for i in range(1, n_features + 1)]
        error_local_min = [argrelextrema(e.values, np.less)[0] for e in error_blocks]
        print(error_local_min)
        break
    quickflow = ts - baseflow
    baseflow.name = 'baseflow'
    quickflow.name = 'quickflow'

    return baseflow, quickflow


def _local_minimum(window):
    win_center_ix, rem = divmod(len(window), 2)
    win_center_val = window[win_center_ix]
    win_minimum = np.min(window)
    if win_center_val == win_minimum:
        return win_center_val
    else:
        return np.nan


# These three functions are from BaseflowSeparation3.ipynb

def Nfreq(wavelength_days, sample_rate_per_hour):
    # This uses my imaginary unit of 'Az', or cycles per year. A week has a frequency of 52 Az, and days are 365 Az.
    Nyquist_freq_Az = sample_rate_per_hour * 24 * 365 / 2    # Nyquist_freq_Az should be 17520 if samples are taken every 15 minutes.
    crit_freq_Az = 365/wavelength_days
    Nratio = crit_freq_Az / Nyquist_freq_Az
    return Nratio


def estimate_filter_response_length(b, a):
    # This is an approximation of how many samples it takes for an impulse to quiet down to almost zero using a particular filter.
    # from bottom of https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.filtfilt.html
    z, p, k = signal.tf2zpk(b, a)
    eps = 1e-9
    r = np.max(np.abs(p))
    approx_impulse_len = int(np.ceil(np.log(eps) / np.log(r)))
    return approx_impulse_len


def butterworth(Qdata, order=2, low_wave_days=10, high_wave_days=1, sample_rate_per_hour=4, filter_type='lowpass'):
    # The defaults are set to be reasonable for filtering out floods on watersheds smaller than 10,000km2 or so...
    if filter_type == 'lowpass':
        Nratio = Nfreq(low_wave_days, sample_rate_per_hour)
        filter_label = str(low_wave_days) + '-day lowpass'
    elif filter_type == 'highpass':
        Nratio = Nfreq(high_wave_days, sample_rate_per_hour)
        filter_label = str(high_wave_days) + '-day highpass'
    elif filter_type == 'bandpass' or filter_type == 'bandstop':
        Nratio = [Nfreq(low_wave_days, sample_rate_per_hour), Nfreq(high_wave_days, sample_rate_per_hour)]
        filter_label = str(low_wave_days) + ' to ' + str(high_wave_days) + '-day ' + filter_type
    else:
        print('filter_type was set to "', filter_type, '", valid types are "lowpass", "highpass", "bandpass", and "bandstop".')

    b, a = signal.butter(order, Nratio, btype=filter_type)
    
    # signal.filtfilt will return a zero-phase shift result;
    # This uses the 'gust'  Gustopherson method for dealing with the edges of the observed data.
    y = signal.filtfilt(b, a, Qdata, method="gust", irlen=estimate_filter_response_length(b,a))
    df = pd.DataFrame(data=y, index=Qdata.index, columns=[Qdata.name])
    label = str(order) + 'th-order ' + filter_label + ' Butterworth filter'
    result = {'data': df, 'label': label}

    return result
