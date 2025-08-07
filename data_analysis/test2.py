import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 生成模拟客户数据
np.random.seed(42)
customer_data = pd.DataFrame({
    '年龄': np.random.randint(18, 70, 200),
    '年收入(万)': np.random.randint(5, 50, 200),
    '消费频率': np.random.randint(1, 20, 200)
})

# 数据标准化
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(customer_data)

# K-Means聚类
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

# 可视化聚类结果
customer_data['聚类'] = clusters
sns.scatterplot(data=customer_data, x='年收入(万)', y='消费频率', hue='聚类', palette='viridis')
plt.title("客户细分")
plt.show()