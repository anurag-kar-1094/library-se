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
class TestSprint2(unittest.TestCase):

    def test_borrow_available_book(self):
        lib = Library()
        lib.add_book("B201", "Refactoring", "Martin Fowler")
        lib.borrow_book("B201")
        self.assertEqual(lib.books["B201"]["status"], "Borrowed")

    def test_borrow_unavailable_book(self):
        lib = Library()
        lib.add_book("B201", "Refactoring", "Martin Fowler")
        lib.borrow_book("B201")
        with self.assertRaises(ValueError):
            lib.borrow_book("B201")

    def test_return_book(self):
        lib = Library()
        lib.add_book("B201", "Refactoring", "Martin Fowler")
        lib.borrow_book("B201")
        lib.return_book("B201")
        self.assertEqual(lib.books["B201"]["status"], "Available")
class TestSprint3(unittest.TestCase):

    def test_generate_report_header(self):
        lib = Library()
        lib.add_book("B301", "Domain-Driven Design", "Eric Evans")
        report = lib.generate_report()
        self.assertIn("BOOK ID", report)

    def test_generate_report_contains_book(self):
        lib = Library()
        lib.add_book("B301", "Domain-Driven Design", "Eric Evans")
        report = lib.generate_report()
        self.assertIn("B301", report)
