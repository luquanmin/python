import numpy as np
import pandas as pd

data = np.arange(0, 50, 2)
data1 = data.reshape(5, 5)
data2 = pd.DataFrame(data1, columns=['a', 'b', 'c', 'd', 'e'])

data2.iloc[2]  # 去指定单行多列，结果为series ，也就是一行

data2.iloc[1:4]  # 索引[开始，结束]，作闭右开

data2.iloc[2, 2]  # 指定行、列取到一个数字

# data2.iloc[2,'c'] #不能直接取字段，报取值错误

data2.iloc[2:3, 0:2]  # 可以用切片来指定行列，行左闭右开,列左闭右开

data2.iloc[2:3, 0:].values  # 切片提取出来的行结果为DataFrame类型，将切片提取出来的数据转为数组

data2.iloc[0:, 1]  # 指定列取的结果是series类型

data2.iloc[0:, 0:1]  # 切片即使取一列的结果也是DataFrame类型

# loc
data2.loc[2]  # 去指定某行

data2.loc[1:4]  # 指定左闭右闭区间

# data2.loc[2,3]  #列不能取行，行不能取列

data2.loc[2, 'c']  # 可以指定特定的行和列，得到指定的一个数字

data3 = data2.loc[1:4]  # 指定行，取列

data4 = data3[['a', 'b']]  # 可以取多列，但是这种形式虽然用了索引方式，但不是用loc

data12 = data2.loc[:, 'a']

# data5=data2.loc[[1:4],['a','b']]   #不能按照行列的思想取

# data6=data2.loc[[1:4],[1:2]]           #不能按照行列的思想取

data7 = data3[['a']]  # 指定单列  DataFrame型，取多列放在列表里

data8 = data3['a']  # 指定单列  Series型，多列不行，因为多列需要列表，如data11

data11 = data3[['a', 'b']]

data9 = data2.loc[[0, 1, 2, 3, 4], ['b', 'c']]

data10 = data2.loc[[1, 1, 1, 3, 4], ['b', 'c']]  # 列出特定行列的的值

"""

   sumarzie
   1、loc：
      1）通过行标签索引行数据；
      2）loc[n]表示索引的是第n行
      3）有行索引，可以没有字段取值，但有字段取值前必须有行索引
      4）行列都有时，行索引只能为标签索引形式来取，不能按切片形式来取
      5）单取切片形式可以，只是索引为左闭右闭

   2、iloc
      1）通过行索引获取行数据，不能是字符，取索引必须按切片形式来取，不能按标签，这是与loc的不同，
      2）索引为左闭右开；
      3）iloc也可以取指定行列，只不过得按切片形式索引。不能直接拿标签索引来做。
   3、advise：
      1）当用行索引的时候，尽量用iloc来进行索引，
      2）用标签索引的时候用loc；
      
   4、自我总结
      1）表达某一个数
         iloc：
            data2.iloc[2,2]
         loc：
            data2.loc[2,'c']
      2)表达某一行
         iloc：                   
            data2.iloc[2]   
         loc：                 
            data2.loc[2]  
      3）表达多行
         iloc：           
            data2.iloc[1：5]       左闭右开
         loc：                
            data2.loc[1：4]        左闭右闭
      4）表达一列
         iloc：                              
            data2.iloc[：，1：2]              
         loc：                                  
            data2.loc[:,'a']    
      5)表达多列
         iloc：               
            data2.iloc[：，1：3]
            data2.iloc[:,[1,2]]
         loc：                
            data2.loc[:,['a'，‘b'，’c']] 
            data2.loc[:,'a':'c']
            
      6) 表达不连续某几行，某几列
          iloc：                         
             data2.iloc[[1,2,4]，[1,2]]          
          loc：                          
             data2.loc[[1,2,4],['a'，‘b']] 
      7)表达不连续的某几行
          iloc：                           
             data2.iloc[[1,2,4]，：]    
          loc：                            
             data2.loc[[1,2,4],：] 
      8）表达不连续的某几列
          iloc：                    
             data2.iloc[:，[0,2]] 
          loc：                     
             data2.loc[：,['a','c']]  
      
             
      9)sumarize
          (1),iloc的列不能用列标签；loc的列只能用列标签，不能用索引或切片，除非用全切片
          (2),两者都可以表达各种情况；
          (3),两者不管表达行，还是列，使用切片时，都是loc左闭右闭，iloc左闭右开；
                          
"""

print(data2.loc[2, 'c'])

print(type(data2.loc[2, 'c']))

print(data2.loc[2, 'c'].shape)
😆
