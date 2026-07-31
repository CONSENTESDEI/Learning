"""
1. 生成1-20的平方
2. 取出偶数
3. 算出取出偶数的平方
4. 将平方数放入新列表
"""

# # 1. 创建
# s1 = []
# for i in range(21):
#     s1.append(i**2)
# print(s1)
#
# # 2. 取出偶数，平方，放入新列表
# s2 = []
# for i in s1:
#     if i % 2 == 0:
#         s2.append(i**2)


# 1. 1-20平方
"""
列表推导式
语法格式1：[要插入的元素 for i in 序列/列表]
"""
list_new1 = [i**2 for i in range(21)]
print(list_new1)

# 2. 取出偶数，平方，放入新列表
"""
语法格式2：[要插入的元素 for i in 序列/列表 if 条件]
"""
list_new2 = [i**2 for i in list_new1 if i%2==0]










