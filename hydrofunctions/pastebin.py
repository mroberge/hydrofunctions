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
    ==> OPTION 2 (preferred): Create a branch off of Develop
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


def clean_DF(df):
    """Convert a hydrofunctions dataframe with mixed data & flag columns into purely data columns.
    """
    df = pd.DataFrame(DF.iloc[:, 0])
    cols = df.columns.values
    for i, col in enumerate(cols):
        cols[i] = col[5:-12]  # This works for siteID's of different lengths.
    df.columns = cols
    print(df.columns)
    return df


def clean(df):
    """Convert a hydrofunctions dataframe with mixed data & flag columns into a dict with a meta & a data dataframe.
    """
    df.index.name = 'time'
    # create a data dataframe with the discharge data.
    data = df.iloc[:, ::2]  # Select all rows, select all columns stepping by two.

    # rename data columns
    cols = data.columns.values
    for i, col in enumerate(cols):
        cols[i] = col[5:-12]
    # create a metadata dataframe with data flags.
    meta = df.iloc[:, 1::2]  # Select all rows, select all columns starting at 1 and stepping by two.

    # rename meta columns
    cols = meta.columns.values
    for i, col in enumerate(cols):
        cols[i] = col[5:-23]+'_flag'

    # Create new data structure
    result = {'data': data, 'meta': meta}
    return result


def clean_verbose (DF, nans=False):
    """
    taken from SusquehannaDataPrep.ipynb on 10/7/2018
    nans parameter is not used.
    
    note from 2018-7-31:
    I Improved my clean() function when I read data.
        - See SusquehannaDataPrep.ipynb
        - It now prints lots of lovely information about the original dataset
        - It improves the index so that if any rows are missing they get added.
        - It sorts all of the indexes properly.
        - It reports on how many NaN’s exist as an absolute count and as a percentage.
        - The call signature is set up so that I can do some interpolation, but I haven’t created that functionality yet.
    TODO: add interpolation functionality to clean.

    """
    DF.index.name = 'time'

    # Remove all duplicated index values
    print(f'Original data has {len(DF.index)} entries. There are no repeated index values: {DF.index.is_unique}')
    DF = DF[~DF.index.duplicated(keep='first')]
    print(f'There are now {len(DF.index)} entries.')
    DF.sort_index(axis=0, inplace=True)
    print(f'New index has no repeated values: {DF.index.is_unique}, and it is monotonic: {DF.index.is_monotonic}.')

    new_freq = DF.index.freq
    if DF.index.freq is None:
        new_freq = pd.infer_freq(DF.index)
        if new_freq is None:
            guess1 = (DF.index.max() - DF.index.min())/len(DF.index)
            if pd.Timedelta('13 minutes') < guess1 < pd.Timedelta('17minutes'):
                new_freq = pd.Timedelta('15 minutes')
            else:
                raise ValueError("Cannot calculate the dataset frequency.")

    print(f'Original frequency: {DF.index.freq}; New Frequency: {new_freq}')
    orig_len = len(DF)
    print(f'Re-organizing the time index. There should be {((DF.index.max()-DF.index.min())/new_freq) + 1} records.')
    DF = DF.asfreq(new_freq)
    new_len = len(DF)
    print(f'original length: {orig_len}; new length: {new_len}; missing records: {new_len - orig_len}')
    
    nulls = DF.isnull().sum()
    nulls = pd.DataFrame(nulls, columns=['NaN_count'])
    nulls.index.name = 'columns'
    nulls['percent'] = nulls / len(DF)
    print(f'Missing data: ')
    print(nulls)
    

    
    # create a data dataframe with the discharge data.
    # TODO: make this work when you ask for more than one type data (right now it assumes that only IV discharge has been requested.)
    # TODO: It would be better to work with the original USGS JSON file than to re-parse this dataframe.
    # TODO: for now, make a separate request for each parameter code.
    
    #     parse the column names
    #        strip the 'USGS:'  (or check for it and raise an error if it is not there)
    #        check for any summary type that isn't '0000'; raise error if they exist; get rid of them. I'll worry about these later.
    #        separate columns into different stations
    #        For each station name:
    #            separate columns into different parameter codes
    #            check that the _qualifiers columns for a station match; raise an error if they don't.
    #            Add one of the _qualifiers columns into a new meta dataframe. get rid of the others.
    #            For each parameter code:
    #                Add the data column to a dataframe for that parameter.
    data = DF.iloc[:, ::2] # Select all rows, select all columns stepping by two.
    
    # rename data columns
    cols = data.columns.values
    for i, col in enumerate(cols):
        cols[i] = col[5:-12] # This gets rid of everything in the name except for the station ID.
        #cols[i] = col[5:-6] # This gets rid of everything in the name except the station ID and the parameter code.
    data.columns = cols
    
    # create a metadata dataframe with data flags.
    meta = DF.iloc[:, 1::2] # Select all rows, select all columns starting at 1 and stepping by two.
    
    # rename meta columns
    #cols = meta.columns.values
    #for i, col in enumerate(cols):
    #    cols[i] = col[5:-23]+'_qualifiers'
    
    #data = data[~data.index.duplicated(keep='first')]
    #data.sort_index(axis=0, inplace=True)
    data.sort_index(axis=1, inplace=True)
    meta.sort_index(axis=1, inplace=True)
    #data = data[sorted(data.columns)]
    #meta = meta[sorted(meta.columns)]
        
    # Create new data structure
    result = {'data':data, 'meta': meta}
    
    print(f'First observation: {data.index.min()}')
    print(f'Last observation: {data.index.max()}')
    print(f'Length: {data.index.max()-data.index.min()};   {len(data)} records x {len(data.columns)} sites.')
    
    return result


