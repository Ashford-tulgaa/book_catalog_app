# Import Django REST Framework serializer tools.
from rest_framework import serializers

# Import our database model.
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Converts Book model objects into JSON responses
    and validates incoming JSON requests.
    """


    class Meta:

        # Tell serializer which model it represents.
        model = Book

        # Include every model field:
        # id
        # title
        # author
        # isbn
        # published_date
        fields = "__all__"



    def validate_title(self, value):
        """
        Validate that title is not empty.
        """

        if not value.strip():

            raise serializers.ValidationError(
                "Title cannot be empty."
            )

        return value


    def validate_author(self, value):
        """
        Validate that author is not empty.
        """

        if not value.strip():

            raise serializers.ValidationError(
                "Author cannot be empty."
            )

        return value


    def validate_isbn(self, value):
        """
        Validate ISBN format.

        ISBN must:
        - contain numbers only
        - be 10 or 13 digits
        """

        if not value.isdigit():

            raise serializers.ValidationError(
                # Raise a validation error if the ISBN contains non-numeric characters.
                "ISBN must contain only numbers."
            )


        if len(value) not in [10, 13]:
            # Raise a validation error if the ISBN is not 10 or 13 digits long.
            raise serializers.ValidationError(
                "ISBN must be 10 or 13 digits."
            )


        return value