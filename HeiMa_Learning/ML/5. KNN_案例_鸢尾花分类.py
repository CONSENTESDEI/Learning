"""
案例：通过 KNN 算法实现鸢尾花分类
"""

# 导包

# 加载鸢尾花数据集（内置经典多分类数据集，含150个样本，3个类别）
from sklearn.datasets import load_iris

# 数据可视化库，基于matplotlib，提供更美观的统计图形（如散点图、箱线图、热力图等）
import seaborn as sns

# 数据处理库，提供DataFrame数据结构，方便数据清洗、操作和分析
import pandas as pd

# 基础绘图库，用于创建各种静态图表（折线图、柱状图、散点图等）
import matplotlib.pyplot as plt

# 数据集划分工具，将数据按指定比例随机分割为训练集和测试集
from sklearn.model_selection import train_test_split

# 数据标准化处理器，将特征缩放为均值为0、方差为1的标准正态分布（提升KNN等距离算法的性能）
from sklearn.preprocessing import StandardScaler

# K近邻分类器（K-Nearest Neighbors），基于距离度量（如欧氏距离）进行分类的监督学习算法
from sklearn.neighbors import KNeighborsClassifier

# 模型评估指标，计算分类正确的样本数占总样本数的比例（准确率）
from sklearn.metrics import accuracy_score

# 1. 定义函数，加载鸢尾花数据集，并查看数据集

def demo01_loadiris():
    # 1. 加载鸢尾花数据集
    iris_data = load_iris()
    # 2. 查看数据集
    """
    print(f"数据集：{iris_data}")  # 字典形态
    print(f"数据集类型：{type(iris_data)}")   # <class 'sklearn.utils._bunch.Bunch'>
    """
    # 3. 查看数据集所有的键
    print(f"数据集所有的键：{iris_data.keys()}")
    # 4. 查看数据集的键对应的值
    print(f"具体的数据：{iris_data.data[:5]}") # 共150条数据，每条数据4个特征，只要前5个
    print(f"具体的标签：{iris_data.target[:5]}") # 共150条数据，每条数据4个特征，只要前5个
    print(f"标签对应的名称：{iris_data.target_names}") # ['setosa' 'versicolor' 'virginica']
    print(f"特征对应的名称：{iris_data.feature_names}") # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']


# 2.

# 3.

# 4.

# 5. 测试

if __name__ == '__main__':
    demo01_loadiris()



























