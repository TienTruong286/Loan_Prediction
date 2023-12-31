# -*- coding: utf-8 -*-
"""Loan Status Prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AN-eBvZCjyB0Womdd3mr02Cm07A1Xa14
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

loan_dataset = pd.read_csv("loan.csv")

loan_dataset.head()

loan_dataset.isnull().sum()

loan_dataset["Loan_Status"].describe()

loan_dataset["Loan_Status"] = loan_dataset["Loan_Status"].map({"Y":1, "N":0})

loan_dataset.shape

loan_dataset.head()

loan_dataset = loan_dataset.dropna()

loan_dataset.isnull().sum()

loan_dataset = loan_dataset.replace(to_replace = '3+', value=4)

loan_dataset["Dependents"].value_counts()

sns.countplot(x ='Education', hue = "Loan_Status", data = loan_dataset)

sns.countplot(x ="Married", hue = "Loan_Status", data = loan_dataset)

loan_dataset = loan_dataset.drop("Loan_ID", axis =1)
loan_dataset = pd.get_dummies(loan_dataset, drop_first = True)

loan_dataset.head()

loan_dataset.shape

X = loan_dataset.drop("Loan_Status", axis =1).values
y = loan_dataset["Loan_Status"].values

X_train, X_test, y_train,y_test = train_test_split(X,y, stratify = y, test_size = 0.25)

classifier = svm.SVC(kernel = 'linear')

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report

print(classification_report(y_pred,y_test))







