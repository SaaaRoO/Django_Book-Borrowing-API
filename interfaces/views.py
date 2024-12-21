from rest_framework import generics
from infrastructure.models import Book, Borrow
from .serializers import BookSerializer, BorrowSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def root_view(request):
    return Response({"message": "Welcome to the Library System API!"})


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BorrowListCreateView(generics.ListCreateAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
