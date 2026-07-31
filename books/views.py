# Import Django REST Framework generic views.
from rest_framework import generics

# Import database model.
from .models import Book

# Import serializer.
from .serializers import BookSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    Handles:

    GET:
        Return all books.

    POST:
        Create a new book.
    """

    # Database query.
    queryset = Book.objects.all()

    # Serializer used for JSON conversion.
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyAPIView(
    # Import Django REST Framework generic views.
    generics.RetrieveUpdateDestroyAPIView
):
    """
    Handles one book object.

    GET: Retrieve one book.

    PUT/PATCH: Update book.

    DELETE: Remove book.
    """

    # Database query.
    queryset = Book.objects.all()
    # Serializer used for JSON conversion.
    serializer_class = BookSerializer