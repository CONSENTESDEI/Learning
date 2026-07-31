"""
实例属性，具体对象的属性，每个对象是独立的
类属性，类的属性，每个实例共享的
"""
class Car:
    # 类属性
    wheel = 4
    tex_rat = 0.1

    def __init__(self, brand, name, price):
        # 实例属性
        self.brand = brand
        self.name = name
        self.price = price

    # 访问时先查找实例属性，再查找类属性，有实例先实例

car1 = Car(brand = "BMW", name = "X5", price = 100)
car2 = Car(brand = "BMW", name = "X5", price = 100)







