from sklearn.metrics import balanced_accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import make_pipeline

from Sklearn_excerize.sklearn002 import X_breast_test
from Sklearn_excerize.sklearn002 import X_breast_train
from Sklearn_excerize.sklearn002 import y_breast_test
from Sklearn_excerize.sklearn002 import y_breast_train

pipe = make_pipeline(StandardScaler(), SGDClassifier(max_iter=1000))

pipe.fit(X_breast_train, y_breast_train)
y_pred = pipe.predict(X_breast_test)
accuracy = balanced_accuracy_score(y_breast_test, y_pred)
print('Accuracy score of the {} is {:.4f}'.format(pipe.__class__.__name__, accuracy))
