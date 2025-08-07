# Stage 4: API应用

本阶段介绍如何使用Python调用第三方API，开发实用的应用程序。

## 学习目标

- 理解API的基本概念和工作原理
- 学习使用requests库发送HTTP请求
- 掌握JSON数据的处理方法
- 了解如何处理API响应和错误

## 示例代码说明

- `demo.py`: 展示一个天气查询应用，使用OpenWeatherMap API获取天气信息

## 运行示例

1. 首先，您需要从[OpenWeatherMap](https://openweathermap.org/api)获取免费的API密钥
2. 将代码中的`your_api_key`替换为您获取的API密钥
3. 运行程序：

```bash
python stage4/demo.py
```

## 知识点

- HTTP请求（GET方法）
- API密钥的使用
- JSON数据解析
- 异常处理
- 文件操作

## 练习建议

1. 扩展天气应用，添加更多天气信息（如风速、气压等）
2. 实现多城市天气查询功能
3. 添加历史记录功能，保存用户查询过的城市天气
4. 尝试使用其他公共API（如新闻、汇率等）创建类似应用

## 注意事项

- API密钥是敏感信息，实际项目中应使用环境变量或配置文件存储
- 免费API通常有请求频率限制，请注意不要超过限制
- 处理API响应时，应考虑各种可能的错误情况

## 扩展学习

- [Requests库文档](https://requests.readthedocs.io/)
- [JSON处理](https://docs.python.org/3/library/json.html)
- [OpenWeatherMap API文档](https://openweathermap.org/api)
