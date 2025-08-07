import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 假设我们有销售数据
data = {
    '日期': pd.date_range(start='2023-01-01', periods=100),
    '产品': np.random.choice(['A', 'B', 'C'], 100),
    '销售额': np.random.randint(100, 1000, 100),
    '地区': np.random.choice(['东区', '西区', '南区', '北区'], 100)
}
sales = pd.DataFrame(data)

# 分析各产品销售额
product_sales = sales.groupby('产品')['销售额'].sum().sort_values(ascending=False)
product_sales.plot(kind='bar')
plt.title("各产品销售额")
plt.show()

# 销售额时间趋势
sales.set_index('日期')['销售额'].resample('W').sum().plot()
plt.title("每周销售额趋势")
plt.show()