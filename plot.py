import plotly.graph_objects as go
from plotly.subplots import make_subplots
from config import TITLE, ESD_MARKER_SIZE, MAX_PP_OH, MFIA_MULTIPLIER

""" Creates plot with Plotly based on three dataframes: realtime data (from
BPWA), memory data (from .las file) and user-defined 'events' (.csv).

Dataframes are generated in process_data.py.
"""


def create_drilling_plot(df_rt, units_rt, df_mem, units_mem, df_events):

    # Initialize figure with three subplots and shared x-axis. The second two
    # have secondary axes.
    fig = make_subplots(rows=3, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.02,
                        specs=[
                            [{"secondary_y": True}],
                            [{"secondary_y": True}],
                            [{"secondary_y": True}]
                        ])

    if df_rt is not None:
        # Bit depth
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['bit_depth'],
                                 mode='lines',
                                 name='Bit Depth',
                                 hovertemplate=('%{y:,.0f}' + ' ' + units_rt['bit_depth'])
                                 ),
                      row=1, col=1, 
                      secondary_y=False
                      )
                      
        # Gas
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['gas'],
                                 mode='lines',
                                 name='Gas',
                                 hovertemplate=('%{y:,.1f}' + ' ' + units_rt['gas']), 
                                 ),
                      row=1, col=1, 
                      secondary_y=True,
                      )

        # MWD Temperature (RT)
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['mwd_temp'],
                                 mode='markers',
                                 name='MWD Temp (RT)',
                                 hovertemplate=('%{y:,.0f}' + ' ' + units_rt['mwd_temp'])
                                 ),
                      row=1, col=1, 
                      secondary_y=True
                      )

        # Gamma Ray (Mem) - does this make sense on a time plot? 
        # fig.add_trace(go.Scatter(x=df_mem.index, y=df_mem['gamma_ray'],
        #                          mode='lines',
        #                          name='Gamma Ray',
        #                          hovertemplate='%{y:,.0f} gAPI'),
        #               row=1, col=1, 
        #               secondary_y=True
        #               )

        # Block position
        fig.add_trace(go.Scatter(x=df_rt.index,
                                 y=df_rt['block_position'],
                                 mode='lines',
                                 name='BPOS',
                                 hovertemplate=('%{y:.1f}' + ' ' + units_rt['block_position'])
                                 ),
                      secondary_y=False,
                      row=3, col=1
                      )

        # RPM
        fig.add_trace(go.Scatter(x=df_rt.index,
                                 y=df_rt['rpm'],
                                 mode='lines',
                                 name='RPM',
                                 hovertemplate=('%{y:.0f}' + ' ' + units_rt['rpm'])
                                 ),
                      secondary_y=False,
                      row=3, col=1
                      )
        # Torque
        fig.add_trace(go.Scatter(x=df_rt.index,
                                 y=df_rt['torque'],
                                 mode='lines',
                                 name='TQ',
                                 hovertemplate=('%{y:.1f}' + ' ' + units_rt['torque'])
                                 ),
                      secondary_y=False,
                      row=3, col=1
                      )

        # Hookload
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['hookload'],
                                 mode='lines',
                                 name='HKLD',
                                 hovertemplate=('%{y:.0f}' + ' ' + units_rt['hookload'])),
                      secondary_y=True,
                      row=3, col=1
                      )

        # WOB
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['wob'],
                                 mode='lines',
                                 name='WOB',
                                 hovertemplate=('%{y:.1f}' + ' ' + units_rt['wob'])
                                 ),
                      secondary_y=False,
                      row=3, col=1
                      )

        # ROP
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['rop'],
                                 mode='lines',
                                 name='ROP',
                                 hovertemplate=('%{y:.0f}' + ' ' + units_rt['rop'])
                                 ),
                      secondary_y=False,
                      row=3, col=1
                      )

        # Standpipe pressure
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['spp'],
                                 mode='lines',
                                 name='SPPA',
                                 hovertemplate=('%{y:,.0f}' + ' ' + units_rt['spp'])
                                 ),
                      secondary_y=False,
                      # yaxis="",
                      row=2, col=1
                      )

        # Surface backpressure (SBP)
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['sbp'],
                                 mode='lines',
                                 name='SBP',
                                 hovertemplate=('%{y:,.0f}' + ' ' + units_rt['sbp'])
                                 ),
                      secondary_y=False,
                      # yaxis="",
                      row=2, col=1
                      )
        
        # Wellhead Pressure
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['whp'],
                                 mode='lines',
                                 name='WHP',
                                 hovertemplate=('%{y:,.0f}' + ' ' + units_rt['whp'])
                                 ),
                      secondary_y=False,
                      # yaxis="",
                      row=2, col=1
                      )

        # Flow rate (x100)
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['mfia_multiplier'],
                                 mode='lines',
                                 name='Flow Rate',
                                 hovertemplate=('%{y:.2f}' + f'x{MFIA_MULTIPLIER} {units_rt["mfia"]}')
                                 ),
                      secondary_y=True,
                      # yaxis="",
                      row=2, col=1
                      )

        # Realtime ECD
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['ecd_rt'],
                                 mode='lines',
                                 name='ECD',
                                 hovertemplate=('%{y:.2f}' + ' ' + units_rt['ecd_rt'])
                                 ),
                      secondary_y=True,
                      # yaxis="",
                      row=2, col=1
                      )

        # ESD_MIN
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['esd_min'],
                                 mode='markers',
                                 name='ESD_MIN',
                                 marker_size=ESD_MARKER_SIZE,
                                 hovertemplate=('%{y:.2f}' + ' ' + units_rt['esd_min'])
                                 ),
                      secondary_y=True,
                      # yaxis="",
                      row=2, col=1
                      )

        # ESD_MAX
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['esd_max'],
                                 mode='markers',
                                 name='ESD_MAX',
                                 marker_size=ESD_MARKER_SIZE,
                                 hovertemplate=('%{y:.2f}' + ' ' + units_rt['esd_max'])
                                 ),
                      secondary_y=True,
                      # yaxis="",
                      row=2, col=1
                      )

        # ESD_AVG
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['esd_avg'],
                                 mode='markers',
                                 name='ESD_AVG',
                                 marker_size=ESD_MARKER_SIZE,
                                 hovertemplate=('%{y:.2f}' + ' ' + units_rt['esd_avg'])
                                 ),
                      secondary_y=True,
                      # yaxis="",
                      row=2, col=1
                      )

        # MW In 
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['mw_in'],
                                 mode='lines',
                                 name='MW In',
                                 hovertemplate=('%{y:.2f}' + ' ' + units_rt['mw_in'])),
                      secondary_y=True,
                      # yaxis="",
                      row=2, col=1
                      )

        # MW Out
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['mw_out'],
                                 mode='lines',
                                 name='MW Out',
                                 hovertemplate=('%{y:.2f}' + ' ' + units_rt['mw_out'])
                                 ),
                      secondary_y=True,
                      # yaxis="",
                      row=2, col=1
                      )
        
    if df_mem is not None:
        # Memory ECD
        fig.add_trace(go.Scatter(x=df_mem.index, y=df_mem['ecd_mem'],
                                 mode='lines',
                                 name='Memory ECD',
                                 hovertemplate=('%{y:.2f}' + ' ' + units_mem['ecd_mem'])
                                 ),
                      secondary_y=True,
                      # yaxis="",
                      row=2, col=1
                      )

        # MWD Temperature (Memory)
        fig.add_trace(go.Scatter(x=df_mem.index, y=df_mem['mwd_temp_mem'],
                                 mode='markers',
                                 name='MWD Temp (Mem)',
                                 hovertemplate=('%{y:,.0f}' + ' ' + units_mem['mwd_temp_mem'])
                                 ),
                      row=1, col=1, 
                      secondary_y=True
                      )

    # Add axis titles
    fig.update_yaxes(row=1, col=1, secondary_y=False,
                     title_text=f'Bit Depth ({units_rt["bit_depth"]})', 
                     autorange='reversed')

    fig.update_yaxes(row=1, col=1, secondary_y=True,
                     title_text=f'Gas({units_rt["gas"]})/Temperature({units_rt["mwd_temp"]})')

    fig.update_yaxes(row=2, col=1, secondary_y=False,
                     title_text=f'Pressure ({units_rt["spp"]})')

    # Use mean ECD to configure axis range
    ecd_mean = round(df_rt['ecd_rt'].mean(), 1)
    fig.update_yaxes(row=2, col=1, secondary_y=True,
                    #  range=[(ecd_mean - 1), (ecd_mean + 1)],
                     range=[8, 14],
                     title_text=f'ECD/ESD/MW ({units_rt["ecd_rt"]})/Flow x{MFIA_MULTIPLIER} ({units_rt["mfia"]})')

    fig.update_yaxes(row=3, col=1, secondary_y=False,
                     range=[0, 300],
                     title_text=(f'BPOS ({units_rt["block_position"]})/RPM/TQ ({units_rt["torque"]})/WOB ({units_rt["wob"]})/ROP ({units_rt["rop"]})'))

    fig.update_yaxes(row=3, col=1, secondary_y=True,
                     title_text=f'Hookload ({units_rt["hookload"]})')

    # Horizontal line to show max pore pressure
    fig.add_hline(y=MAX_PP_OH, row=2, col=1, secondary_y=True) 
    fig.add_annotation(
        text="Max PP in Open Hole",
        x=max(df_rt.index.max(), df_mem.index.max()),
        y=MAX_PP_OH,
        yshift=-10, 
        xshift=10,
        secondary_y=True,
        row=2, col=1, 
        showarrow=False, 
        xanchor='right'
    )

    # Add graph title
    fig.update_layout(title=TITLE, title_x=0.5)

    if df_events is not None:
        # Add annotations
        adjustment = 0.2 * (df_rt['bit_depth'].max()
                            - df_rt['bit_depth'].min())
        df_events['y'] = df_rt.loc[df_events.index, 'bit_depth']
        df_events.loc[
            df_events[
                df_events['y'] < df_rt['bit_depth'].mean()]
            .index, 'y_adj'] = df_events['y'] + adjustment
        df_events.loc[
            df_events[
                df_events['y'] > df_rt['bit_depth'].mean()]
            .index, 'y_adj'] = df_events['y'] - adjustment

        annotations = [{
            'x': df_events.index[i],
            'y': df_events.iloc[i, 2],
            'text': df_events.iloc[i, 0],
            'showarrow': False
        } for i in range(len(df_events.index))]
        fig.update_layout({"annotations": annotations})

    fig.update_layout(template='plotly_dark', hovermode='x unified')

    return fig
