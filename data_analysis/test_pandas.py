#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pandas数据分析示例

本示例展示了Pandas库的基本操作，包括Series和DataFrame的创建、数据选择、过滤、
分组聚合等常见数据分析任务。通过这些示例，您可以了解如何使用Pandas进行数据
清洗、转换和分析。

作者: Python学习项目
日期: 2023-11-15
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def create_series():
    """
    创建Pandas Series对象并展示其基本属性

    Series是Pandas中的一维数组，可以存储任何数据类型。
    它类似于带标签的数组（类似字典）。

    返回:
        pd.Series: 创建的Series对象
    """
    print("=" * 50)
    print("创建Series对象")
    print("=" * 50)

    # 创建一个简单的Series，包含整数和缺失值(NaN)
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print("创建的Series:")
    print(s)

    # 展示Series的属性
    print("
Series的属性:")
    print(f"索引: {s.index}")
    print(f"值: {s.values}")
    print(f"数据类型: {s.dtype}")
    print(f"缺失值数量: {s.isna().sum()}")

    return s

def create_dataframe():
    """
    创建Pandas DataFrame对象并展示其基本属性

    DataFrame是Pandas中的二维表格数据结构，可以看作是Series的集合。
    它类似于电子表格或SQL表。

    返回:
        pd.DataFrame: 创建的DataFrame对象
    """
    print("
" + "=" * 50)
    print("创建DataFrame对象")
    print("=" * 50)

    # 使用字典创建DataFrame
    data = {
        '姓名': ['张三', '李四', '王五'],
        '年龄': [25, 30, 35],
        '城市': ['北京', '上海', '广州']
    }
    df = pd.DataFrame(data)
    print("创建的DataFrame:")
    print(df)

    # 展示DataFrame的属性
    print("
DataFrame的属性:")
    print(f"索引: {df.index}")
    print(f"列名: {df.columns}")
    print(f"数据形状: {df.shape}")
    print(f"数据类型:
{df.dtypes}")

    return df

def explore_dataframe(df):
    """
    探索性数据分析

    展示如何使用Pandas查看和分析数据的基本方法。

    参数:
        df (pd.DataFrame): 要分析的DataFrame
    """
    print("
" + "=" * 50)
    print("探索性数据分析")
    print("=" * 50)

    # 查看前几行数据
    print("前5行数据:")
    print(df.head())

    # 查看数据的统计摘要
    print("
数据的统计摘要:")
    print(df.describe())

    # 查看数据的基本信息
    print("
数据的基本信息:")
    print(df.info())

def select_and_filter_data(df):
    """
    数据选择和过滤

    展示如何选择DataFrame中的特定列和行，以及如何根据条件过滤数据。

    参数:
        df (pd.DataFrame): 要处理的DataFrame
    """
    print("
" + "=" * 50)
    print("数据选择和过滤")
    print("=" * 50)

    # 选择单列
    print("选择'姓名'列:")
    print(df['姓名'])

    # 选择多列
    print("
选择'姓名'和'年龄'列:")
    print(df[['姓名', '年龄']])

    # 使用iloc选择行（基于整数位置）
    print("
使用iloc选择第二行:")
    print(df.iloc[1])

    # 使用loc选择行（基于标签）
    print("
使用loc选择前两行:")
    print(df.loc[0:1])

    # 条件过滤
    print("
筛选年龄大于28的记录:")
    print(df[df['年龄'] > 28])

def modify_data(df):
    """
    数据修改

    展示如何向DataFrame添加新列、修改现有数据和处理缺失值。

    参数:
        df (pd.DataFrame): 要修改的DataFrame
    """
    print("
" + "=" * 50)
    print("数据修改")
    print("=" * 50)

    # 添加新列
    df['薪资'] = [5000, 8000, 6000]
    print("添加'薪资'列后的DataFrame:")
    print(df)

    # 修改数据
    print("
将第一行的年龄修改为26:")
    df.loc[0, '年龄'] = 26
    print(df)

    # 处理缺失值
    print("
添加包含缺失值的'奖金'列:")
    df['奖金'] = [1000, np.nan, 1500]
    print(df)

    print("
使用0填充缺失值:")
    df.fillna(0, inplace=True)  # 用0填充缺失值
    print(df)

def group_and_aggregate(df):
    """
    数据分组和聚合

    展示如何按特定列对数据进行分组，并计算聚合统计量。

    参数:
        df (pd.DataFrame): 要处理的DataFrame
    """
    print("
" + "=" * 50)
    print("数据分组和聚合")
    print("=" * 50)

    # 按城市分组并计算平均薪资
    print("按城市分组计算平均薪资:")
    city_salary = df.groupby('城市')['薪资'].mean()
    print(city_salary)

    # 按城市分组并计算多个统计量
    print("
按城市分组计算薪资的多个统计量:")
    city_salary_stats = df.groupby('城市')['薪资'].agg(['mean', 'max', 'min'])
    print(city_salary_stats)

    # 多列分组
    print("
按城市和年龄分组计算平均薪资:")
    # 创建年龄组
    df['年龄组'] = pd.cut(df['年龄'], bins=[0, 30, 40], labels=['30岁以下', '30岁以上'])
    age_city_group = df.groupby(['城市', '年龄组'])['薪资'].mean()
    print(age_city_group)

def visualize_data(df):
    """
    数据可视化

    展示如何使用Matplotlib和Seaborn对Pandas数据进行可视化。

    参数:
        df (pd.DataFrame): 要可视化的DataFrame
    """
    print("
" + "=" * 50)
    print("数据可视化")
    print("=" * 50)

    # 设置中文字体显示
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    try:
        # 创建图表窗口
        plt.figure(figsize=(12, 8))

        # 子图1：按城市分组柱状图
        plt.subplot(2, 2, 1)
        df.groupby('城市')['薪资'].mean().plot(kind='bar', color='skyblue')
        plt.title('各城市平均薪资')
        plt.xlabel('城市')
        plt.ylabel('平均薪资')
        plt.xticks(rotation=0)

        # 子图2：年龄分布直方图
        plt.subplot(2, 2, 2)
        df['年龄'].plot(kind='hist', bins=10, color='lightgreen')
        plt.title('年龄分布')
        plt.xlabel('年龄')
        plt.ylabel('人数')

        # 子图3：薪资箱线图
        plt.subplot(2, 2, 3)
        df.boxplot(column='薪资', by='城市')
        plt.title('各城市薪资分布')
        plt.xlabel('城市')
        plt.ylabel('薪资')

        # 子图4：散点图
        plt.subplot(2, 2, 4)
        plt.scatter(df['年龄'], df['薪资'], color='purple')
        plt.title('年龄与薪资关系')
        plt.xlabel('年龄')
        plt.ylabel('薪资')

        # 调整子图间距
        plt.tight_layout()

        # 保存图表
        plt.savefig('data_analysis.png')
        print("图表已保存为 data_analysis.png")

        # 显示图表（在某些环境中可能不会显示）
        plt.show()

    except Exception as e:
        print(f"创建图表时出错: {e}")
        print("请确保已安装matplotlib库: pip install matplotlib")

def main():
    """
    主函数，执行所有数据分析示例
    """
    print("Pandas数据分析示例")
    print("本示例展示了Pandas库的基本操作，包括数据创建、选择、修改、分组聚合和可视化。")

    # 创建Series
    s = create_series()

    # 创建DataFrame
    df = create_dataframe()

    # 探索性数据分析
    explore_dataframe(df)

    # 数据选择和过滤
    select_and_filter_data(df)

    # 数据修改
    modify_data(df)

    # 数据分组和聚合
    group_and_aggregate(df)

    # 数据可视化
    visualize_data(df)

    print("
" + "=" * 50)
    print("数据分析示例完成")
    print("=" * 50)

if __name__ == "__main__":
    main()
