from rest_framework import serializers
from .models import Books

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ('title','authors','publishedDate','isbn13','isbn10','pageCount','imageLinks','language')