"""
注意：一下所有方法都不会对字符串进行任何更改，会返回修改后的值

find()          |   找字串，返回第一个索引位置，找不到返回-1   | s.find('python')
count()         |   统计字串出现次数                       | S.count('h')
upper()         |   所有字母转大写                        |  s.upper()
lower()         |   所有字母转小写                        |  s.lower()
split()         |   按指定分隔分割成列表                   |  s.split('  ')
strip()         |   去除两端空白字符或指定字符              |  s.strip() / s.strip('*')
replace()       |   将指定子串替换为新子串                 |  s.replace('h', 'c')
startswith()    |   检测是否以指定字串为开头，返回bool值     |  s.startswitch('p')
"""

str = "asoifqnvqpoiweu    ___---1=34mv;asdnaw;"

# 1. find()
index = str.find('n')
print(index)

# 2. count()
num = str.count('h')
print(num)

# 3. upper() / lower()
str_upp = str.upper()
str_low = str.lower()
print(str_upp)
print(str_low)

# 4. split()
str_list = str.split('||')
print(str_list)

# 5. strip()
str_str = str.strip()
print(str_str)

# 6. replace()
str_rep = str.replace('h', 'c')
print(str_rep)

# 7. startswitch()
print(f'{str.startswith('aso')}')



















