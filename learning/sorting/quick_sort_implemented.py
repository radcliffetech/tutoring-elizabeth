import unittest
import random


def quicksort(array):
    """Sort an array of numbers!"""

    if len(array) == 0:
        return []

    left = []
    right = []
    pivot = array[0]
    del array[0]

    for index in range(len(array)):
        if array[index] < pivot:
            left.append(array[index])
        else:
            right.append(array[index])

    return quicksort(left) + [pivot] + quicksort(right)


class TestSearch(unittest.TestCase):
    """Tests for our search function!"""

    def test_sort(self):
        sorted = quicksort([7, 2, 5, 1, 3, 6, 4])
        self.assertEqual(sorted, [1, 2, 3, 4, 5, 6, 7])

    def test_sort_2(self):
        sorted = quicksort([7, 2, 5, 1, 1, 3, 6, 2, 4])
        self.assertEqual(sorted, [1, 1, 2, 2, 3, 4, 5, 6, 7])

    def test_random_shuffle(self):
        sorted = list(range(100))
        shuffled = list(range(100))
        random.shuffle(shuffled)

        self.assertEqual(quicksort(shuffled), sorted)

    def test_random_shuffle_multiple(self):
        number_of_runs = 100

        for i in list(range(number_of_runs)):
            sorted = list(range(100))
            shuffled = list(range(100))
            random.shuffle(shuffled)
            self.assertEqual(quicksort(shuffled), sorted)


if __name__ == '__main__':
    unittest.main()
