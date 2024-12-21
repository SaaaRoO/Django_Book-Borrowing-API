from django.urls import path
from .views import BookListCreateView, BorrowListCreateView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('borrow/', BorrowListCreateView.as_view(), name='borrow-list-create'),
]
