from datetime import datetime
import pandas as pd
import numpy as np
import pytz
import lasio

""" Import and process data from various sources and return Pandas
Dataframes. Sources are BPWA .csv file, memory data .las file, and user-defined
events .csv file.
"""


# Import and clean memory data from .las file. Set datetime index and convert
# to UTC.
def process_memory_data(filename):
    df = import_memory_data(filename)
    df = clean_data(df)
    df = set_time_index(df, 'TIME')
    df = convert_index_utc(df)
    return df


# Import and clean realtime data from .csv file. Set index to datetime on
# import. Convert to UTC.
def process_rt_data(filename):
    df = import_bpwa_data(filename)
    df = clean_data(df)
    df = convert_index_utc(df)
    return df


# Import events file. Set datetime index and convert to UTC.
def process_events(filename):
    df = pd.read_csv(filename)
    df = set_time_index(df, 'time')
    df = convert_index_utc(df)
    return df


# Helper method to set Dataframe index to datetime based on some key (column
# name). Localize to US central time.
def set_time_index(df, key):
    df = df.set_index(key)
    df.index = pd.to_datetime(df.index)
    df.index = df.index.tz_localize(pytz.timezone('US/Central'))
    return df


# Convert datetime index to UTC. Assumes TZ aware.
def convert_index_utc(df):
    df.index = df.index.tz_convert(pytz.UTC)
    return df


def import_bpwa_data(filename):
    """ Imports data from csv format into DataFrame, setting time as index.
    Returns DataFrame.
    """

    def dateparse(s):
        return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S.%f%z')

    df = pd.read_csv(filename,
                     skiprows=[1],
                     index_col='TIME',
                     date_parser=dateparse,
                     parse_dates=['TIME'])
    return df


# Cleans data, replacing -999.25 null value with np.nan
def clean_data(df):
    return df.replace(-999.25, np.nan)


def import_memory_data(filename):
    las = lasio.read(filename)
    return las.df()


# events['y'] = df_bpwa.loc[events.index, 'GS_DBTM']
