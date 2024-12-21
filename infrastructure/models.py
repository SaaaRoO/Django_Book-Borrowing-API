from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    available_copies = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Borrow(models.Model):
    member_name = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrow_records")
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.member_name} borrowed {self.book.title}"
