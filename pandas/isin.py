# 一、isin函数（条件前加~表示isin函数的逆函数）
# 1、返回含有具体条件的dataframe，如返回'A'列中含有[4,8]的dataframe(用逆函数对筛选后的结果取余，起删除指定行作用）
import pandas as pd

data = pd.DataFrame([[0, 1, 2, 3], [4, 6, 8, 9], [4, 5, 6, 7], [8, 9, 10, 11]], columns=['A', 'B', 'C', 'D'])
data1 = data[data['A'].isin([4, 8])]  # 返回值满足{A列含有数值[4，8]的行
data2 = data[~data['A'].isin([4, 8])]  # 逆函数，剔除{A列含有数值[4,8]}的dataframe

# 2、返回含有多个条件的dataframe，如返回’A‘列中含有4,'B'列含有5的dataframe（用逆函数对筛选后的结果取余，起删除指定行作用）
data3 = data[data['A'].isin([4]) & data['B'].isin([5])]
data4 = data[~(data['A'].isin([4]) & data['B'].isin([5]))]

# 3、返回含有条件所在行的行号（index）
dta5 = list(data[data['A'].isin([4, 8])].index)

# 二、drop函数（DataFrame删除指定行列）
# 1、drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=false, errors='raise'):
# 1、labels:一个字符或数值，加上axis，表示带label标识的行或者列；如（labels='A', axis=1）表示A列
# 2、axis:axis=0表示行，axis=1表示列
# 3、columns：表示列名
# 4、index：表示dataframe的index，如index=1， index=a
# inplace：True表示删除某行后原DataFrame变化，False不改变原来的DataFrame

# 1、drop行数删除行
# 1.1、drop函数基于index和columns删除行
data6 = data.drop(index=0)  # 删除index=0的行
data7 = data.drop(labels=0, axis=0)  # 删除’行号为0’的行

# 2、drop行数删除特定条件的行（加入条件，找出满足此条件的index
# 如删除A列中包含数值4的行，可以先找满足此条件的行号，再利用drop函数，如index=data[data['A'].isin([4]).index[0],或者
# index=data[data['A']==4].index[0]

data8 = data.drop(index=data[data['A'].isin([4])].index[0])  # 删除包含4的第一行
data9 = data.drop(index=[data[data['A'].isin([4])].index[0], data[data['A'].isin([4])].index[1]])  # 删除包含4的第一行，第二行

# data20=data.drop([0,1]) #按照索引删除行

# data30=data.drop('a')  #此处a为假设的行索引，即index=‘a'
# data40=data.drop(['a','b','c'])  #此处a为假设的行索引，即index='a','b','c',删除多行
data40 = data.drop(['A', 'B', 'C'], axis=1)  # label为行时，可以没有轴，但当label为列时，必须有轴

# 知道第几行，但不知道行索引
# data50=data.drop(data.index(0))
# data60=data.drop([data.index[0],data.index[1]])

# 如果是在原地进行删除
# data70=data.drop(['a','b'], inplace=True)


# 2、drop函数删除列
# 2.1drop函数基于index和columns删除列
data10 = data.drop(columns='A')  # 删除columns为A的列
data11 = data.drop(labels='A', axis=1)  # 删除列名为A的列

# 3、因此删除行列有两种形式
# 3.1  labels=None, axis=0的组合
# 3.2  index或columns直接指定要删除的行或列
# 3.3  index和columns可以直接带标签，也可以用[]的方法，但是表示列时一定要带轴。


print(data, '\n')
print(data10)
print(data40)
# print(data10)
