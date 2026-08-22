"""
案例：通过 KNN 算法实现鸢尾花分类

回顾：机器学习项目原发流程
    1. 加载数据
    2. 数据的预处理
    3. 特征工程（提取、预处理...）
    4. 模型训练
    5. 模型评估
    6. 模型预测
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

def demo01_load_iris():
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
    print(f"特征对应的名称：{iris_data.feature_names}")
    # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

    # 其他字段：'frame', 'DESCR', 'filename', 'data_module'
    """
    # filename：iris.csv
    print(f"数据集的描述：{iris_data.DESCR}")
    :Summary Statistics: from iris_data.DESCR

        ============== ==== ==== ======= ===== ====================
                        Min  Max   Mean    SD   Class Correlation
        ============== ==== ==== ======= ===== ====================
        sepal length:   4.3  7.9   5.84   0.83    0.7826
        sepal width:    2.0  4.4   3.05   0.43   -0.4194
        petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)
        petal width:    0.1  2.5   1.20   0.76    0.9565  (high!)
        ============== ==== ==== ======= ===== ====================
    """

# 2. 数据集格式化，绘制散点图
def demo02_show_iris():
    # 1. 加载数据集
    iris_data = load_iris()

    # 2. 把 数据集 封装成 DataFrame对象
    iris_df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)

    # 3. 给 DF 添加1列 标签
    iris_df['label'] = iris_data.target

    # 4. 通过 seaborn 输出散点图
    sns.lmplot(data=iris_df, x='sepal length (cm)', y='sepal width (cm)', hue='label', fit_reg=True)

    # 5. 设置标题，显示
    plt.title("iris data")
    plt.tight_layout()  # 自动调整子图参数，让图像边界与子图匹配
    plt.show()

    #输出预览
    #print(iris_df)

# 3. 定义函数，切分训练集和测试集
def demo03_split_train_test():
    # 1. 加载数据集
    iris_data = load_iris()

    # 2. 数据预处理，将150份数据 按 8:2 切分，8份训练 2份测试
    """
    参1：特征数据，参2：标签数据，参3：测试集比例
    random_state 随机种子，种子相同，随机结果相同，不定义的话，每次结果不一样
    返回值：训练特征数据，测试特征数据，训练标签数据，测试标签数据
    """
    x_train, x_test, y_train, y_test = train_test_split(iris_data.data,
                                                        iris_data.target,
                                                        test_size=0.2,
                                                        random_state=25)
    # 3. 打印
    print(f"训练集特征{x_train}，个数{len(x_train)}")   # 120条，4列
    print(f"训练集标签{y_train}，个数{len(y_train)}")   # 120条，1列
    print(f"测试集特征{x_test}，个数{len(x_test)}")     # 30条，4列
    print(f"测试集标签{y_test}，个数{len(y_test)}")     # 30条，1列


# 4. 加载数据，数据预处理，特征工程，模型训练，模型评估，模型测试
def demo04_iris_evaluate_test():
    # 1. 加载数据集
    iris_data = load_iris()

    # 2. 数据预处理，按 8:2 切分
    x_train, x_test, y_train, y_test = train_test_split(iris_data.data,
                                                        iris_data.target,
                                                        test_size=0.2,
                                                        random_state=20)

    # 3. 特征工程
    ## 特征提取，源数据只有4列，都是我们用的，所以不用提取
    ## 特征预处理，因为4列特征差值不大，不做处理，但为了学习

    # 3.1 创建标准化对象
    transfer = StandardScaler()

    # 3.2 对特征列做标准化，x_train, x_test
    """
    为什么 x_test 不用 fit_transform：
    fit_transform：兼具 fit transform 的功能，即：训练，转换，适用于第一次标准化使用
                参考你的数据集来改 StandardScaler 中的默认参数，契合你的数据，一般用于训练集
    transform：重复进行标准化时使用，一般用于测试集
    """
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4. 模型训练
    # 4.1. 创建模型对象
    estimator = KNeighborsClassifier(n_neighbors=5)

    # 4.2. 具体训练模型的动作
    estimator.fit(x_train, y_train) # 传入训练集数据

    # 5. 模型预测==============================================
    # 场景1：对测试集测试
    # 5.1. 直接预测
    y_pred = estimator.predict(x_test)

    # 5.2. 打印预测结果
    print(f"预测结果为：{y_pred}")

    # 场景2：对新数据测试
    """
    # 5.1. 自定义数据测试集
    
    # :Summary Statistics: from iris_data.DESCR
    # 
    #     ============== ==== ==== ======= ===== ====================
    #                     Min  Max   Mean    SD   Class Correlation
    #     ============== ==== ==== ======= ===== ====================
    #     sepal length:   4.3  7.9   5.84   0.83    0.7826
    #     sepal width:    2.0  4.4   3.05   0.43   -0.4194
    #     petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)
    #     petal width:    0.1  2.5   1.20   0.76    0.9565  (high!)
    #     ============== ==== ==== ======= ===== ====================
    
    my_data = [
        [5.1, 3.5, 1.4, 0.2],  # 接近setosa（山鸢尾）
        [7.0, 3.2, 4.7, 1.4],  # 接近versicolor（变色鸢尾）
        [6.3, 3.3, 6.0, 2.5],  # 接近virginica（维吉尼亚鸢尾）
        [4.9, 2.4, 3.3, 1.0],  # versicolor区域
        [6.7, 3.1, 5.6, 2.1],  # virginica区域
        [5.5, 2.6, 4.4, 1.2],  # versicolor区域
        [4.4, 2.9, 1.3, 0.2],  # setosa区域
        [6.1, 2.8, 4.9, 1.8],  # virginica/versicolor边界
        [5.8, 4.0, 1.2, 0.1],  # setosa区域（宽萼片）
        [6.9, 3.0, 5.1, 1.9]   # virginica区域
    ]

    # 5.2. 对自己的数据进行标准化
    my_data = transfer.transform(my_data)

    # 5.3. 模型预测
    y_pred_my = estimator.predict(my_data)

    # 5.4. 打印预测结果
    print(f"预测结果为：{y_pred_my}")

    # 5.5. 查看上述数据集，每种分类的预测概率
    y_pred_proba = estimator.predict_proba(my_data)
    print(f"个分类预测概率为：{y_pred_proba}")
    """
    # =========================================================

    # 6. 模型评估
    # 方式1：直接评估，基于：训练集特征和训练集标签
    print(f"正确率（准确率）：{estimator.score(x_train, y_train)}")

    # 方式2：调用函数，基于：测试集标签和预测结果，更专业
    print(f"正确率（准确率）：{accuracy_score(y_test, y_pred)}")

# 5. 测试

if __name__ == '__main__':
    # demo01_load_iris()
    # demo02_show_iris()
    # demo03_split_train_test()
    demo04_iris_evaluate_test()