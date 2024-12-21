from django.test import TestCase
from infrastructure.models import Book, Borrow

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Django for APIs",
            author="William S. Vincent",
            isbn="1234567890123",
            available_copies=5
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Django for APIs")
        self.assertEqual(self.book.available_copies, 5)

    def test_book_str(self):
        self.assertEqual(str(self.book), "Django for APIs by William S. Vincent (ISBN: 1234567890123)")

class BorrowModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Django for APIs",
            author="William S. Vincent",
            isbn="1234567890123",
            available_copies=5
        )
        self.borrow = Borrow.objects.create(
            member_name="Alice",
            book=self.book
        )

    def test_borrow_creation(self):
        self.assertEqual(self.borrow.member_name, "Alice")
        self.assertEqual(self.borrow.book, self.book)

    def test_borrow_str(self):
        self.assertEqual(str(self.borrow), "Alice borrowed Django for APIs")
