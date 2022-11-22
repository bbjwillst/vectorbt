import numpy as np
import pandas as pd
import vectorbt as vbt


price_close = pd.read_csv("datas/600980.csv")['close']

rsi = vbt.RSI.run(price_close, window=14, short_name="rsi")

num = 10
entry_points = np.linspace(10, 20, num=num, dtype=int)
exit_points = np.linspace(60, 80, num=num, dtype=int)
grid = np.array(np.meshgrid(entry_points, exit_points)).T.reshape(-1, 2)

entries = rsi.rsi_crossed_below(list(grid[:, [0]]))
exits = rsi.rsi_crossed_above(list(grid[:, [1]]))

pf = vbt.Portfolio.from_signals(price_close, entries, exits)
print(pf.stats())