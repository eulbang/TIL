from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BorrowBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, isbn):
        try:
            book = Book.objects.get(isbn=isbn)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=404)

        book.borrowed = True
        book.save()
        serializer = BookSerializer(book)
        return Response(serializer.data)