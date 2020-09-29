from search import search
import unittest


class TestSearch(unittest.TestCase):
    """Tests for our search function!"""

    def test_search_order(self):
        matched_results = search("Elizabeth")
        # print(matched_results)

        self.assertEqual(len(matched_results), 5)
        self.assertEqual(matched_results[0]['result'], "Elizabeth Elizabeth Elizabeth!")
        self.assertEqual(matched_results[1]['result'], "Elizabeth says 'Elizabeth is great!'")


if __name__ == '__main__':
    unittest.main()
