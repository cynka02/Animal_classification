import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from load_dataset import split_data

def get_model_DecisionTree(path_to_dataset):
    data = pd.read_csv(path_to_dataset)
    x = data.drop(columns=['animal_name', 'class_type'])
    y = data['class_type']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)

    return model

def main():
    path_to_dataset = '../data/zoo.csv'
    get_model_DecisionTree(path_to_dataset)

if __name__ == "__main__":
    main()
