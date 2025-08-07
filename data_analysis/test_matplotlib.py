import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 创建DataFrame
data = {
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 35],
    '城市': ['北京', '上海', '广州']
}
df = pd.DataFrame(data)

# 折线图
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("简单折线图")
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.show()

# 柱状图
plt.bar(df['姓名'], df['年龄'])
plt.title("年龄分布")
plt.show()