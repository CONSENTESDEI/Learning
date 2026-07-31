"""
在函数内定义全局变量 global 变量
"""

num = 3

def test():
    global num
    num = 0
    return num
print(f'num = {num}')
print(f'num = {test()}')
print(f'num = {num}')   # 注意 num 变量发生变化

#------------------------------------------------------------------------------------------------


"""
传参方式
"""

def rectangle (l, w):
    """
    矩形面积、周长计算说明文档：
    :param l: 矩形的长
    :param w: 矩形的宽
    :return: 举行的面积，矩形的周长
    """
    return l * w , (l + w) * 2

# 1. 按位置传参
rec_1 = rectangle(5, 5) # 调用是传参顺序和函数定义的顺序相同

# 2. 按形参名称传参
rec_2 = rectangle(w = 4, l = 3) # 传参以键值对形式传入函数，顺序无要求，最好顺序传，方便理解

#------------------------------------------------------------------------------------------------


"""
默认参数，可缺省参数
"""

def per_id (name, age, city ='北京'): # 需要放在非默认参数后，传入时不定义会按照默认值输出
    return f'name = {name}, age = {age}, city = {city}'

zs = per_id('张三',20)
ls = per_id('李四', 21, '南京')
print(f'zs = {zs}, ls = {ls}')

#------------------------------------------------------------------------------------------------


"""
不定长传参，可变参数
"""

# 1. 基于位置传参
def calcul(*args):
    """
    * 基于位置传不定长参数，最后形成的是元组
    求一组数的最值和平均值
    :param args: 传入的不定长参数
    :return: 返回 最大值，最小值，平均值
    """
    max_data = max(args)
    min_data = min(args)
    avg_data = sum(args) / len(args)
    return max_data, min_data, avg_data

test_max, test_min, test_avg = calcul(1, 2, 3, 4, 3123, 462, 6797, 245, 0)
print(f'test_max = {test_max}, test_min = {test_min }, test_avg = {test_avg}')

# 2. 基于关键字传参
def calcul(*args, **kwargs):
    """
    * 基于位置传不定长参数，最后形成的是元组

    ** 表示关键字传不定长参数，传入的是键值对，形成字典
       传入要用键值对

    求一组数的最值和平均值
    :param args: 传入的不定长参数
    :param kwargs: 传入的不定长关键字参数
           round: 保留小数位
           print: 是否打印
    :return: 返回 最大值，最小值，平均值
    """
    max_data = max(args)
    min_data = min(args)
    avg_data = sum(args) / len(args)

    if kwargs.get('round') is not None: # 通过获取键值对参数的 key，进行判读，对输出内容进行修改
        avg_data = round(avg_data, kwargs.get('round'))

    if kwargs.get('print'):
        print(max_data, min_data, avg_data)

    return max_data, min_data, avg_data

test_max, test_min, test_avg = calcul(1, 2, 3, 4, 3123, 0, round = 1, print = True)
print(f'test_max = {test_max}, test_min = {test_min }, test_avg = {test_avg}')

# 奶茶案例

# 1. 最终订单
def nc_ord(*nc_class, **test):
    pass

# 2. 奶茶菜单
zhongLei_manu = '''
################
#  1. 珍珠奶茶  #
#  2. 香芋奶茶  #
#  3. 百香果茶  #
#  4. 退出菜单  #
################
'''


# 3. 小料菜单
xiaoLiao_manu = '''
############
# 1. 布丁  #
# 2. 珍珠  #
# 3. 椰果  #
# 4. 退出  #
############
'''
# 4. 是否加冰
ice_manu = '''
############
# 1. 少量冰 #
# 2. 正常冰 #
# 3. 大量冰 #
# 4. 不加冰 #
############
'''

# 5，糖分选择
sug_manu = '''
############
# 1. 少量糖 #
# 2. 正常糖 #
# 3. 大量糖 #
# 4. 不加糖 #
############
'''
# 5. 顾客选择
cas_ord = ()

# 6. 输入
print(f'欢迎使用订单系统：')
print(f'{zhongLei_manu}')
zhongLei = input("请选择奶茶品种：")
cas_ord.add()

#------------------------------------------------------------------------------------------------


"""
函数的参数类型：将函数作为函数参数
特殊的函数嵌套方式
"""

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def calcul(x, y, order):
    """
    加减复合函数
    :param x: 传入参数
    :param y: 传入参数
    :param order: 操作符
    :return: 返回结果
    """
    return order(x, y)

cul1 = calcul(3, 4, add)
cul2 = calcul(3, 4, sub)

print(f'cul1 = {cul1}, cul2 = {cul2}')

#------------------------------------------------------------------------------------------------


"""
匿名函数/表达式函数
用lambda表达式
书写格式：lambda 参数列表 : 函数体
只适用于简单函数
需要赋值给变量才能使用
"""

add = lambda x, y : x + y

# 水果列表排序

fru_list = ["apple", "banana", "orange", "strawberry",
            "grape", "watermelon", "blueberry", "kiwi", "peach", "pear"]

fru_list.sort(lambda item : len(item), True)




