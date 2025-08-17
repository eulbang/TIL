from rest_framework import serializers
from .models import Book, Genre
from authors.models import Author

class SimpleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    author = SimpleAuthorSerializer() 
    
    class Meta:
        model = Book
        fields = ['title', 'author']

class GenreSerializer(serializers.ModelSerializer):
    book_count = serializers.SerializerMethodField()
    books = BookSerializer(many=True, source='book_set')
    name = serializers.CharField(source='genre')

    class Meta:
        model = Genre
        fields = ['name', 'books', 'book_count']

    def get_book_count(self, obj):
        return obj.book_set.count()