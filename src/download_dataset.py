import kaggle
from config import *


def download_dataset():
    try:
        kaggle.api.dataset_download_files(DATASET_ID, path=DOWNLOAD_PATH, unzip=True)
    except Exception as e:
        print("Error downloading dataset. Ensure you have Kaggle API credentials set up.")
        print(f"Error: {e}")


if __name__ == "__main__":
    download_dataset()
