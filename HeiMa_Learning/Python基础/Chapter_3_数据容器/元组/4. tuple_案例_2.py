"""
1. 计算学生总分，各科平均分，输出
2. 统计个可最低分，最高分，平均分，输出
3. 查找平均分大于90的学生
"""

students_data = (
    ("S001", "张明", 85, 92, 98),
    ("S002", "李丽", 67, 73, 88),
    ("S003", "王强", 91, 65, 82),
    ("S004", "赵芳", 74, 89, 95),
    ("S005", "陈浩", 58, 71, 63),
    ("S006", "周琳", 96, 84, 79),
    ("S007", "吴凯", 62, 58, 74),
    ("S008", "郑欣", 83, 96, 87),
    ("S009", "孙阳", 79, 68, 91),
    ("S010", "林萍", 88, 77, 69)
)

# 1. 学生总分、平均分
# 法1
"""
for s in students_data:
    total = s[-1] + s[-2] + s[-3]
    avg = total / 3
    print(f'学号{s[0]}  | '
          f'姓名：{s[1]}  | '
          f'语文：{s[2]}  | '
          f'数学：{s[3]}  | '
          f'英语：{s[4]}  | '
          f'总分：{total}  | '
          f'平均分：{avg:.1f}')
"""

# 法2 元组解包
for id, name, chinese, math, english in students_data:
    total = chinese + math + english
    avg = total / 3
    print(f'学号{id}  | '
          f'姓名：{name}  | '
          f'语文：{chinese}  | '
          f'数学：{math}  | '
          f'英语：{english}  | '
          f'总分：{total}  | '
          f'平均分：{avg:.1f}')

# 2. 各科最低、最高、平均
chinese_scores = [s[2] for s in students_data]
math_scores = [s[3] for s in students_data]
english_scores = [s[4] for s in students_data]

print(f'语文 | '
      f'最低分：{min(chinese_scores)} | '
      f'最高分：{max(chinese_scores)} | '
      f'平均分：{sum(chinese_scores) / len(chinese_scores)} |')
print(f'数学 | '
      f'最低分：{min(math_scores)} | '
      f'最高分：{max(math_scores)} | '
      f'平均分：{sum(math_scores) / len(math_scores)} |')
print(f'英语 | '
      f'最低分：{min(english_scores)} | '
      f'最高分：{max(english_scores)} | '
      f'平均分：{sum(english_scores) / len(english_scores)} |')

# 3. 找平均分90以上,同理可用解包
print(f'优秀学生：')
for s in students_data:
    avg = (s[-1] + s[-2] + s[-3]) / 3
    if avg > 90:
        print(f'学号：{s[0]}  | '
              f'姓名：{s[1]}  | '
              f'平均分：{avg:.1f}  |')








