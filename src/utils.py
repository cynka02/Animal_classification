from pathlib import Path
import os
import pandas as pd
from config import *
from sklearn.model_selection import train_test_split


def get_repo_path():
    current_path = Path(os.path.abspath('.'))
    path = current_path / Path(__file__)

    # Find .git folder in superdirectory
    while not os.path.exists(path / '.git'):
        path = path.parent
        if path == Path('/'):
            raise FileNotFoundError('Probably not inside git repository.')

    return path


def load_data():
    """
        Loads the dataset.

        Returns:
            DataFrame: A DataFrame containing the dataset.
    """

    data = pd.read_csv(get_repo_path() / PATH_TO_DATASET)
    data.drop_duplicates(subset='animal_name', inplace=True)
    return data


def split_data():
    """
        Splits data into train and test dataframes.

        Returns:
            tuple: train and test dataframes.
    """

    data = load_data()
    x = data.drop(columns=COLUMN_TO_DELETE)
    y = data[CLASS_COLUMN]
    return train_test_split(x, y, test_size=TEST_SIZE, random_state=SEED)
