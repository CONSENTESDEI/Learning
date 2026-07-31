i = 1
user_name = "carol"
password = "0123"
while i <= 3:
    user_name_input = input("输入用户名")
    password_input = input("输入密码")
    if((user_name_input, password_input) != (user_name, password)):
        print("请重试")
        i += 1
    else:
        print("登陆成功")
        break
else:
    print("请等待")