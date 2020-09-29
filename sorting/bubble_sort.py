import unittest
import random


def sort(array):
    """Sort an array of numbers!"""

    return array


class TestSearch(unittest.TestCase):
    """Tests for our search function!"""

    # def test_sort(self):
    #     sorted = sort([5, 1, 3, 4, 2])
    #     self.assertEqual(sorted, [1, 2, 3, 4, 5])

    def test_random_shuffle(self):
        sorted = list(range(10000))
        shuffled = list(range(10000))
        random.shuffle(shuffled)

        self.assertEqual(sort(shuffled), sorted)

    # def test_random_shuffle_multiple(self):
    #     number_of_runs = 100
    #
    #     for i in list(range(number_of_runs)):
    #         sorted = list(range(100))
    #         shuffled = list(range(100))
    #         random.shuffle(shuffled)
    #         self.assertEqual(sort(shuffled), sorted)


if __name__ == '__main__':
    unittest.main()
