import unittest
from src.library import Library


class TestSprint1(unittest.TestCase):

    def test_add_book_success(self):
        lib = Library()
        lib.add_book("B101", "Clean Code", "Robert Martin")
        self.assertIn("B101", lib.books)

    def test_add_book_duplicate(self):
        lib = Library()
        lib.add_book("B101", "Clean Code", "Robert Martin")
        with self.assertRaises(ValueError):
            lib.add_book("B101", "Clean Architecture", "Robert Martin")
