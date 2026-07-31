# input

# 案例：简单取款取款
# 总金额
total = 10000

# 1.输入密码
password = input("请输入你的密码：")
print(f"密码正确，{password}")

# 2.输入全款额度
num = input("请输入取款额度：")

# 3.计算输出 --> 转int --> 类型转换
print(f"取款成功，所剩余额为：{total - int(num)}")