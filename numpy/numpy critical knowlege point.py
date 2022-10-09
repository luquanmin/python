#https://blog.csdn.net/zkx990121/article/details/119136515
#https://mp.weixin.qq.com/s/dPwgdbHF7Cumi-USPZTrYg
#1.0引入numpy库
import numpy as np

#1.1使用np.array创建数组
a = np.array([1,2,3,4])
print(a)
print(type(a))

#1.2使用np.arange创建数组，创建0~10，步数为2的数组[0,2,4,6,8]
b = np.arange(0,10,2)

#1.3 np.random.random创建数组,其中里面的值是在0~1之间的随机数，创建2行2列的随机数组
c = np.random.random((2,2))

#1.4 np.random.randint创建数组，其中值的范围可以通过前面2个参数来指定，创建4行4列的数组。
d = np.random.randint(0,9,size=(4,4))

#1.5特殊函数
#1.5.1 zeros 创建N行N列的全零数组
array_zeros = np.zeros((3,3))

#1.5.2 ones 创建N行N列的全一数组
array_ones = np.ones((4,4))

#1.5.3 full 全部为指定值的N行N列的数组
array_full =  np.full((2,3),9)

#1.5.4 eye 生成一个在斜方形上元素为1，其它元素都为0的N行N列矩阵
array_eye = np.eye(4)

#1.6zy注意：数组中的数据类型必须一致，要么全部为整型，要么全部为浮点类型，不能同时出现多种数组类型

#2.1 数据类型
# bool b
# int8 i1
# int16 i2
# int32 i4
# int64 i8
# uint8 u1
# uint16 u2
# uint32 u4
# uint64 u8
# float16 f2
# float32 f4
# float64 f8
# complex64 c8
# complex128 c16
# object O
# sting_ S
# unicode_ U