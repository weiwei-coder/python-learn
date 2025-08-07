# 术语表

本术语表解释了Python学习项目中使用的专业术语和概念，帮助初学者更好地理解项目内容。

## Python基础术语

### 变量 (Variable)
- **定义**: 用于存储数据值的容器
- **示例**: `name = "Alice"` 中的 `name` 就是一个变量
- **相关概念**: 数据类型、赋值、作用域

### 数据类型 (Data Types)
- **定义**: 变量可以存储的数据种类
- **常见类型**:
  - 整数 (int): 如 `42`
  - 浮点数 (float): 如 `3.14`
  - 字符串 (str): 如 `"Hello, World!"`
  - 布尔值 (bool): `True` 或 `False`
  - 列表 (list): 如 `[1, 2, 3]`
  - 字典 (dict): 如 `{"name": "Alice", "age": 25}`
  - 元组 (tuple): 如 `(1, 2, 3)`

### 函数 (Function)
- **定义**: 一段可重复使用的代码块，用于执行特定任务
- **组成部分**: 函数名、参数、函数体、返回值
- **示例**: 
  ```python
  def greet(name):
      return f"Hello, {name}!"
  ```
- **相关概念**: 参数、返回值、作用域、递归

### 控制流 (Control Flow)
- **定义**: 程序执行的顺序控制
- **主要结构**:
  - 条件语句 (if-elif-else): 根据条件执行不同代码块
  - 循环 (for/while): 重复执行代码块
- **示例**:
  ```python
  # 条件语句
  if age >= 18:
      print("成年人")
  else:
      print("未成年人")

  # 循环
  for i in range(5):
      print(i)
  ```

## 数据分析术语

### Pandas
- **定义**: Python的一个数据分析库，提供高性能、易于使用的数据结构和数据分析工具
- **主要数据结构**:
  - Series: 一维带标签数组
  - DataFrame: 二维表格型数据结构
- **官方网站**: [pandas.pydata.org](https://pandas.pydata.org/)

### NumPy
- **定义**: Python的一个科学计算库，提供多维数组对象、派生对象（如掩码数组和矩阵）和用于数组快速操作的各种例程
- **主要特点**:
  - 强大的N维数组对象
  - 广播功能函数
  - 整合C/C++/Fortran代码的工具
- **官方网站**: [numpy.org](https://numpy.org/)

### 数据清洗 (Data Cleaning)
- **定义**: 识别并纠正（或删除）数据中的错误、不一致和不准确之处的过程
- **常见任务**:
  - 处理缺失值
  - 标准化数据格式
  - 删除重复数据
  - 处理异常值

### 数据聚合 (Data Aggregation)
- **定义**: 将多个数据点组合并汇总为单个摘要值的过程
- **常见聚合函数**:
  - sum(): 求和
  - mean(): 计算平均值
  - median(): 计算中位数
  - min()/max(): 计算最小/最大值
  - count(): 计数

## Web开发术语

### API (Application Programming Interface)
- **定义**: 应用程序编程接口，定义了软件组件之间的交互方式
- **在本项目中的使用**: 使用OpenWeatherMap API获取天气数据
- **相关概念**: RESTful API、HTTP请求、JSON

### Flask
- **定义**: 一个用Python编写的轻量级Web应用框架
- **特点**:
  - 轻量级和模块化
  - 内置开发服务器和调试器
  - 支持单元测试
- **官方网站**: [flask.palletsprojects.com](https://flask.palletsprojects.com/)

### HTTP请求 (HTTP Request)
- **定义**: 客户端向服务器发送的请求消息
- **主要方法**:
  - GET: 获取资源
  - POST: 提交数据
  - PUT: 更新资源
  - DELETE: 删除资源
- **在本项目中的使用**: 使用requests库发送HTTP请求获取天气数据

### JSON (JavaScript Object Notation)
- **定义**: 一种轻量级的数据交换格式
- **特点**:
  - 易于人阅读和编写
  - 易于机器解析和生成
  - 基于JavaScript编程语言的一个子集
- **示例**:
  ```json
  {
    "name": "John",
    "age": 30,
    "city": "New York"
  }
  ```

## 开发工具术语

### 虚拟环境 (Virtual Environment)
- **定义**: 一个隔离的Python环境，允许您为特定项目安装依赖包，而不影响全局Python安装
- **优点**:
  - 避免包版本冲突
  - 保持项目依赖隔离
  - 便于重现环境
- **相关工具**: venv, virtualenv, conda

### PIP (Package Installer for Python)
- **定义**: Python的包管理系统，用于安装和管理Python包
- **常用命令**:
  - `pip install package_name`: 安装包
  - `pip uninstall package_name`: 卸载包
  - `pip list`: 列出已安装的包
  - `pip freeze > requirements.txt`: 将当前环境中的包列表保存到文件

### Jupyter Notebook
- **定义**: 一个交互式计算环境，允许您创建和共享包含实时代码、方程式、可视化和叙述性文本的文档
- **特点**:
  - 支持多种编程语言（主要是Python）
  - 交互式数据探索和可视化
  - 便于分享和协作
- **官方网站**: [jupyter.org](https://jupyter.org/)

## 其他术语

### 代码注释 (Code Comments)
- **定义**: 在代码中添加的解释性文本，帮助理解代码功能
- **目的**:
  - 解释复杂逻辑
  - 提供使用说明
  - 标记待办事项
- **Python中的注释方式**:
  - 单行注释: `# 这是一个注释`
  - 多行注释: `"""这是一个多行注释"""`

### 文档字符串 (Docstring)
- **定义**: Python中用于描述模块、函数、类或方法的字符串
- **目的**: 提供代码文档，可以通过`help()`函数访问
- **示例**:
  ```python
  def greet(name):
      """
      向指定的人问好

      参数:
          name (str): 要问候的人名

      返回:
          str: 问候语
      """
      return f"Hello, {name}!"
  ```

### 异常处理 (Exception Handling)
- **定义**: 程序运行时处理错误和异常的机制
- **目的**: 防止程序因错误而崩溃，提供优雅的错误处理
- **Python中的实现**:
  ```python
  try:
      # 可能引发异常的代码
      result = 10 / 0
  except ZeroDivisionError:
      # 处理特定异常
      print("不能除以零")
  except Exception as e:
      # 处理其他异常
      print(f"发生错误: {e}")
  finally:
      # 无论是否发生异常都会执行的代码
      print("执行完毕")
  ```

### 语义化版本 (Semantic Versioning)
- **定义**: 一种版本号命名规范，格式为MAJOR.MINOR.PATCH
- **规则**:
  - MAJOR版本号：当有不兼容的API修改时递增
  - MINOR版本号：当添加向下兼容的功能时递增
  - PATCH版本号：当进行向下兼容的问题修复时递增
- **示例**: `1.0.0`, `1.0.1`, `1.1.0`, `2.0.0`
- **官方网站**: [semver.org](https://semver.org/)
