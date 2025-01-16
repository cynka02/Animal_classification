import pandas as pd
from config import *
from sklearn.model_selection import train_test_split
from utils import get_repo_path


def split_data():
    """
        Splits data into train and test dataframes.

        Returns:
            tuple: train and test dataframes.
    """

    data = pd.read_csv(get_repo_path() / PATH_TO_DATASET)
    data = data.drop_duplicates()
    x = data.drop(columns=COLUMN_TO_DELETE)
    y = data[CLASS_COLUMN]
    return train_test_split(x, y, test_size=TEST_SIZE, random_state=SEED)


def load_data():
    data = pd.read_csv(get_repo_path() / PATH_TO_DATASET)
    data = data.drop_duplicates()
    return data