def nwis_measurements(site):
    """Load USGS stream discharge measurements into a Pandas dataframe.
    Written on 2018-8-13 
    Taken from Rating_Curve.ipynb on 2018-10-7
    
    Inputs: site
        The gage number for the site.
        
    Outputs:
    Will produce a table, each row represents an observation of river conditions at the gage by USGS personell. Values measured
    include stream discharge, channel width, channel area, depth, and velocity. These data can be used to create a rating curve,
    to estimate the gage height for a discharge of zero, and to get readings of water velocity.
    
    to plot a rating curve, use output.plot(x='gage_height_va', y='discharge_va', kind='scatter')
    NOTE: Rating curves are typically plotted with the indepedent variable (gage_height) plotted on the Y axis.
    """
    url = f'https://waterdata.usgs.gov/pa/nwis/measurements?site_no={site}&agency_cd=USGS&format=rdb_expanded'
    response = requests.get(url)
    text = response.text
    # It may be desireable to keep the original na_values, like 'unkn' for many of the columns. However, it is still
    # a good idea to replace for the gage depth and discharge values, since these variables get used in plotting functions.
    output = pandas.read_table(url, comment='#', keep_default_na=True, na_values=['UNSP', 'unkn', 'unspe', 'unkno'],
                           skiprows=[15],
                           dtype={'site_no':str},
                           parse_dates=['measurement_dt'], infer_datetime_format=True
                          )
    return output


def QQplot(A, B, scale='log', ylabel='Discharge', symbol='.'):
    """Creates a QQ chart from two series of discharges with the same time index.

    Usually a QQplot means quantile-quantile plot, **NOT** discharge.

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
    if np.any(np.isnan(y1)):
        print("replacing nan's in y1 through interpolation")
        # y1 = np.nan_to_num(y1)  # replace Nan's with zero
        y1 = y1.interpolate()
        assert not np.any(np.isnan(y1))

    if np.any(np.isnan(y2)):
        print("replacing nan's in y2 through interpolation")
        y2 = y2.interpolate()
        assert not np.any(np.isnan(y2))

    y1mean = y1.mean()
    y2mean = y2.mean()
    print('y1mean: ', y1mean)
    print('y2mean: ', y2mean)

    # Subtract mean from value; but don't include all of our padded zeros, use orig values but ignore nans.
    ccov = np.correlate(y1 - y1mean, y2 - y2mean, mode='full')
    # matplotlib also has an acorr and xcorr plot for autocorrelation and xcorrelation, with some additional features, like
    # detrending.
    assert not np.any(np.isnan(ccov))
    ccor = ccov / (npts * np.nanstd(y1) * np.nanstd(y2))
    assert not np.any(np.isnan(ccor))

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
    axs[2].plot(maxlag, maxccor, 'r+', markersize=12, markeredgewidth=1, label='max')
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
        result = win_center_val
    else:
        result = np.nan
    return result


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
    y = signal.filtfilt(b, a, Qdata, method="gust", irlen=estimate_filter_response_length(b, a))
    df = pd.DataFrame(data=y, index=Qdata.index, columns=[Qdata.name])
    datalabel = str(order) + 'th-order ' + filter_label + ' Butterworth filter'
    result = {'data': df, 'label': datalabel}

    return result
