import unittest

class TestGetMaxCount(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        expected = 0
        result = GetMaxCount(arr)
        self.assertEqual(result, expected)

    def test_single_max_value(self):
        arr = [1, 2, 3, 4, 5, 5]
        expected = 2
        result = GetMaxCount(arr)
        self.assertEqual(result, expected)

    def test_multiple_max_values(self):
        arr = [1, 5, 3, 5, 4, 5]
        expected = 3
        result = GetMaxCount(arr)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
