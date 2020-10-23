import unittest
import random


def bogosort(array):
    """Sort an array of numbers!"""

    return array


class TestSearch(unittest.TestCase):
    """Tests for our search function!"""

    def test_sort(self):
        sorted = bogosort([7, 2, 5, 1, 3, 6, 4])
        self.assertEqual(sorted, [1, 2, 3, 4, 5, 6, 7])

    def test_random_shuffle(self):
        # warning this is slow! Don't do this with more than 50 unless you want to wait a while...
        sorted = list(range(50))
        shuffled = list(range(50))
        random.shuffle(shuffled)

        self.assertEqual(bogosort(shuffled), sorted)


if __name__ == '__main__':
    unittest.main()
