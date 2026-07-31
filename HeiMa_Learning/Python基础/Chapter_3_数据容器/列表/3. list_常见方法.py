"""
方法：实现某种功能的语句

常见方法：
append()     |    表尾追加                     |   s.append(100)
insert()     |    在指定索引之前插入             |   s.insert(3, 20)
remove()     |    移除第一个匹配到的值          |     s.remove(1)
pop()        |    删除指定索引位置的元素         |    s.pop(2) / s.pop()
reverse()    |    反转列表                    |     s.sort()
sort()       |    排序，必须列表元素类型一致     |     s.reverse()
len()        |    求列表长                    |     len(s)
min() / max()|    找最值                      |    min(s) / max(s)
"""

# 创建
s3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 7, 5, 23, 14, 15]

# 1. append
s3.append(20)
print(s3)

# 2. insert
s3.insert(3, 30)
print(s3)

# 3. remove
s3.remove(7)
print(s3)

# 4. pop
ret1 = s3.pop(2)
print(ret1)

ret2 = s3.pop()
print(ret2)

# 5. sort
s_temp1 = s3.sort()
print(s_temp1)

# 6. reverse
s_temp2 = s3.reverse()
print(s_temp2)








