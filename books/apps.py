# Import the AppConfig class from Django's apps module.
# AppConfig is used to configure an application in a Django project.
from django.apps import AppConfig


# Create a new configuration class for the 'books' application.
# This class inherits from Django's built-in AppConfig class.
class BooksConfig(AppConfig):

    # Specify the default type of primary key for models in this app.
    # BigAutoField creates a 64-bit integer that automatically increments.
    # If you don't explicitly define a primary key in a model,
    # Django will use BigAutoField by default.
    default_auto_field = 'django.db.models.BigAutoField'

    # Specify the name of the application.
    # This should match the app folder name.
    # Django uses this to identify and register the app.
    name = 'books'