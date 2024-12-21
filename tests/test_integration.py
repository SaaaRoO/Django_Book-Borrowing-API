from rest_framework.test import APITestCase
from interfaces.models import Book, BorrowingRecord

class IntegrationTest(APITestCase):
    def test_full_workflow(self):
        # Create a book
        book_data = {"title": "Book 1", "author": "Author", "isbn": "123", "available_copies": 3}
        book_response = self.client.post('/books/', book_data)
        self.assertEqual(book_response.status_code, 201)

        # Borrow the book
        borrow_data = {"member_id": 1, "book": book_response.data['id']}
        borrow_response = self.client.post('/borrowing-records/', borrow_data)
        self.assertEqual(borrow_response.status_code, 201)

        # Check that available copies were updated
        updated_book = Book.objects.get(id=book_response.data['id'])
        self.assertEqual(updated_book.available_copies, 2)
