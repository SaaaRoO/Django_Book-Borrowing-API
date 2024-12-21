from rest_framework import serializers
from infrastructure.models import Book, Borrow

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'available_copies']


class BorrowSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)
    book_author = serializers.CharField(source='book.author', read_only=True)

    class Meta:
        model = Borrow
        fields = [
            'id',
            'member_name',
            'book',
            'book_title',
            'book_author',
            'borrowed_at',
            'returned_at',
        ]
