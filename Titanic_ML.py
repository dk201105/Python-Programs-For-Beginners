# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:54:05 2026

@author: 23CSC11
"""
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report

df = pd.read_csv("titanic.csv")   

print("First 5 rows:")
print(df.head())

df = df[["survived","pclass","sex","age","sibsp","parch","fare","embarked"]]

df["age"] = df["age"].fillna(df["age"].mean())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

le_sex = LabelEncoder()
le_embarked = LabelEncoder() 

df["sex"] = le_sex.fit_transform(df["sex"])
df["embarked"] = le_embarked.fit_transform(df["embarked"])

X = df.drop("survived", axis=1)
y = df["survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#Feature Scaling 
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Naive Bayes Classifier
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

nb_pred = nb_model.predict(X_test)

nb_accuracy = accuracy_score(y_test, nb_pred)
nb_precision = precision_score(y_test, nb_pred)
nb_recall = recall_score(y_test, nb_pred)
nb_cm = confusion_matrix(y_test, nb_pred)

print("\n--- Naive Bayes Results ---")
print("Accuracy:", nb_accuracy)
print("Precision:", nb_precision)
print("Recall:", nb_recall)
print("Confusion Matrix:\n", nb_cm)

#Support Vector Machine (SVM)
svm_model = SVC(kernel="linear")
svm_model.fit(X_train, y_train)

svm_pred = svm_model.predict(X_test)

svm_accuracy = accuracy_score(y_test, svm_pred)
svm_precision = precision_score(y_test, svm_pred)
svm_recall = recall_score(y_test, svm_pred)
svm_cm = confusion_matrix(y_test, svm_pred)

print("\n--- SVM Results ---")
print("Accuracy:", svm_accuracy)
print("Precision:", svm_precision)
print("Recall:", svm_recall)
print("Confusion Matrix:\n", svm_cm)

#Comparison
print("\n--- Comparison ---")
print("Naive Bayes Accuracy:", nb_accuracy)
print("SVM Accuracy:", svm_accuracy)

print("\nNaive Bayes Classification Report:")
print(classification_report(y_test, nb_pred))

print("\nSVM Classification Report:")
print(classification_report(y_test, svm_pred))
