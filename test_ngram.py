import unittest
from calculate_ngram import get_ngrams


class TestNgrams(unittest.TestCase):
    def test_ngram(self):
        test_data = {"text": "The sun rises in the east", "ngram": 2}
        expected_output = ["The sun", "sun rises", "rises east"]
        result = get_ngrams(test_data["text"], test_data["ngram"])
        self.assertEqual(result, expected_output)

