"""
学生选课情况分析
"""

math_set = {"张三", "李四", "王五"}
eng_set = {"李四", "赵六", "孙七"}
prog_set = {"张三", "赵六", "周八"}
pyp_set = {"王五", "孙七", "周八"}

# 运算符求交集
ma_eng_set = math_set & eng_set
print(ma_eng_set)

all_set = math_set & eng_set & prog_set & pyp_set
print(f'{all_set}')

# 运算符求差集
math_no_eng_set = math_set - eng_set
print(f'{math_no_eng_set}')

# 集合推导式 语法：{要添加的数据 for s in set1 if 条件}

math_no_eng_set2 = {s for s in math_set if s not in eng_set}
print(f'{math_no_eng_set2}')

# 统计不同学生选课数量
# 获取学生名单
all_set2 = math_set | eng_set | prog_set | pyp_set
print(f'{all_set2}')

# 列表转换学生总选课数
list = [*math_set, *eng_set, *prog_set, *pyp_set]

for s in all_set2:
    print(f'{s} 选了 {list.count(s)} 门')























