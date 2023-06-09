import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots


com1 = pd.read_csv(r'historical_country_Germany_indicator_Inflation_Rate.csv')
com2 = pd.read_csv(r'historical_country_Euro_Area_indicator_Interest_Rate.csv')
com3 = pd.read_csv(r'historical_country_Spain_indicator_Inflation_Rate.csv')
com4 = pd.read_csv(r'historical_country_France_indicator_Inflation_Rate.csv')
com5 = pd.read_csv(r'historical_country_Italy_indicator_Inflation_Rate.csv')


com2 = com2[['DateTime', 'Value']]
com2['DateTime'] = pd.to_datetime(com2['DateTime'])

com3 = com3[['DateTime', 'Value']]
com3['DateTime'] = pd.to_datetime(com3['DateTime'])

com4 = com4[['DateTime', 'Value']]
com4['DateTime'] = pd.to_datetime(com4['DateTime'])

com5 = com5[['DateTime', 'Value']]
com5['DateTime'] = pd.to_datetime(com5['DateTime'])


###DATE RANGE FOR ALL DATA
start_date = "2018-01-01"
end_date = "2023-02-01"

##WHITTLE DOWN COMMODITIES
#COMMODITY ONE
after_start_date = com1['DateTime'] >= start_date
before_end_date = com1['DateTime'] <= end_date
date_range = after_start_date & before_end_date
com1 = com1.loc[date_range]

#COMMODITY TWO
after_start_date = com2['DateTime'] >= start_date
before_end_date = com2['DateTime'] <= end_date
date_range = after_start_date & before_end_date
com2 = com2.loc[date_range]

#COMMODITY THREE
after_start_date = com3['DateTime'] >= start_date
before_end_date = com3['DateTime'] <= end_date
date_range = after_start_date & before_end_date
com3 = com3.loc[date_range]

#COMMODITY FOUR
after_start_date = com4['DateTime'] >= start_date
before_end_date = com4['DateTime'] <= end_date
date_range = after_start_date & before_end_date
com4 = com4.loc[date_range]

#COMMODITY FIVE
after_start_date = com5['DateTime'] >= start_date
before_end_date = com5['DateTime'] <= end_date
date_range = after_start_date & before_end_date
com5 = com5.loc[date_range]


##FORMAT AS STANDARD GPM GRAPH
trace1 = go.Scatter(x=com1['DateTime'], y=com1['Value'], name="Germany Inflation", mode='lines', line=dict(width=2.5, color='#C33C54'))
trace2 = go.Scatter(x=com2['DateTime'], y=com2['Value'], name='ECB Interest Rate', mode='lines', fill='tozeroy', line=dict(width=2.5, color='rgba(245,125,108, 0.5)'))
trace3 = go.Scatter(x=com3['DateTime'], y=com3['Value'], name="Spain Inflation", mode='lines', line=dict(width=2.5, color='#694966'))
trace4 = go.Scatter(x=com4['DateTime'], y=com4['Value'], name="France Inflation", mode='lines', line=dict(width=2.5, color='#FFF275'))
trace5 = go.Scatter(x=com5['DateTime'], y=com5['Value'], name="Italy Inflation", mode='lines', line=dict(width=2.5, color='#6699CC'))


##CREATE SUBPLOTS
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(trace2, secondary_y=True)
fig.add_trace(trace1)
fig.add_trace(trace3)
fig.add_trace(trace4)
fig.add_trace(trace5)

##DATE RANGES
#COVID
fig.update_layout(
    shapes=[
    dict(
        type="rect",
        xref="x",
        yref="y",
        x0="2019-8-1",
        y0='0',
        x1="2022-1-1",
        y1='13.5',
        fillcolor="lightgray",
        opacity=0.6,
        line_width=0,
        layer="below"),

#GREAT RECESSION
#     dict(
#         type="rect",
#         xref="x",
#         yref="y",
#         x0="2008",
#         y0='0',
#         x1="2010",
#         y1="13.5",
#         fillcolor="lightgray",
#         opacity=0.6,
#         line_width=0,
#         layer="below"
#     )
        ])



##LAYOUT
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    height=466,
    width=970,
    title='<i>Euro Zone Inflation<i>',
    title_font=dict(size=19),
    title_x=0.06,
    margin=dict(b=30, l=25, r=25, t=30),
    title_y=0.9,
    showlegend=True,
    autosize=False,
    font_family="open sans, sans-serif",
    yaxis_title_font=dict(size=11),
    annotations=[dict(
                    x=0.98,
                    y=-0.15,
                    showarrow=False,
                    text="Trading Economics; (c) Geopolitical Monitor",
                    yref="paper",
                    xref="paper",
                    font=dict(size=10)
                    )],
    legend=dict(
                    font=dict(size=12),
                    yanchor='top',
                    y=0.9,
                    xanchor='right',
                    x=0.19),
                    )

##ANNOTATIONS
#GREAT RECESSION
# fig.add_annotation(y='9.5',
#             text="GREAT RECESSION",
#             x='2009',
#             arrowsize=1.5,
#             opacity=0.4,
#             showarrow=False,
#             textangle=-90,
#             font=dict(size=11),
#             )

#COVID
fig.add_annotation(y='8 ',
            text="COVID-19",
            x='2020-11-1',
            arrowsize=1.5,
            opacity=0.4,
            showarrow=False,
            textangle=-90,
            font=dict(size=20),
                )

## LAYOUT ADJUSTMENTS
#Set y-axis titleS
fig.update_yaxes(title_text="Inflation Rate (YoY)")
fig.update_yaxes(title_text='ECB Interest Rate (Percent)', range=[-2, 13], secondary_y=True)
fig.layout.yaxis2.title.update(standoff=0.5, font=dict(size=11))
fig.layout.yaxis.title.update(standoff=0.5)

#Create the box around the plot
fig.update_xaxes(showline=True, linewidth=2, linecolor='#5e5e5e', mirror=True, showgrid=False)
fig.update_yaxes(showline=True, linewidth=2, linecolor='#5e5e5e', mirror=True, showgrid=False, zeroline=False,
                 range=[-2, 13], tickformat=',T')


fig.show()

if not os.path.exists("images"):
    os.mkdir("images")
pio.write_image(fig, 'images/output.png')
