import unittest
import random


def sort(array):
    """Sort an array of numbers! We will use bubble sort"""
    length = len(array)

    for pass_number in range(length):

        for index in range(length - 1):
            if array[index] > array[index + 1]:
                # swap!
                tmp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = tmp

    return array


class TestSearch(unittest.TestCase):
    """Tests for our search function!"""

    def test_sort(self):
        sorted = sort([5, 1, 3, 4, 2])
        self.assertEqual(sorted, [1, 2, 3, 4, 5])

    def test_random_shuffle(self):
        sorted = list(range(100))
        shuffled = list(range(100))
        random.shuffle(shuffled)

        self.assertEqual(sort(shuffled), sorted)

    def test_random_shuffle_multiple(self):
        number_of_runs = 25

        for i in list(range(number_of_runs)):
            sorted = list(range(100))
            shuffled = list(range(100))
            random.shuffle(shuffled)
            self.assertEqual(sort(shuffled), sorted)


if __name__ == '__main__':
    unittest.main()
