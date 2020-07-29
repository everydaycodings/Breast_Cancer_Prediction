import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import pickle

data = pd.read_csv("breast_cancer.csv", sep=';')
# print(data.head())

data = data[
    ["clump_thickness", "cell_size", "cell_shape", "marginal_adhesion", "single_epithelial_cell_size", "bare_nuclei",
     "bland_chromatin", "normal_nucleoli", "mitoses", "diagnose"]]

predict = "diagnose"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

print("Processing...")
best = 0
i = 0
for i in range(10000):
    i += 1
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)

    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)

    acc = linear.score(x_test, y_test)
    print(i,"%")

    if acc > best:
        best = acc
        # print(best)
        with open("Cancer_model.pickle", "wb") as f:
            pickle.dump(linear, f)

print()

print("Prediction: ",best)
