import numpy as np

np.version
np.show_config()

np.info(np.abs)

np.zeros(10)
np.zeros((5, 2))
np.zeros((2, 2, 3))

z = np.zeros((3, 4))
z[2, 3] = 1
z[1, 1] = 2
np.nonzero(z)

np.ones(6)
np.ones((3, 2))
np.ones((2, 3, 3))

np.eye(4)
np.eye(4, dtype=int)

np.ones([2, 3])
np.ones([2, 3], dtype=int)

lst = [1, 2, 3, 4]
np.array(lst)

np.array(lst, dtype=float)

lst1 = [[1, 2, 3], [4, 5, 6]]
np.array(lst1)
np.array(lst1, dtype=float)

t1 = (9, 8, 7)
np.array(t1)

t2 = ((9, 8, 7), (6, 5, 4))
np.array(t2)

lt = [(1, 2, 3), (7, 8, 9)]
np.array(lt)

range_number = range(3, 8)  # 迭代器转数组,range对象
np.array(range_number)

range_number1 = range(3, 8)
np.array(range_number1, dtype=float)

b = np.ones((6, 6))
b[1:-1, 1:-1] = 0

c = np.ones((6, 6))
np.pad(c, pad_width=1, mode='constant', constant_values=0)

np.diag(1 + np.arange(5), k=-1)
np.diag(np.arange(1, 6), k=-1)

np.random.random((2, 3, 2))

import pandas as pd

s = pd.Series([1, 2, 3, 4])

d1 = pd.DataFrame((1, 2, 3, 4), [7, 8, 10, 11])
d2 = pd.DataFrame((1, 2, 3, 4), (7, 8, 10, 11))
d3 = pd.DataFrame((1, 2, 3, 4), ['S1', 'S2', 'S3', 'S4'])

ten = np.arange(10)
ten[::-1]

arr = np.arange(16)
arr.shape
arr.reshape(4, 4)
arr.reshape((4, 4))
arr.reshape(2, 8)
arr.reshape(8, 2)
arr.reshape(-1, 8)

np.linspace(1, 8.2, 5)  # 等差数列

np.logspace(1, 5, num=10)  # 等比数列
np.logspace()
