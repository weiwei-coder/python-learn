# 字典使用
# 创建一个学生字典
student = {
    "name": "张三",
    "age": 20,
    "major": "计算机科学"
}

# 访问和修改字典
print(f"{student['name']}的专业是{student['major']}")
student["age"] = 21  # 更新年龄

# 遍历字典
for key, value in student.items():
    print(f"{key}: {value}")