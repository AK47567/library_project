from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_no', 'title', 'author', 'genre']

        """
        This serializer serializes Book model instances.
        
        """