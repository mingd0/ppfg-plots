from datetime import datetime
import pandas as pd
import numpy as np
import pytz
import lasio


def process_memory_data(filename):
    df = import_memory_data(filename)
    df = clean_data(df)
    df = set_time_index(df, 'TIME')
    df = convert_index_utc(df)
    return df


def process_rt_data(filename):
    df = import_bpwa_data(filename)
    df = clean_data(df)
    df = convert_index_utc(df)
    return df


def process_events(filename):
    df = pd.read_csv(filename)
    df = set_time_index(df, 'time')
    df = convert_index_utc(df)
    return df


def set_time_index(df, key):
    df = df.set_index(key)
    df.index = pd.to_datetime(df.index)
    df.index = df.index.tz_localize(pytz.timezone('US/Central'))
    return df


def convert_index_utc(df):
    df.index = df.index.tz_convert(pytz.UTC)
    return df


# Could pull out dateparse and pass in as function
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


def clean_data(df):
    return df.replace(-999.25, np.nan)


def import_memory_data(filename):
    las = lasio.read(filename)
    return las.df()


# events['y'] = df_bpwa.loc[events.index, 'GS_DBTM']
