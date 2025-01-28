import unittest
from sklearn.svm import SVC
import repackage
repackage.up()
from models.SVC import get_model_svc


class TestSVCModel(unittest.TestCase):
    def test_return_type(self):
        model = get_model_svc()
        self.assertIsInstance(model, SVC)


if __name__ == "__main__":
    unittest.main()
