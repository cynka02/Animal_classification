import unittest
from sklearn.ensemble import GradientBoostingClassifier
import repackage
repackage.up()
from models.GradientBoosting import get_model_gradient_boosting


class TestGradientBoostingModel(unittest.TestCase):
    def test_return_type(self):
        """
            Test if get_model_gradient_boosting returns an instance of GradientBoostingClassifier.
        """

        model = get_model_gradient_boosting()
        self.assertIsInstance(model, GradientBoostingClassifier)


if __name__ == "__main__":
    unittest.main()
