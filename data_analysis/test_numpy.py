# NumPy - 数值计算基础
import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 基本运算
print(arr + 2)  # 每个元素加2
print(arr * 3)  # 每个元素乘3

# 多维数组
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("矩阵形状:", matrix.shape)

# 常用函数
print("平均值:", np.mean(arr))
print("标准差:", np.std(arr))
print("最大值:", np.max(arr))