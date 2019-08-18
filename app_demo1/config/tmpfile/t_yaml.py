import yaml

file = open('..//baidu.yaml', 'r', encoding="utf-8")
file_data = file.read()
file.close()

# 将字符串转化为字典或列表
print("***转化yaml数据为字典或列表***")
data = yaml.load(file_data)

print(data)
print(data["search"])
print(data["search"]["搜索框"])