from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Genre
from .serializers import GenreSerializer

# Create your views here.
@api_view(["GET"])
def genre(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreSerializer(genre)
    return Response(serializer.data, status = status.HTTP_200_OK)