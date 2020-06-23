from rest_framework import generics

from .models import Book
from .permissions import ISAuthorOrReadOnly
from .serializers import BooksSerializer

# Create your views here.
class BooksList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

class BooksDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (ISAuthorOrReadOnly)
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

