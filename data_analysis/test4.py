import pandas as pd
import numpy as np
import seaborn as sns
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

# 使用之前的销售数据
pivot = pd.pivot_table(sales, 
                      values='销售额', 
                      index='产品', 
                      columns='地区', 
                      aggfunc=np.sum,
                      fill_value=0)
print(pivot)

# 热力图可视化
sns.heatmap(pivot, annot=True, fmt="d", cmap="YlGnBu")
plt.title("各地区产品销售热力图")
plt.show()