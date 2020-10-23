import unittest
import random


def insertion_sort(array):
    """Sort an array of numbers!"""

    # loop - start with the SECOND item

    # what value are we checking?

    # set the initial check index

    # keep moving the key down in the array until it's in place,
    # swapping as needed

    # place the key

    return array


class TestSearch(unittest.TestCase):
    """Tests for our search function!"""

    def test_sort(self):
        sorted = insertion_sort([7, 2, 5, 1, 3, 6, 4])
        self.assertEqual(sorted, [1, 2, 3, 4, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()
