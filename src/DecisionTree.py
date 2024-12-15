from sklearn.tree import DecisionTreeClassifier
from load_dataset import split_data

def get_model_DecisionTree():
    x_train, x_test, y_train, y_test = split_data()
    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)
    return model

def main():
    get_model_DecisionTree()

if __name__ == "__main__":
    main()
