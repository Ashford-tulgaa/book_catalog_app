# Import Django's built-in testing framework.
from django.test import TestCase

# Import Django REST Framework test client.
from rest_framework.test import APIClient

# Import HTTP status codes for readable assertions.
from rest_framework import status

# Import our Book database model.
from .models import Book


class BookAPITestCase(TestCase):
    """
    -- Test suite for the Book Catalog REST API. --

    These tests verify that CRUD operations work correctly:
    - Create
    - Read
    - Update
    - Delete
    """

    def setUp(self):
        """
        Runs before every test.

        Creates:
        - API client
        - Sample book object
        """

        # Client used to send API requests.
        self.client = APIClient()

        # Create a sample book in the test database.
        self.book = Book.objects.create(
            title="Clean Code",
            author="Robert C. Martin",
            isbn="9780132350884",
            published_date="2008-08-01"
        )

    def test_create_book(self):
        """
        Test creating a new book using POST /api/books/
        """

        data = {
            "title": "The Pragmatic Programmer",
            "author": "Andrew Hunt",
            "isbn": "9780135957059",
            "published_date": "2019-09-13"
        }


        response = self.client.post(
            "/api/books/",
            data,
            format="json"
        )

        # Check that the API returns HTTP 201 Created.
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )


        # Verify the book was saved in the database.
        self.assertEqual(
            Book.objects.count(),
            2
        )

        # Verify returned data.
        self.assertEqual(
            response.json()["title"],
            "The Pragmatic Programmer"
        )

    def test_get_books(self):
        """
        Test retrieving books using GET /api/books/
        """

        response = self.client.get(
            "/api/books/"
        )

        # API should return HTTP 200 OK.
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Verify one book exists in response.
        self.assertEqual(
            len(response.json()),
            1
        )

        # Verify returned book title.
        self.assertEqual(
            response.json()[0]["title"],
            "Clean Code"
        )

    def test_update_book(self):
        """
        Test updating a book using PUT /api/books/<id>/
        """

        updated_data = {
            "title": "Clean Code Second Edition",
            "author": "Robert C. Martin",
            "isbn": "9780132350884",
            "published_date": "2008-08-01"
        }

        response = self.client.put(
            f"/api/books/{self.book.pk}/",
            updated_data,
            format="json"
        )

        # API should return HTTP 200 OK.
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Refresh object from database.
        self.book.refresh_from_db()

        # Check that title was updated.
        self.assertEqual(
            self.book.title,
            "Clean Code Second Edition"
        )

    def test_delete_book(self):
        """
        Test deleting a book using DELETE /api/books/<id>/
        """

        response = self.client.delete(
            f"/api/books/{self.book.pk}/"
        )

        # API should return HTTP 204 No Content.
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        # Verify object was removed.
        self.assertEqual(
            Book.objects.count(),
            0
        )