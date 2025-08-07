import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 创建时间序列数据
date_rng = pd.date_range(start='1/1/2023', end='1/08/2023', freq='D')
ts = pd.Series(np.random.randn(len(date_rng)), index=date_rng)

# 滚动平均
rolling_mean = ts.rolling(window=5).mean()

# 绘图
plt.figure(figsize=(12,6))
plt.plot(ts, label='原始数据')
plt.plot(rolling_mean, label='5天滚动平均', color='red')
plt.legend()
plt.show()