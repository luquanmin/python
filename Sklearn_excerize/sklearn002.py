from time import time

t1 = time()
from sklearn.datasets import load_breast_cancer

X_breast, y_breast = load_breast_cancer(return_X_y=True)

from sklearn.model_selection import train_test_split

X_breast_train, X_breast_test, y_breast_train, y_breast_test = train_test_split(
    X_breast, y_breast, stratify=y_breast, random_state=0, test_size=0.3)

from sklearn.ensemble import GradientBoostingClassifier

clf = GradientBoostingClassifier(n_estimators=100, random_state=0)
clf.fit(X_breast_train, y_breast_train)

y_pred = clf.predict((X_breast_test))

from sklearn.metrics import balanced_accuracy_score

accuracy = balanced_accuracy_score(y_breast_test, y_pred)
print('Accuracy score of the {} is {:.4F}'.format(clf.__class__.__name__, accuracy))

t2 = time()
t = t2 - t1
print(t)
