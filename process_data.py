from datetime import datetime
import os
import pandas as pd
import numpy as np
import pytz
import lasio

from config import RT_MNEMONICS as mnem_rt
from config import MEM_MNEMONICS as mnem_mem
from config import MFIA_MULTIPLIER

""" Import and process data from various sources and return Pandas
Dataframes. Sources are BPWA .csv file, memory data .las file, and user-defined
events .csv file.
"""


# Import and clean memory data from .las file. Set datetime index and convert
# to UTC.
def process_memory_data(filename):
    if not filename:
        return (None, None)
    df, units = import_memory_data(filename)
    df = clean_data(df)
    df = set_time_index(df, mnem_rt['time'])
    df = convert_index_utc(df)
    df = rename_cols(df, mnem_mem)
    return df, units


# Import and clean realtime data from .csv file. Set index to datetime on
# import. Convert to UTC.
def process_rt_data(filename):
    if not filename:
        return
    df = import_bpwa_data(filename)
    units = import_bpwa_units(filename)
    df = clean_data(df)
    df = convert_index_utc(df)
    df = rename_cols(df, mnem_rt)
    units = rename_cols(units, mnem_rt).iloc[0].to_dict()
    df = flowrate_multiplier(df, MFIA_MULTIPLIER)
    return df, units


# Import events file. Set datetime index and convert to UTC.
def process_events(filename):
    if not filename:
        return
    df = pd.read_csv(filename)
    df = set_time_index(df, mnem_mem['time'])
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

    # def dateparse(s):
    #     return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S.%f%z')

    df = pd.read_csv(filename,
                     skiprows=[1],
                     index_col=mnem_rt['time'],
                    #  date_parser=dateparse,
                     parse_dates=[mnem_rt['time']])
    return df

def import_bpwa_units(filename): 

    units = pd.read_csv(filename, nrows=1)
    return units

# Cleans data, replacing -999.25 null value with np.nan
def clean_data(df):
    return df.replace(-999.25, np.nan)


def import_memory_data(filename):
    las = lasio.read(filename)
    units = {key: las.curves[value].unit for key, value in mnem_mem.items()}
    return las.df(), units


def get_filepath(path, filename):
    dirname = os.path.dirname(__file__)
    if filename:
        return os.path.join(dirname, path, filename)
    return

def rename_cols(df, mnem): 
    # Swap mnemonics keys/values and rename columns to standardized names
    col_map = {}
    for key, value in mnem.items(): 
        col_map[value] = key
    return df.rename(columns=col_map)

def flowrate_multiplier(df, multiplier): 
    df['mfia_multiplier'] = df['mfia'] / multiplier
    return df