import unittest
import random


def is_sorted(array):
    """Return True if an array is sorted, least to greatest"""
    for index in range(0, len(array) - 1):
        if array[index] > array[index + 1]:
            return False
    return True


def bogosort(array):
    """Sort an array of numbers!"""

    sorted = False

    while not sorted:

        random.shuffle(array)

        if is_sorted(array):
            sorted = True

    return array


class TestSearch(unittest.TestCase):
    """Tests for our search function!"""

    def test_sort(self):
        sorted = bogosort([7, 2, 5, 1, 3, 6, 4])
        self.assertEqual(sorted, [1, 2, 3, 4, 5, 6, 7])

    # def test_random_shuffle(self):
    #     sorted = list(range(100))
    #     shuffled = list(range(100))
    #     random.shuffle(shuffled)
    #
    #     self.assertEqual(bogosort(shuffled), sorted)


if __name__ == '__main__':
    unittest.main()
