# 简易计算器
def calculator():
    print("简易计算器")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    
    choice = input("请选择操作(1/2/3/4): ")
    num1 = float(input("输入第一个数字: "))
    num2 = float(input("输入第二个数字: "))
    
    if choice == '1':
        print(f"结果: {num1 + num2}")
    elif choice == '2':
        print(f"结果: {num1 - num2}")
    elif choice == '3':
        print(f"结果: {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"结果: {num1 / num2}")
        else:
            print("错误: 除数不能为零!")
    else:
        print("无效输入")

calculator()