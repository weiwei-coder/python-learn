# Python学习项目

这是一个循序渐进的Python学习项目，通过5个不同阶段的示例代码，帮助学习者从基础语法逐步过渡到实际应用开发。

## 项目结构

项目分为5个阶段，难度递增：

- **Stage 1**: Python基础 - 变量、输出和基本语法
- **Stage 2**: 函数定义与使用 - 学习如何定义和调用函数
- **Stage 3**: 控制流与交互 - 条件语句、循环和用户交互
- **Stage 4**: API应用 - 使用第三方API开发实际应用
- **Stage 5**: Web开发 - 使用Flask框架创建简单的Web应用

## 安装说明

### 基本要求
- Python 3.6 或更高版本

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
python stage1/demo1.py
```

### Stage 4
运行天气查询应用：
```bash
python stage4/demo.py
```
注意：您需要获取OpenWeatherMap的API密钥并替换代码中的`your_api_key`。

### Stage 5
运行Flask Web应用：
```bash
cd stage5/demo
python main.py
```
然后在浏览器中访问 `http://127.0.0.1:5000/`

## 学习路径建议

1. 从Stage 1开始，按顺序学习每个阶段的示例
2. 尝试修改代码，观察结果变化
3. 完成每个阶段README中推荐的练习
4. 在掌握基础知识后，尝试扩展项目功能

## 扩展学习资源

- [Python官方文档](https://docs.python.org/3/)
- [Flask官方文档](https://flask.palletsprojects.com/)
- [Requests库文档](https://requests.readthedocs.io/)

## 许可证

本项目仅用于学习目的。
