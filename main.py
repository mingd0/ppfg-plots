import config
from plot import create_drilling_plot
from process_data import (
    process_memory_data, process_rt_data, process_events, get_filepath)

import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def main():

    bpwa_filename = get_filepath(config.BPWA_PATH, config.BPWA_FILENAME)
    las_filename = get_filepath(config.MEMORY_PATH, config.MEMORY_FILENAME)
    events_filename = get_filepath(config.EVENTS_PATH, config.EVENTS_FILENAME)

    df_rt = process_rt_data(bpwa_filename)
    df_mem = process_memory_data(las_filename)
    df_events = process_events(events_filename)

    fig = create_drilling_plot(df_rt, df_mem, df_events)
    fig.show()
    fig.write_html(os.path.join(
        os.path.dirname(__file__),
        f'{config.OUTPUTS_PATH}{config.OUTPUT_FILENAME}'
        ))


if __name__ == "__main__":
    main()
