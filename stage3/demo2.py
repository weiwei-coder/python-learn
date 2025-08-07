# 待办事项列表
todo_list = []

def show_tasks():
    print("\n当前待办事项:")
    for index, task in enumerate(todo_list, 1):
        print(f"{index}. {task}")

def add_task():
    task = input("请输入新任务: ")
    todo_list.append(task)
    print(f"已添加任务: {task}")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("请输入要删除的任务编号: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num-1)
            print(f"已移除任务: {removed}")
        else:
            print("无效的任务编号")
    except ValueError:
        print("请输入有效的数字")

while True:
    print("\n待办事项管理器")
    print("1. 显示任务")
    print("2. 添加任务")
    print("3. 删除任务")
    print("4. 退出")
    
    choice = input("请选择操作(1/2/3/4): ")
    
    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("再见!")
        break
    else:
        print("无效的选择")