"""
1. 输入 10 个数字，存储到列表中
2. 将列表进行排序
3. 输出其中最值 平均值
"""

# 1. 创建
s1 = []

# 2. 存入
for i in range(10):
    s1.append(int(input("请输入数字")))
print(s1)

# 3，排序
s1.sort()
print(s1)

# 4. 找最值
print(f'min = {s1[0]}\nmax = {s1[-1]}')
print(f'min = {min(s1)}\nmax = {max(s1)}\n')
# 5. 算平均值
print(f'平均值 = {sum(s1) / len(s1)}')



