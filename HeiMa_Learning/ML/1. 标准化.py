"""
标准化

方差：该 列 每个值和该列 均值 的差的 平方和 的 平均值
标准差：方差开平方根
"""

# 导包
from sklearn.preprocessing import StandardScaler    # 标准化对象

# 1. 准备数据
x_train = [[40, 2, 10, 65], [60, 15, 34, 46], [77, 38, 57, 29]]

# 2. 创建标准化对象
transfer1 = StandardScaler()  # 均值、方差、标准差是数据固有属性，所以不能限定范围

# 3. 对原数据集进行标准化操作
x_train_new_1 = transfer1.fit_transform(x_train)

# 4. 打印数据
print(f"标准化后的数据集_1为：\n{x_train_new_1}")

# 5. 打印数据集的均值和方差
print(f'数据集的_1均值为{transfer1.mean_}；\n方差为；{transfer1.var_}；\n标准差为{transfer1.scale_}')
