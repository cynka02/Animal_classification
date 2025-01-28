import unittest
from sklearn.ensemble import RandomForestClassifier
import repackage
repackage.up()
from models.RandomForest import get_model_random_forest


class TestRandomForestModel(unittest.TestCase):
    def test_return_type(self):
        """
            Tests if get_model_random_forest returns an instance of RandomForestClassifier.
        """

        model = get_model_random_forest()
        self.assertIsInstance(model, RandomForestClassifier)


if __name__ == "__main__":
    unittest.main()
