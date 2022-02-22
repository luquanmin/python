import numpy as np
import pandas as pd

data = np.arange(0, 30, 2)
data1 = data.reshape(5, 3)
data2 = pd.DataFrame(data1, columns=('a', 'b', 'c'))

data2.iloc[2]  # 去指定单行多列，结果为series

data2.iloc[1:4]  # 索引[开始，结束]，作弊右开

data2.iloc[2, 2]  # 指定行、列取到一个数字

# data2.iloc[2,'c'] #不能直接取字段，报取值错误

data2.iloc[2:3, 0:2]  # 可以用切片来指定行列，行左闭右开,列左闭右开

data2.iloc[2:3, 0:].values  # 切片提取出来的行结果为DataFrame类型，将切片提取出来的数据转为数组

data2.iloc[0:, 1]  # 指定列取的结果是series类型

data2.iloc[0:, 0:1]  # 切片即使取一列的结果也是DataFrame类型

print(data2.iloc[0:, 0:1])
print(type(data2.iloc[0:, 0:1]))
print(data2.iloc[0:, 0:1].shape)
