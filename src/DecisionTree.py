import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def get_model_DecisionTree(dataset, columns_to_drop, target):
    data = pd.read_csv(dataset)
    x = data.drop(columns=columns_to_drop)
    y = data[target]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)

    return model


