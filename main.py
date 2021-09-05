from config import BPWA_FILENAME, MEMORY_DATA_FILENAME, EVENTS_FILENAME
from plot import create_drilling_plot
from process_data import process_memory_data, process_rt_data, process_events

import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def main():

    dirname = os.path.dirname(__file__)

    bpwa_filename = os.path.join(dirname, f'data/bpwa/{BPWA_FILENAME}')
    las_filename = os.path.join(dirname, f'data/memory/{MEMORY_DATA_FILENAME}')
    events_filename = os.path.join(dirname, f'data/events/{EVENTS_FILENAME}')

    df_mem = process_memory_data(las_filename)
    df_rt = process_rt_data(bpwa_filename)
    df_events = process_events(events_filename)

    create_drilling_plot(df_rt, df_mem, df_events)


if __name__ == "__main__":
    main()
