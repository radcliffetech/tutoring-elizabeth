import unittest
import random


def compare(item1, item2):
    return item1 > item2


def swap(array, index1, index2):
    tmp = array[index1]
    array[index1] = array[index2]
    array[index2] = tmp


def sort(array):
    """Sort an array of numbers! We will use bubble sort"""
    length = len(array)

    for pass_number in range(length):
        for index in range(length - 1):
            if compare(array[index], array[index + 1]):
                swap(array, index, index+1)

    return array


class TestSearch(unittest.TestCase):
    """Tests for our search function!"""

    # def test_sort(self):
    #     sorted = sort([5, 1, 3, 4, 2])
    #     self.assertEqual(sorted, [1, 2, 3, 4, 5])

    def test_random_shuffle(self):
        sorted = list(range(30000))
        shuffled = list(range(30000))
        random.shuffle(shuffled)

        self.assertEqual(sort(shuffled), sorted)

    # def test_random_shuffle_multiple(self):
    #     number_of_runs = 25
    #
    #     for i in list(range(number_of_runs)):
    #         sorted = list(range(100))
    #         shuffled = list(range(100))
    #         random.shuffle(shuffled)
    #         self.assertEqual(sort(shuffled), sorted)


if __name__ == '__main__':
    unittest.main()
