from rest_framework.test import APITestCase
from rest_framework import status
from interfaces.models import Book, BorrowingRecord

class BookViewSetTest(APITestCase):
    def test_create_book(self):
        data = {
            "title": "Test Book",
            "author": "Test Author",
            "isbn": "1234567890123",
            "available_copies": 5
        }
        response = self.client.post('/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "Test Book")

    def test_list_books(self):
        Book.objects.create(title="Book 1", author="Author 1", isbn="123", available_copies=2)
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class BorrowingRecordViewSetTest(APITestCase):
    def test_create_borrowing_record(self):
        book = Book.objects.create(title="Book 1", author="Author 1", isbn="123", available_copies=2)
        data = {
            "member_id": 1,
            "book": book.id
        }
        response = self.client.post('/borrowing-records/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['member_id'], 1)

    def test_list_borrowing_records(self):
        book = Book.objects.create(title="Book 1", author="Author 1", isbn="123", available_copies=2)
        BorrowingRecord.objects.create(member_id=1, book=book)
        response = self.client.get('/borrowing-records/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
