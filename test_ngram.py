import unittest
from parameterized import parameterized
from calculate_ngram import get_ngrams


class TestNgrams(unittest.TestCase):
    @parameterized.expand([
        ["", "The sun rises in the east", 1, ["The", "sun", "rises", "east"]],
        ["", "The sun rises in the east", 2, ["The sun", "sun rises", "rises east"]],
        ["", "The sun rises in the east", 3, ['The sun rises', 'sun rises east']],
        ["", "", 3, []]
    ])
    def test_ngrams(self, name, text, ngram, expected_output):
       result = get_ngrams(text, ngram)
       self.assertEqual(result, expected_output)


if __name__ == "__main__":
    print(dir(TestNgrams))
    unittest.main()

