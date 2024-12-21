from core.repo import BookRepository, BorrowRepository

class BookService:
    @staticmethod
    def list_books():
        return BookRepository.get_all_books()

    @staticmethod
    def add_book(data):
        return BookRepository.create_book(data)

    @staticmethod
    def update_book(book_id, data):
        return BookRepository.update_book(book_id, data)

class BorrowService:
    @staticmethod
    def borrow_book(member_name, book_id):
        # Check if the book exists and has available copies
        book = BookRepository.get_book_by_id(book_id)
        if not book or book.available_copies <= 0:
            return {"error": "Book is unavailable"}

        # Check if the member already has 2 borrowed books
        borrowed_books = BorrowRepository.get_borrowed_books(member_name)
        if borrowed_books.count() >= 2:
            return {"error": "You can only borrow up to 2 books at a time"}

        # Decrease the available copies and create a borrow record
        book.available_copies -= 1
        book.save()
        borrow_record = BorrowRepository.create_borrow_record({
            "member_name": member_name,
            "book": book,
        })
        return {"message": "Book borrowed successfully", "borrow_record": borrow_record}

    @staticmethod
    def list_borrowed_books(member_name):
        return BorrowRepository.get_borrowed_books(member_name)
