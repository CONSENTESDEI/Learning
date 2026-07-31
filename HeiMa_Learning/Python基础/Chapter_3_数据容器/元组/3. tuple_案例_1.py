# 1. 变量值交换
a = 10
b = 20
c = 30
d = 40
# 普通交换
t = a
a = b
b = t
print(f'a = {a}, b = {b}')
# 元组交换
c, d = (d, c)
print(f'c = {c}, d = {d}')
# 多变量交换
a1, a2, a3 = 1, 2, 3
a1, a2, a3 = (a3, a1, a2)
print(f'a1 = {a1}, a2 = {a2}, a3 = {a3}')