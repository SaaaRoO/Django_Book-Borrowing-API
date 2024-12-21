from core.models import Book, BorrowingRecord

class BookRepository:
    def __init__(self, db_session):
        self.db_session = db_session
    
    def save(self, book: Book):
        self.db_session.add(book)
        self.db_session.commit()

    def get_by_isbn(self, isbn):
        return self.db_session.query(Book).filter_by(isbn=isbn).first()

class BorrowingRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def save(self, borrowing_record: BorrowingRecord):
        self.db_session.add(borrowing_record)
        self.db_session.commit()

    def get_by_member_id(self, member_id):
        return self.db_session.query(BorrowingRecord).filter_by(member_id=member_id).all()
