from rest_framework import serializers
from .models import Author

# class SomeSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     content = serializers.CharField()
#     opening_time = serializers.TimeField()

#     class Meta:
#         read_only_fields = ('opening_time')

class AuthorSerializer(serializers.ModelSerializer):
    # book_count = serializers.IntegerField(source='book_set.count', read_only=True)
    book_count = serializers.SerializerMethodField()

    def get_book_count(self, obj):
        return obj.book_count
    
    class Meta:
        model = Author
        fields = '__all__'