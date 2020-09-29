"""

This file contains tests!

"""

from search import search

import unittest


class TestSearch(unittest.TestCase):
    """Tests for our search function!"""

    def test_search(self):
        matched_results = search("jeffrey")
        self.assertEqual(len(matched_results), 4)

    def test_search_2(self):
        matched_results = search("hannah")
        self.assertEqual(len(matched_results), 1)

    def test_search_order(self):
        matched_results = search("Elizabeth")
        self.assertEqual(len(matched_results), 5)
        self.assertEqual(matched_results[0]['result'], "Elizabeth Elizabeth Elizabeth!")
        self.assertEqual(matched_results[1]['result'], "Elizabeth says 'Elizabeth is great!'")


if __name__ == '__main__':
    unittest.main()
