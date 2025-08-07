# 天气查询应用
import requests
import json

def get_weather(city):
    # 使用公开的天气API (这里使用示例API，实际使用时需要注册)
    api_key = "your_api_key"  # 实际使用时替换为真实API密钥
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"
    
    try:
        response = requests.get(complete_url)
        data = response.json()
        
        if data["cod"] != "404":
            main_data = data["main"]
            temperature = main_data["temp"]
            humidity = main_data["humidity"]
            weather_desc = data["weather"][0]["description"]
            
            print(f"\n{city}的天气情况:")
            print(f"温度: {temperature}°C")
            print(f"湿度: {humidity}%")
            print(f"天气状况: {weather_desc.capitalize()}")
        else:
            print("城市未找到")
    except Exception as e:
        print(f"获取天气信息时出错: {e}")

def save_to_file(city, data):
    with open("weather_history.txt", "a") as file:
        file.write(f"{city}: {data}\n")

def weather_app():
    print("天气查询应用程序")
    print("输入'quit'退出程序")
    
    while True:
        city = input("\n请输入城市名称: ")
        
        if city.lower() == 'quit':
            print("感谢使用天气查询应用!")
            break
            
        get_weather(city)

# 启动应用
weather_app()