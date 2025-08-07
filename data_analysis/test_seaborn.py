import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 指定本地数据集路径
local_path = "tips.csv"  # 替换为实际的文件路径

# 检查文件是否存在
if os.path.exists(local_path):
    # 使用pandas读取本地CSV文件
    tips = pd.read_csv(local_path)
else:
    print("数据集文件未找到，请检查路径是否正确")

# 加载示例数据集
# tips = sns.load_dataset('tips')

# 散点图
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time')
plt.show()

# 箱线图
sns.boxplot(data=tips, x='day', y='total_bill')
plt.show()

# 热力图
corr = tips.corr()
sns.heatmap(corr, annot=True)
plt.show()