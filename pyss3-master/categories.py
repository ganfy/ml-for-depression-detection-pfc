from pyss3 import SS3
from pyss3.util import Dataset, Evaluation, span
from pyss3.server import Live_Test

from sklearn.metrics import accuracy_score

clf = SS3()

s, l, p, _ = clf.get_hyperparameters()

print("Smoothness(s):", s)
print("Significance(l):", l)
print("Sanction(p):", p)

x_train, y_train = Dataset.load_from_files("DAIC_WOZ/train")
x_test, y_test = Dataset.load_from_files("DAIC_WOZ/test")

clf.train(x_train, y_train, n_grams=3)  # clf.fit(x_train, y_train)

acc = Evaluation.test(clf, x_test, y_test)
print("Accuracy:", acc)

f1 = Evaluation.test(clf, x_test, y_test, metric="f1-score")
print("F1-Score:", f1)

pr = Evaluation.test(clf, x_test, y_test, metric="precision")
print("Precision:", pr)

rec = Evaluation.test(clf, x_test, y_test, metric="recall")
print("Recall:", rec)

print(accuracy_score(y_test, clf.predict(x_test)))