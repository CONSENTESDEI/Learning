"""
特点：
    1. 不可重复
    2. 会自动去重
    3. 无序
    4. 可修改

定义：
    集合名称 = {"元素1"， "元素2"...}
    空集合 集合名称 = set() 不可用 {} 表示空字典

常用操作：
    add()           |       在任意位置添加元素      |     s1.add()
    remove()        |   移除指定元素，不存在会报错   |     s1.remove()
    pop()           |        随机删除并返回        |     s1.pop()
    clear()         |            清空            |     s1.clear()
    difference()    |           求差集           |     s1.difference(s2)
    intersection()  |           求交集           |     s1.intersection(s2)
    union()         |           求并集           |     s1.union(s2)
"""

s1 = {1, 2, 34, 579, 14, 3466, 20}
s2 = {2, 478, 12, 11, 1, 78, 0, 35, 20}

# 1. add
print(s1)
s1.add(478)
print(s1)

# 2. remove
print(s2)
s2.remove(11)
print(s2)

# 3. pop
print(s1)
s1.pop()
print(s1)

# 4. clear
s3 = s1
print(s3)
s3.clear()
print(s3)

# 5. difference uinon intersection
print(s1.difference(s2))
print(s1.intersection(s2))
print(s1.union(s2))







