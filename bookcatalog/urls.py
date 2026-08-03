# Import Django URL tools.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Django administration interface.
    path(
        "admin/",
        admin.site.urls
    ),

    # Book API routes.
    # All book endpoints begin with: /api/books/
    path(
        # Include the book API routes from the books app.
        "books/",
        include("books.urls")
    ),
]