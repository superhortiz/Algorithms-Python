import unittest
import random
from copy import deepcopy
from algorithms import Heapsort


class TestSort(unittest.TestCase):
    def test_empty_list(self):
        data = []
        Heapsort(data)
        self.assertEqual(data, [])

    def test_single_element(self):
        data = [5]
        Heapsort(data)
        self.assertEqual(data, [5])

    def test_already_sorted(self):
        data = [1, 2, 3, 4, 5]
        Heapsort(data)
        self.assertEqual(data, [1, 2, 3, 4, 5])

    def test_unsorted(self):
        data = [5, 2, 8, 1, 9]
        Heapsort(data)
        self.assertEqual(data, [1, 2, 5, 8, 9])

    def test_duplicates(self):
        data = [4, 2, 2, 8, 1]
        Heapsort(data)
        self.assertEqual(data, [1, 2, 2, 4, 8])

    def test_negative_numbers(self):
        data = [5, -2, 8, -1, 9]
        Heapsort(data)
        self.assertEqual(data, [-2, -1, 5, 8, 9])

    def test_floats(self):
        data = [5.5, 2.2, 8.8, 1.1, 9.9]
        Heapsort(data)
        self.assertEqual(data, [1.1, 2.2, 5.5, 8.8, 9.9])

    def test_random(self):
        n = 200
        data = [random.randint(-100, 100) for _ in range(n)]
        copy = deepcopy(data)
        Heapsort(data)
        self.assertEqual(data, sorted(copy))

    def test_input_validation(self):
        with self.assertRaises(ValueError):
            Heapsort("not a list")


if __name__ == '__main__':
    unittest.main()