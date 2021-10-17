import plotly.graph_objects as go
from plotly.subplots import make_subplots
from config import TITLE, ESD_MARKER_SIZE, MAX_PP_OH

""" Creates plot with Plotly based on three dataframes: realtime data (from
BPWA), memory data (from .las file) and user-defined 'events' (.csv).

Dataframes are generated in process_data.py.
"""


def create_drilling_plot(df_rt, df_mem, df_events):

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
                                 hovertemplate='%{y:,.0f} ft MD'),
                      row=1, col=1, 
                      secondary_y=False
                      )
                      
        # Gas
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['gas'],
                                 mode='lines',
                                 name='Gas',
                                 hovertemplate='%{y:,.1f} units'),
                      row=1, col=1, 
                      secondary_y=True,
                      )

        # MWD Temperature (RT)
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['mwd_temp'],
                                 mode='markers',
                                 name='MWD Temp (RT)',
                                 hovertemplate='%{y:,.0f}°F'),
                      row=1, col=1, 
                      secondary_y=True
                      )

        # Block position
        fig.add_trace(go.Scatter(x=df_rt.index,
                                 y=df_rt['block_position'],
                                 mode='lines',
                                 name='BPOS',
                                 hovertemplate='%{y:.1f} ft'),
                      secondary_y=False,
                      row=3, col=1
                      )

        # RPM
        fig.add_trace(go.Scatter(x=df_rt.index,
                                 y=df_rt['rpm'],
                                 mode='lines',
                                 name='RPM',
                                 hovertemplate='%{y:.0f}'),
                      secondary_y=False,
                      row=3, col=1
                      )
        # Torque
        fig.add_trace(go.Scatter(x=df_rt.index,
                                 y=df_rt['torque'],
                                 mode='lines',
                                 name='TQ',
                                 hovertemplate='%{y:.1f} kft-lbs'),
                      secondary_y=False,
                      row=3, col=1
                      )

        # Hookload
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['hookload'],
                                 mode='lines',
                                 name='HKLD',
                                 hovertemplate='%{y:.0f} klbs'),
                      secondary_y=True,
                      row=3, col=1
                      )

        # WOB
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['wob'],
                                 mode='lines',
                                 name='WOB',
                                 hovertemplate='%{y:.1f} klbs'),
                      secondary_y=False,
                      row=3, col=1
                      )

        # ROP
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['rop'],
                                 mode='lines',
                                 name='ROP',
                                 hovertemplate='%{y:.0f} klbs'),
                      secondary_y=False,
                      row=3, col=1
                      )

        # Standpipe pressure
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['spp'],
                                 mode='lines',
                                 name='SPPA',
                                 hovertemplate='%{y:,.0f} psi'),
                      secondary_y=False,
                      # yaxis="",
                      row=2, col=1
                      )
        
        # Wellhead Pressure
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['whp'],
                                 mode='lines',
                                 name='WHP',
                                 hovertemplate='%{y:,.0f} psi'),
                      secondary_y=False,
                      # yaxis="",
                      row=2, col=1
                      )

        # Realtime ECD
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['ecd_rt'],
                                 mode='lines',
                                 name='ECD',
                                 hovertemplate='%{y:.2f} ppg'),
                      secondary_y=True,
                      # yaxis="",
                      row=2, col=1
                      )

        # ESD_MIN
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['esd_min'],
                                 mode='markers',
                                 name='ESD_MIN',
                                 marker_size=ESD_MARKER_SIZE,
                                 hovertemplate='%{y:.2f} ppg'),
                      secondary_y=True,
                      # yaxis="",
                      row=2, col=1
                      )

        # ESD_MAX
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['esd_max'],
                                 mode='markers',
                                 name='ESD_MAX',
                                 marker_size=ESD_MARKER_SIZE,
                                 hovertemplate='%{y:.2f} ppg'),
                      secondary_y=True,
                      # yaxis="",
                      row=2, col=1
                      )

        # ESD_AVG
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['esd_avg'],
                                 mode='markers',
                                 name='ESD_AVG',
                                 marker_size=ESD_MARKER_SIZE,
                                 hovertemplate='%{y:.2f} ppg'),
                      secondary_y=True,
                      # yaxis="",
                      row=2, col=1
                      )

        # MW In 
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['mw_in'],
                                 mode='lines',
                                 name='MW In',
                                 hovertemplate='%{y:.2f} ppg'),
                      secondary_y=True,
                      # yaxis="",
                      row=2, col=1
                      )

        # MW Out
        fig.add_trace(go.Scatter(x=df_rt.index, y=df_rt['mw_out'],
                                 mode='lines',
                                 name='MW Out',
                                 hovertemplate='%{y:.2f} ppg'),
                      secondary_y=True,
                      # yaxis="",
                      row=2, col=1
                      )
        
    if df_mem is not None:
        # Memory ECD
        fig.add_trace(go.Scatter(x=df_mem.index, y=df_mem['ecd_mem'],
                                 mode='lines',
                                 name='Memory ECD',
                                 hovertemplate='%{y:.2f} ppg'),
                      secondary_y=True,
                      # yaxis="",
                      row=2, col=1
                      )

        # MWD Temperature (Memory)
        fig.add_trace(go.Scatter(x=df_mem.index, y=df_mem['mwd_temp_mem'],
                                 mode='markers',
                                 name='MWD Temp (Mem)',
                                 hovertemplate='%{y:,.0f}°F'),
                      row=1, col=1, 
                      secondary_y=True
                      )

    # Add axis titles
    fig.update_yaxes(row=1, col=1, secondary_y=False,
                     title_text='Bit Depth (ft MD)')
    fig.update_yaxes(row=1, col=1, secondary_y=True,
                     title_text='Gas(units)/Temperature(°F)')
    fig.update_yaxes(row=2, col=1, secondary_y=False,
                     title_text='Pressure (psi)')
    # Use mean ECD to configure axis range
    ecd_mean = round(df_rt['ecd_rt'].mean(), 1)
    fig.update_yaxes(row=2, col=1, secondary_y=True,
                     range=[(ecd_mean - 1), (ecd_mean + 1)],
                     title_text='ECD/ESD/MW (ppg)')
    fig.update_yaxes(row=3, col=1, secondary_y=False,
                     range=[0, 300],
                     title_text='BPOS (ft)/RPM/TQ (kft-lbs)/WOB (klbs)')
    fig.update_yaxes(row=3, col=1, secondary_y=True,
                     title_text='Hookload (klbs)')

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
