from infrastructure.models import Book, Borrow

class BookRepository:
    @staticmethod
    def get_all_books():
        return Book.objects.all()

    @staticmethod
    def create_book(data):
        return Book.objects.create(**data)

    @staticmethod
    def get_book_by_id(book_id):
        return Book.objects.filter(id=book_id).first()

    @staticmethod
    def update_book(book_id, data):
        book = Book.objects.filter(id=book_id).first()
        if book:
            for field, value in data.items():
                setattr(book, field, value)
            book.save()
            return book
        return None

class BorrowRepository:
    @staticmethod
    def create_borrow_record(data):
        return Borrow.objects.create(**data)

    @staticmethod
    def get_borrowed_books(member_name):
        return Borrow.objects.filter(member_name=member_name, returned_at=None)
