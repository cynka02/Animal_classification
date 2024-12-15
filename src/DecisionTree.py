import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


def get_model_DecisionTree(dataset, columns_to_drop, target):
    data = pd.read_csv(dataset)
    X = data.drop(columns=columns_to_drop)
    y = data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    return DecisionTreeClassifier()

