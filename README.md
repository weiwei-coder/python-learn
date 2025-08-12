# Python学习项目

这是一个循序渐进的Python学习项目，通过5个不同阶段的示例代码，帮助学习者从基础语法逐步过渡到实际应用开发。

## 项目简介

本项目专为Python初学者设计，通过实践导向的学习方式，帮助学习者从零开始掌握Python编程。项目采用阶段性学习路径，每个阶段都包含理论知识和实践代码，让学习者在动手实践中掌握Python的核心概念和应用技能。

### 适用人群

- 编程初学者
- 想要系统学习Python的开发者
- 希望通过项目实践巩固Python知识的学习者
- 对数据分析和Web开发感兴趣的Python学习者

## 项目结构

项目分为5个阶段，难度递增：

- **Stage 1**: Python基础 - 变量、数据类型和基本语法
- **Stage 2**: 函数定义与使用 - 学习如何定义和调用函数，参数传递
- **Stage 3**: 控制流与交互 - 条件语句、循环和用户交互
- **Stage 4**: API应用 - 使用第三方API开发实际应用
- **Stage 5**: Web开发 - 使用Flask框架创建简单的Web应用

- **data_analysis**: 数据分析模块 - 使用Pandas和NumPy进行数据分析
- **automation**: 自动化脚本 - 文件处理、网页爬取等自动化任务
- **examples**: 实用示例集合 - 各种Python应用场景的代码示例

## 安装说明

### 基本要求
- Python 3.7 或更高版本
- pip (Python包管理器)

### 创建虚拟环境（强烈推荐）
```bash
# Windows
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 安装依赖
```bash
pip install -r requirements.txt
```

## 使用指南

### Stage 1-3
这些阶段的示例代码可以直接运行：
```bash
python basic/stage1/demo1.py
```

### Stage 4
运行天气查询应用：
```bash
python basic/stage4/demo.py
```
注意：您需要获取OpenWeatherMap的API密钥并替换代码中的`your_api_key`。

### Stage 5
运行Flask Web应用：
```bash
cd basic/stage5/demo
python main.py
```
然后在浏览器中访问 `http://127.0.0.1:5000/`

### 数据分析模块
运行Pandas数据分析示例：
```bash
python data_analysis/test_pandas.py
```

## 学习路径建议

1. **基础阶段**：从Stage 1到Stage 3，掌握Python核心语法和编程概念
2. **实践阶段**：完成Stage 4和Stage 5，学习如何将Python应用到实际开发中
3. **探索阶段**：尝试数据分析、自动化脚本等模块，探索Python在不同领域的应用
4. **进阶阶段**：阅读示例集合中的代码，学习最佳实践和设计模式
5. **项目实践**：尝试构建自己的项目，将所学知识融会贯通

每个阶段都应该：
- 仔细阅读代码示例
- 尝试修改代码，观察结果变化
- 完成每个阶段README中推荐的练习
- 思考如何将所学应用到实际问题中

## 常见问题

### Q: 如何获取OpenWeatherMap的API密钥？
A: 访问[OpenWeatherMap官网](https://openweathermap.org/api)，注册账户后即可获取免费API密钥。

### Q: 运行代码时遇到模块导入错误怎么办？
A: 请确保已正确安装所有依赖，可以使用`pip install -r requirements.txt`重新安装。

### Q: 如何提出问题或贡献代码？
A: 请参考CONTRIBUTING.md文件中的指南。

## 扩展学习资源

### 文档与教程
- [Python官方文档](https://docs.python.org/3/)
- [Flask官方文档](https://flask.palletsprojects.com/)
- [Requests库文档](https://requests.readthedocs.io/)
- [Pandas官方文档](https://pandas.pydata.org/docs/)
- [NumPy官方文档](https://numpy.org/doc/stable/)

### 在线学习平台
- [Real Python](https://realpython.com/) - 提供高质量的Python教程
- [Python.org官方教程](https://docs.python.org/3/tutorial/index.html) - Python官方提供的教程
- [W3Schools Python教程](https://www.w3schools.com/python/) - 适合初学者的互动教程

### 社区与支持
- [Python Subreddit](https://www.reddit.com/r/Python/) - Python社区讨论
- [Stack Overflow Python标签](https://stackoverflow.com/questions/tagged/python) - 编程问答社区
- [Python Discord社区](https://discord.gg/python) - 实时交流社区

## 版本信息

当前版本: 1.1.0

最近更新: 2023-12-01

更新内容:
- 添加自动化脚本模块
- 添加更多实用示例
- 完善项目文档
- 优化示例代码
- 增强错误处理机制
- 添加单元测试示例

## 维护者

本项目由Python学习社区维护。如有问题或建议，请通过以下方式联系：
- 邮箱: contact@python-learn.com
- GitHub Issues: [提交问题](https://github.com/weiwei-coder/python-learn/issues)

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。

## 致谢

感谢所有为本项目做出贡献的开发者和学习者！
