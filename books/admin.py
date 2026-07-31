# Import Django admin module.
from django.contrib import admin

# Import Book model.
from .models import Book

# Register Book model so it appears
# in Django administration panel.
admin.site.register(Book)