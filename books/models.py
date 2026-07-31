from django.db import models

class Book(models.Model):
    """
    Book model represents a single book stored in the catalog database.
    Each Book object becomes one database record.
    """

    # Stores the title of the book.
    # Example:
    # "48 Laws of Power"
    title = models.CharField(
        max_length=255
    )

    # Stores the author's name.
    # Example:
    # "Robert Greene"
    author = models.CharField(
        max_length=255
    )

    # Stores the ISBN number.
    # ISBN identifies a book uniquely.
    # unique=True prevents duplicate ISBN values.
    # Example: 9780132350884
    isbn = models.CharField(
        max_length=13,
        unique=True
    )

    # Stores the date the book was published.
    # Example:
    # "1998-09-01"
    published_date = models.DateField()

    def __str__(self):
        """
        Defines the string representation of the object.

        Used by:
        - Django admin panel
        - Django shell
        """

        return self.title