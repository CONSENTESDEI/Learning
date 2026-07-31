"""
for 元素 in 数据集:
    循环代码
else:
    结束语
"""

# 字符串循环查找
msg = "hello world!"
for i in msg:
    print(f"{i}")
else:
    print("over")

#range
"""
range(end) 从 0 到 end
range(start, end) 从 start 到 end
range(start, end, step) step 步长
"""

# 100-500，3的倍数之和
sum = 0
for i in range(100, 500):
    if i % 3 == 0:
        sum += i
else:
    print(f"{sum}")