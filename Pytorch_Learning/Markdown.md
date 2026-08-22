## 算法

> - 穷举
> - 贪心
> - 分治
> - 动态规划



## 机器学习与人工智能的关系

<img src=".\resource\picture\机器学习人工智能关系.png" style="zoom:50%;" />



## 学习系统的发展

> 维度的诅咒，特征维度越高，数据量越大，所以有高低维映射进行降维，<u>数学部分</u>
>
> 特征和学习器是分开训练的：
>
> - 无监督学习很多都是做特征学习的
>
>   深度学习是 End to End 端到端的学习
>
> 支持向量机？



> transformer？



## 神经网络

> 神经学延申出的？
>
> 链式法则？复合函数求导
>
> - 多元函数微分，反向传播算法
>   ![](.\resource\picture\反向传播算法.png)
>
> 卷积？
>
> CV？
>
> 构造模型的套路
>
> 算法、数据集、算力



## 线性模型

> 1. 准备数据集
> 2. 根据数据集情况决定or设计模型
> 3. 训练
> 4. 推理

> 引例：
>
> 每周花费 x 小时，最终考 y 分，根据数据集推理花费5小时获得多少分
>
> |  x   |      y      |
> | :--: | :---------: |
> |  1   |      2      |
> |  2   |      4      |
> |  3   |      6      |
> |  4   | ?（测试集） |
>
> 输入新的数据获得预测结果
>
> 当测试集不存在，将训练集划分训练和开发集（验证集）

> 线性模型：y = a*x+b
>
> 当有初步模型：y_hat = m*a 时，找方法进行模型评估，确定和数据集间的误差，
>
> 评估模型是损失函数？**loss = (y_hat-y)^2^** <u>是针对单个样本的</u>
>
> 将每条数据的损失算出后，计算平均损失，让平均损失降到最低，几乎找不到 0 损失的模型
>
> 针对整个训练集的损失函数Mean Square Error(MSE) **cost = 1/N * Σ^N^~n=1~(y~n~_hat-y~n~)^2^ **
>
> 找权重的方法：暴力穷举

> 代码
>
> 通常不易权重为x，以训练次数为x，要找开发集减少到极小值时就是最优
>
> ```python
> # 1.导入数据
> x_data = [1.0, 2.0, 3.0]
> y_data = [2.0, 4.0, 6.0]
> 
> # 2.确定模型或对应关系
> def forward(x):
>     return x * w
> 
> # 3.损失函数
> def loss(x, y):
>     y_pred = forward(x)
>     return (y_pred - y) ** 2
> 
> # 4.创建权重表和 MSE表
> w_list = []
> mes_lest = []
> 
> # 5.生成 权重w 算出损失函数和MSE值
> for w in np.arange(0.0, 4.1, 0.1):
>     print(f"w={w:2f}")
>     l_sum = 0
>     for x_val, y_val in zip(x_data, y_data):
>         y_pred_val = forward(x_val)
>         loss_val = loss(x_val, y_val)
>         l_sum += loss_val
>         print(f"\t {x_val:.1f} {y_val:.1f} {y_pred_val:.3f} {loss_val:.4f}")
>     print("MSE = ", l_sum / len(x_data))
>     w_list.append(w)
>     mes_lest.append(l_sum / len(x_data))
> 
> # 6.输出权重和MSE的统计图
> plt.plot(w_list, mes_lest)
> plt.ylabel("loss")
> plt.xlabel("w")
> plt.show()
> ```
>
> <img src=".\resource\picture\loss_plot.png" style="zoom:72%;" />



> 加入偏置
>
> ```python
> # 导包
> import numpy as np
> import matplotlib.pyplot as plt
> from mpl_toolkits.mplot3d import Axes3D
> 
> # 1.导入数据
> x_data = [1.0, 2.5, 3.2, 4.8]
> y_data = [2.5, 5.0, 6.9, 10.1]
> 
> # 2.权重函数
> def w_d_func(x):
>     return x * w + b
> 
> # 求出表长
> len_x = len(x_data)
> 
> # 4.损失函数
> def loss(x, y):
>     y_pred = w_d_func(x)
>     return y_pred, (y_pred - y) ** 2
> 
> # 4.w b mse 的列表
> w_list = []
> b_list = []
> mse_list = []
> 
> # 5.不同权重下的各返回值
> for w in np.arange(0.0, 5.1, 0.1):
>     print(f"w={w:.1f}")
>     for b in np.arange(-1.0, 1.1, 0.1):
>         loss_sum = 0
>         print(f"\tb={b:.1f}")
>         for x_val, y_val in zip(x_data, y_data):
>             y_pred_val, loss_val = loss(x_val, y_val)
>             loss_sum += loss_val
>             print(f"\t\t {x_val:.1f}  {y_val:.1f}  {y_pred_val:.3f}  {loss_val:.4f}")
>         # 计算mse
>         mse_loss = loss_sum / len_x
>         print(f"\tMSE = {mse_loss:.3f}")
> 
>         # 存入mse
>         mse_list.append(mse_loss)
>         # 存入b
>         b_list.append(b)
>     # 存入w
>     w_list.append(w)
> 
> # 6.绘制图表
> # 将列表转换为二维网格
> w_unique = np.arange(0.0, 5.1, 0.1)
> b_unique = np.arange(-1.0, 1.1, 0.1)
> w_grid, b_grid = np.meshgrid(w_unique, b_unique)
> cost_grid = np.array(mse_list).reshape(len(b_unique), len(w_unique))
> 
> # 然后正常绘图
> fig = plt.figure()
> ax = fig.add_subplot(111, projection='3d')
> surf = ax.plot_surface(w_grid, b_grid, cost_grid, cmap='viridis', alpha=0.8, edgecolor='none')
> fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='MSE')
> 
> ax.set_xlabel("w")
> ax.set_ylabel("b")
> ax.set_zlabel("MSE")
> 
> plt.savefig('./resource/picture/loss_surface.png')
> plt.show()
> ```
>
> ![](.\resource\picture\loss_surface.png)



##