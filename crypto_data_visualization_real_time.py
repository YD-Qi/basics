import numpy as np
import pandas as pd
import ccxt
import time
import dateutil
from datetime import datetime
from functools import reduce
from scipy.signal import argrelextrema


import matplotlib.pyplot as plt
import plotly.offline as pyo
import plotly.graph_objs as go
# Set notebook mode to work in offline
pyo.init_notebook_mode()
import plotly.express as px

data = collect_data(timeframe = '4h', limit = 300)

df = data.dropna()

current_time = pd.DataFrame(df[df['Symbol']=='ETH/USDT']['Datetime']).iloc[-1,0]

recent_candles = df[df['Datetime'] == current_time]

import plotly.express as px
fig = px.bar(df, 
             y='Symbol', 
             x='price_ch_24', 
             orientation='h', 
             text='price_ch_24',
             color='Symbol',
             title="<b>币圈风云榜</b>",
             animation_frame='Datetime',
             animation_group='Symbol',
              width=1500, 
             height=1500,
            range_x=[-0.9,1.5])
fig.update_layout(yaxis={'categoryorder':'total ascending'},
                  xaxis=dict(
                      title='24小时价格变化'),
                 showlegend=False)
fig.update_traces(texttemplate='%{text:.1%}', textposition='outside')

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 300
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 300
fig.show()

# Save Chart and export to HTML
import plotly.offline as pyo

pyo.plot(fig, filename="crypto_markets.html")
