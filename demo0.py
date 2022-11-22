import vectorbt as vbt
import numpy as np
import pandas as pd
import vectorbt.indicators.factory
import yfinance as yf


price_close = pd.read_csv("datas/600980.csv")[["close"]]

windows = np.arange(2, 101)
fast_ma, slow_ma = vbt.MA.run_combs(price_close, window=windows, r=2, short_names=['fast', 'slow'])
entries = fast_ma.ma_crossed_above(slow_ma)
exits = fast_ma.ma_crossed_below(slow_ma)

pf_kwargs = dict(size=np.inf, fees=0.0005, freq='1D')
pf = vbt.Portfolio.from_signals(price_close, entries, exits, **pf_kwargs)

fig = pf.total_return().vbt.heatmap(x_level='fast_window', y_level='slow_window', slider_level='symbol',
                                    symmetric=True, trace_kwargs=dict(colorbar=dict(title='Total return', tickformat='%')))
fig.show()