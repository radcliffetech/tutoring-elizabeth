import unittest
import random


def quicksort(array):
    """Sort an array of numbers!"""

    # if the array is empty return []

    # grab the first element - this is the pivot!

    # get rid of the pivot in the array we're going to process

    # create two buckets, left and right

    # put everything lesser than the pivot in the left bucket

    # put everything greater than the pivot in the right bucket

    # run quicksort on each of the two new buckets
    # return quicksort(left) + [pivot] + quicksort(right)

    return array


class TestSearch(unittest.TestCase):
    """Tests for our search function!"""

    def test_sort(self):
        sorted = quicksort([4, 2, 5, 1, 3, 6, 7])
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
