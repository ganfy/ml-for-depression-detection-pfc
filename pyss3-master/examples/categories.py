from pyss3 import SS3
from pyss3.util import Dataset, Evaluation, span
from pyss3.server import Live_Test

from sklearn.metrics import accuracy_score

clf = SS3()

s, l, p, _ = clf.get_hyperparameters()

print("Smoothness(s):", s)
print("Significance(l):", l)
print("Sanction(p):", p)

x_train, y_train = Dataset.load_from_files("datasets/topic/train", folder_label=False)
x_test, y_test = Dataset.load_from_files("datasets/topic/test", folder_label=False)

clf.train(x_train, y_train, n_grams=3)  # clf.fit(x_train, y_train)

Evaluation.test(clf, x_test, y_test)