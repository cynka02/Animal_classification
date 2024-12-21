import pandas as pd
from config import *
from sklearn.model_selection import train_test_split


def split_data():
    data = pd.read_csv(PATH_TO_DATASET)
    x = data.drop(columns=COLUMN_TO_DELETE)
    y = data[CLASS_COLUMN]
    return train_test_split(x, y, test_size=TEST_SIZE, random_state=SEED)


def load_data():
    data = pd.read_csv(PATH_TO_DATASET)
    data = data.drop(columns='class_type')
    return data
