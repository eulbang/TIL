from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count
from .models import Author
from .serializers import AuthorSerializer

# Create your views here.
@api_view(['GET'])
def author_detail(request, author_pk):
    author = Author.objects.get(pk = author_pk)
    author = Author.objects.annotate(book_count=Count('book')).get(pk=author_pk)
    print(author.book_count)
    print(author.pk, author.name, len(author.book_set.all()))
    serializers = AuthorSerializer(author)
    return Response(serializers.data)
