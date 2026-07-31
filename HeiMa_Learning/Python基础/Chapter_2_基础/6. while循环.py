"""
while 条件:
    循环语句1
    循环语句2
    ...
与else合并使用
else:
    输出结束
"""

# 计算1-100偶函数和
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
else:   # 可直接print，但会出错
    print(f"1-100偶函数和为：{sum}")
