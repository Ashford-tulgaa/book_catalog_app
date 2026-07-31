# Import Django URL routing.
from django.urls import path

# Import API views.
from .views import (
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
)

urlpatterns = [

    # Collection endpoint.
    # GET: /api/books/
    # POST: /api/books/
    path(
        "books/",
        BookListCreateAPIView.as_view(),
        name="book-list-create"
    ),

    # Single book endpoint.
    # GET: /api/books/1/
    # PUT: /api/books/1/
    # DELETE: /api/books/1/
    path(
        "books/<int:pk>/",
        BookRetrieveUpdateDestroyAPIView.as_view(),
        name="book-detail"
    ),
]