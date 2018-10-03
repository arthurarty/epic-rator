import unittest
from lfa import Lfa

class LfaTest(unittest.TestCase):

    def setUp(self):
        self.lfa = Lfa()

    def test_add_score(self):
        """test adding score."""
        response = self.lfa.add_score(88, 1, 8)
        self.assertIsInstance(response, dict)
        self.assertEqual(response, { "bootcamper_id": 1, "score": 8, "lfa_id": 88 })

    def test_update(self):
        """Test edit score."""
        self.lfa.add_score(88, 1, 8)
        response = self.lfa.edit_score(1, 10)
        self.assertIsInstance(response, dict)
        self.assertEqual(response, { "bootcamper_id": 1, "score": 10, "lfa_id": 88 })

    def test_get_scores_lfa_bootcamper(self):
        response = self.lfa.get_scores_lfa_bootcamper(88)
        self.assertIsInstance(response, list)
