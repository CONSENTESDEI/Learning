"""
特征预处理——归一化
"""

# 导包
from sklearn.preprocessing import MinMaxScaler

# 1. 准备数据
x_train = [[40, 2, 10, 65], [60, 15, 34, 46], [77, 38, 57, 29]]

# 2. 创建归一化对象
transfer1 = MinMaxScaler()  # 默认 [0, 1]
transfer2 = MinMaxScaler(feature_range=(2, 5))  # 指定 [2, 5]

# 3. 对原数据集进行归一化操作
x_train_new_1 = transfer1.fit_transform(x_train)
x_train_new_2 = transfer2.fit_transform(x_train)

# 4. 打印数据
print(f"归一化后的数据集_1为：\n{x_train_new_1}")
print(f"归一化后的数据集_2为：\n{x_train_new_2}")