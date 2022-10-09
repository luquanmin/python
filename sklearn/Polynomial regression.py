import matplotlib.pyplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

"""
我们已经学习了线性回归模型，但是线性回归模型要求数据之间具有线性关系，而在很多场景中，数据之间往往不是线性关系而是非线性关系。
因此我们引入多项式回归，来专门处理这种非线性数据。多项式回归的基本思想与线性回归一致，只是在模型中引入了特征的高次项，从而使其能够拟合非线性关系
"""
#生成模拟数据
np.random.seed(666)
x = np.random.uniform(-3, 3, size = 100)
X = x.reshape(-1, 1)
y = 1.5 * x ** 2 + 2 * x + np.random.normal(0, 2, size=100)

#绘图
plt.scatter(x, y, color = 'steelblue')


#线性回归进行拟合
from sklearn.linear_model import LinearRegression
line_reg = LinearRegression()

#训练
line_reg.fit(X, y)

#预测
y_predict = line_reg.predict(X)

#绘制拟合曲线
#plt.scatter(x, y, color='steelblue')
#plt.plot(np.sort(x), y_predict[np.argsort(x)], color='indianred', linewidth=2.5)
#plt.show()

#R2
print(line_reg.score(X, y))

#添加x2项

X_new = np.hstack([X, X**2])
X_new.shape

#训练
line_reg.fit(X_new, y)

#预测
y_predict = line_reg.predict(X_new)

#绘制拟合曲线
plt.scatter(x, y, color='steelblue')
plt.plot(np.sort(x), y_predict[np.argsort(x)], color='indianred', linewidth=2.5)
plt.show()

# R2
print(line_reg.coef_)
print(line_reg.intercept_)

#(二)scikit-learn中的多项式回归和Pipeline(管道)
#使用PolynomialFeatures生成多项式特征

from sklearn.preprocessing import PolynomialFeatures

#添加最高二次幂的特征
Poly = PolynomialFeatures(degree=2)
Poly.fit(X)
X_2 = Poly.transform(X)
X_2[:5,:]

