import matplotlib.pyplot as plt

from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)

plt.imshow(X[0].reshape(8, 8), cmap='gray')
plt.axis('off')
print('The digit in the image is {}'.format(y[0]))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    stratify=y,
                                                    random_state=42)
# https://blog.csdn.net/weixin_37226516/article/details/62042550


from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(solver='sag',
                         multi_class='multinomial',
                         max_iter=5000,
                         random_state=42)

clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print('Accuracy score of the {} is {:.4f}'.format(clf.__class__.__name__,
                                                  accuracy))
# https://blog.csdn.net/lc574260570/article/details/82116197

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=42)
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print('Accuracy score of the {} is {:.4f}'.format(clf.__class__.__name__,
                                                  accuracy))

# https://blog.csdn.net/u012768474/article/details/92829985
