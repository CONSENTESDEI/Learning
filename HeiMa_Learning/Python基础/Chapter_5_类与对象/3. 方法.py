"""
实例方法
"""

"""
魔法方法
初始化             | __init__
字符串表示          | __str__
比较对象是否相等     | __eq__
比较对象大小        | __lt__  __le__  __gt__  __ge__
                  | 小于     小于等于 大于     大于等于
"""

# 类创建
class Car:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.name} {self.price}"

# 对象创建
car1 = Car(brand = "BMW", name = "X5", price = 100)
car2 = Car(brand = "BMW", name = "X5", price = 100)

# 1. 比较
print(car1 == car2) # 调用的是 __eq__ 方法








