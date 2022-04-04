from sklearn.linear_model import LogisticRegression

from Sklearn_excerize.Sklearn001 import X_test
from Sklearn_excerize.Sklearn001 import X_train
from Sklearn_excerize.Sklearn001 import y_test
from Sklearn_excerize.Sklearn001 import y_train

clf = LogisticRegression(solver='lbfgs',
                         multi_class='auto',
                         max_iter=5000,
                         random_state=42)
clf.fit(X_train, y_train)
print('{} required {} iterations to be fitted'.format(clf.__class__.__name__, clf.n_iter_[0]))

from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

clf = LogisticRegression(solver='lbfgs',
                         multi_class='auto',
                         max_iter=1000,
                         random_state=42)
clf.fit(X_train_scaled, y_train)
accuracy = clf.score(X_test_scaled, y_test)
print('Accuracy score of the {} is {:.4f}'.format(clf.__class__.__name__, accuracy))
print('{} required {} iterations to be fitted'.format(clf.__class__.__name__, clf.n_iter_[0]))

from sklearn.pipeline import Pipeline

pipe = Pipeline(
    steps=[('scaler', MinMaxScaler()),
           ('clf', LogisticRegression(solver='lbfgs', multi_class='auto', random_state=42
                                      ))])

from sklearn.pipeline import make_pipeline

pipe = make_pipeline(
    MinMaxScaler(),
    LogisticRegression(solver='lbfgs',
                       multi_class='auto',
                       random_state=42,
                       max_iter=1000))

pipe.fit(X_train, y_train)
accuracy = pipe.score(X_test, y_test)
print('Accuracy score of the {} is {:.4f}'.format(pipe.__class__.__name__, accuracy))
# print('{} required {} iterations to be fitted'.format(pipe.__class__.__name__, pipe.n_iter_[0]))
print(pipe.get_params())
