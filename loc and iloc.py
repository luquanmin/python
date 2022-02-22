import numpy as np
import pandas as pd

data=np.arange(0,30,2)
data1=data.reshape(5,3)
data2=pd.DataFrame(data1,columns=('a','b','c'))
data2.iloc[2]  #去指定单行多列，结果为series
data2.iloc[1:4]



print(data2.iloc[1:4])
print(type(data2.iloc[1:4]))
print(data2.iloc[1:4].shape)


