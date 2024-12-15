import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

def get_model_SVC(path_to_dataset):
    data = pd.read_csv(path_to_dataset)
    x = data.drop(columns=['animal_name', 'class_type'])
    y = data['class_type']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
    model = SVC(probability=True)
    model.fit(x_train, y_train)

    return model

def main():
    path_to_dataset = '../data/zoo.csv'
    get_model_SVC(path_to_dataset)


