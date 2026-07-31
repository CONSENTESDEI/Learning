def trangle (b, h):
    """
    三角形面积计算：
    :param b: 三角形底边长
    :param h: 三角形高
    :return: 三角形面积
    """
    return b * h / 2

def count_aeiou (s):
    """
    计算字符串中元音字母出现的次数：
    :param s: 传入字符串
    :return: 返回元音字母出现次数
    """
    num = 0
    for n in s:
        if n in 'aeiouAEIOU':
            num +=1
        return num
    












