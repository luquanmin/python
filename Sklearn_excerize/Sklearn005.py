from imblearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import MinMaxScaler

from Sklearn_excerize.Sklearn001 import X
from Sklearn_excerize.Sklearn001 import y

pipe = make_pipeline(MinMaxScaler(),
                     LogisticRegression(solver='lbfgs', multi_class='auto',
                                        max_iter=1000, random_state=42))
scores = cross_validate(pipe, X, y, cv=3, return_train_score=True)

import pandas as pd

df_scores = pd.DataFrame(scores)
print(df_scores)
