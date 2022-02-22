import numpy as np
import pandas as pd

data=np.arange(0,30,2)
data1=data.reshape(5,3)
data2=pd.DataFrame(data1,columns=('a','b','c'))
data2.iloc[2]




print(data2.iloc[2])
print(type(data2.iloc[2]))
print(data2.iloc[2].shape)


