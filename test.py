from pprint import pprint
import unittest
from main import clean_book_title, calc_book_metrics, collect_data_from_csv

class TestBookFunctions(unittest.TestCase):
    def test_clean_book_title(self):
        # Test cases for clean_book_title
        self.assertEqual(clean_book_title("  The Great Gatsby  "), "the great gatsby")
        self.assertEqual(clean_book_title(" To Kill a Mockingbird "), "to kill a mockingbird")
        self.assertEqual(clean_book_title("  The Catcher in the Rye"), "the catcher in the rye")

    def test_calc_book_metrics(self):
        # Test cases for calc_book_metrics
        book_entry1 = {'Lauren O': 1.0, 'Alma W': 2.5, 'Gabriel B': 2.0, 'David B': 0.0, 'Farrah P': 2.5}
        book_entry2 = {'Alice A': 5.0, 'Bob B': 5.0, 'Carol C': 5.0}
        book_entry3 = {'John D': 1.0, 'Jane E': 3.0, 'Jim F': 4.0}

        # Test 1: Testing calculation of average rating
        self.assertAlmostEqual(calc_book_metrics("Book1", book_entry1)[1], 1.6, places=2)
        self.assertAlmostEqual(calc_book_metrics("Book2", book_entry2)[1], 5.0, places=2)
        self.assertAlmostEqual(calc_book_metrics("Book3", book_entry3)[1], 2.67, places=2)

        # Test 2: Testing calculation of number of 5-star reviews
        self.assertEqual(calc_book_metrics("Book1", book_entry1)[2], 0)
        self.assertEqual(calc_book_metrics("Book2", book_entry2)[2], 3)
        self.assertEqual(calc_book_metrics("Book3", book_entry3)[2], 0)

    def test_collect_data_from_csv(self):
        # Test cases for collect_data_from_csv with the provided reference file.

        # Test 1: Check if the data is correctly collected from the reference file.
        data1 = collect_data_from_csv("test_ratings.csv")
        correct_data1 = {
            "gödel's proof": {'Lauren O': 5.0},
            'primed to perform': {'Jordan S': 3.0, 'David B': 3.5},
            'design patterns: elements of reusable object-oriented software': {'Alex M': 0.5},
            'extreme ownership': {'Alex M': 1.0, 'Cory E': 5.0, 'Sam B': 4.5},
            'the tangled web': {'Eva Z': 3.0, 'Michael G': 4.5},
            "computer systems: a programmer's perspective": {'Zach S': 4.5},
            'the art of computer programming': {'Sameeta D': 4.0, 'Alma W': 5.0},
            'resilient management': {'Farrah P': 2.0},
            'the whole earth catalog': {'Angela C': 4.0},
            'conscious business: how to build value through values': {'Scott D': 2.5},
            'crucial conversations': {'Andrew L': 1.5, 'Edward Z': 2.0},
            'setting the table': {'Sherly T': 4.0}
        }
        self.assertEqual(correct_data1, data1)

        # Test 2: Check if the data is correctly collected from the reference file with mixed case and whitespace.
        data2 = collect_data_from_csv("test_ratings.csv")
        correct_data2 = {
            "gödel's proof": {'Lauren O': 5.0},
            'primed to perform': {'Jordan S': 3.0, 'David B': 3.5},
            'design patterns: elements of reusable object-oriented software': {'Alex M': 0.5},
            'extreme ownership': {'Alex M': 1.0, 'Cory E': 5.0, 'Sam B': 4.5},
            'the tangled web': {'Eva Z': 3.0, 'Michael G': 4.5},
            "computer systems: a programmer's perspective": {'Zach S': 4.5},
            'the art of computer programming': {'Sameeta D': 4.0, 'Alma W': 5.0},
            'resilient management': {'Farrah P': 2.0},
            'the whole earth catalog': {'Angela C': 4.0},
            'conscious business: how to build value through values': {'Scott D': 2.5},
            'crucial conversations': {'Andrew L': 1.5, 'Edward Z': 2.0},
            'setting the table': {'Sherly T': 4.0}
        }
        self.assertEqual(correct_data2, data2)

if __name__ == '__main__':
    unittest.main()




