"""
类定义
    class 类名 :
        def __init__(self, 参数列表):  # self 表示当前创建的实例对象
            self.属性名 = 参数值
            self.属性名 = 参数值
类命名不用 _ ，用大小写区分

对象创建
    对象名 = 类名()
    对象名.属性1 = 属性值1
    对象名。属性2 = 属性值2
"""

# 1. 类定义
class Car:
    # init 方法是初始化方法，会在对象创建时自动调用
    # self 是第一个参数，是当前所创建的实例对象
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.c_color = c_color
        self.c_brand = c_brand
        self.c_name = c_name
        self.c_price = c_price

    def running(self):
        print(f"{self.c_brand} {self.c_name} 正在高速上行驶")

    def total_cost(self, discount, rate):
        """
        购车总价
        :param discount: 折扣
        :param rate: 税率
        :return: 购车总价
        """
        total_cost = discount * self.c_price + rate * self.c_price
        return total_cost

# 2. 创建对象
car1 = Car(c_color = "Red", c_brand = "BMW", c_name = "X7", c_price = 800000)
print(car1.__dict__)

car2 = Car(c_color= "Black", c_brand = "奔驰", c_name = "E300", c_price = 100000)
print(car2.__dict__)

car1.running()
total = car2.total_cost(discount = 0.8, rate = 0.1)
print(f"{total}")
print(f"{car2.total_cost(discount = 0.9, rate = 0.1)}")










