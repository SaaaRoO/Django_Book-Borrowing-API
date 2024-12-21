from django.test import TestCase
from interfaces.serializers import BookSerializer, BorrowingRecordSerializer
from interfaces.models import Book, BorrowingRecord

class BookSerializerTest(TestCase):
    def test_book_serializer(self):
        data = {
            "title": "Test Book",
            "author": "Test Author",
            "isbn": "1234567890123",
            "available_copies": 3
        }
        serializer = BookSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        book = serializer.save()
        self.assertEqual(book.title, "Test Book")

class BorrowingRecordSerializerTest(TestCase):
    def test_borrowing_record_serializer(self):
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            isbn="1234567890123",
            available_copies=5
        )
        data = {
            "member_id": 1,
            "book": book.id
        }
        serializer = BorrowingRecordSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        record = serializer.save()
        self.assertEqual(record.member_id, 1)
