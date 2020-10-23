import unittest
import random


def insertion_sort(array):
    """Sort an array of numbers!"""

    # start with the SECOND item
    for index in range(1, len(array)):

        # what value are we checking?
        key = array[index]

        # set the initial check index
        check_index = index - 1

        # keep moving the key down in the array until it's in place
        while check_index >= 0 and key < array[check_index]:
            array[check_index + 1] = array[check_index]
            check_index -= 1

        # place the key
        array[check_index + 1] = key

    return array


class TestSearch(unittest.TestCase):
    """Tests for our search function!"""

    def test_sort(self):
        sorted = insertion_sort([7, 2, 5, 1, 3, 6, 4])
        self.assertEqual(sorted, [1, 2, 3, 4, 5, 6, 7])

    def test_random_shuffle(self):
        sorted = list(range(10000))
        shuffled = list(range(10000))
        random.shuffle(shuffled)

        self.assertEqual(insertion_sort(shuffled), sorted)


if __name__ == '__main__':
    unittest.main()
