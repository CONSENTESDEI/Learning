"""
函数定义：
    组织好的、可重复使用的、用来实现特动功能的代码段


函数的基础：
    函数定义：
        def 函数名(参数列表):
            函数体
            ......
            return 返回值

    函数调用：
        函数名(参数)

    函数的说明文档：
    用于解释函数的功能和参数的作用
"""

def rectangle (l, w):
    """
    矩形面积、周长计算说明文档：
    :param l: 矩形的长
    :param w: 矩形的宽
    :return: 举行的面积，矩形的周长
    """
    return l * w , (l + w) * 2

print(rectangle(5, 5))  # 多返回值，返回的是元组

def cercle (r):
    """
    根据圆的半径，计算圆的面积、周长
    :param r: 圆的半径
    :return: 圆的面积，圆的周长
    """
    return round(3.14 * r ** 2, 1) , round(2 * 3.14 * r, 1)
    # round 用于保留小数位

print(cercle(2))
area, len = cercle(3)   # 解包操作
print(area, len)

"""
多函数嵌套调用：
    使用后进先出，LIFO，栈结构，递归
"""














