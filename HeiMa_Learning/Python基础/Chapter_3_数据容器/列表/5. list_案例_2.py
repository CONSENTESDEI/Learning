"""
1. 合并列表
2， 去重
"""

# 1. 创建
list1 = [1, 3, 5, 7, 9, 3, 5, 2, 8, 5]
list2 = [2, 4, 6, 8, 10, 2, 4, 6, 1, 4]

# 2. 合并
"""
for i in list2:
    list1.append(i)
print(list1)
"""
num_list = list1 + list2
print(num_list)

# 3. 去重
new_list = []
for i in num_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)











