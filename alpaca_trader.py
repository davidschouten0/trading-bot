from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

import plotly.graph_objects as go
import pandas as pd

# no keys required for crypto data
client = CryptoHistoricalDataClient()

request_params = CryptoBarsRequest(
                        symbol_or_symbols=["BTC/USD", "ETH/USD"],
                        timeframe=TimeFrame.Day,
                        start=datetime.strptime("2022-07-01", '%Y-%m-%d')
                        )

bars = client.get_crypto_bars(request_params)

# convert to dataframe
bars = bars.df

bars = bars.reset_index()

print(bars.head(5))


bars['timestamp'] = pd.to_datetime(bars['timestamp'])

fig = go.Figure()
fig.add_trace(go.Candlestick(x=bars['timestamp'], open=bars['open'], high=bars['high'], low=bars['low'], close=bars['close']))

fig.write_html('mein chart go brrrrr')