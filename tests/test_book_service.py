import pytest
from unittest.mock import MagicMock
from application.book_service import BookService
from core.models import Book, BorrowingRecord

@pytest.fixture
def book_repo():
    return MagicMock()

@pytest.fixture
def borrowing_repo():
    return MagicMock()

@pytest.fixture
def book_service(book_repo, borrowing_repo):
    return BookService(book_repo, borrowing_repo)

def test_borrow_book_success(book_service, book_repo, borrowing_repo):
    book = Book(title="Test Book", author="Author", isbn="123", available_copies=3)
    book_repo.get_by_isbn.return_value = book
    borrowing_repo.save.return_value = None

    record = book_service.borrow_book(member_id=1, isbn="123")
    assert record is not None
    book_repo.save.assert_called_once_with(book)
    borrowing_repo.save.assert_called_once()

def test_borrow_book_no_available_copies(book_service, book_repo):
    book = Book(title="Test Book", author="Author", isbn="123", available_copies=0)
    book_repo.get_by_isbn.return_value = book

    record = book_service.borrow_book(member_id=1, isbn="123")
    assert record is None
