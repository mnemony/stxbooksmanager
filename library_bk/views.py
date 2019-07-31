from django.shortcuts import render,get_object_or_404
from .models import Books
from .choices import publishedDate_choices
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import BooksForm
import requests
from .serializers import BooksSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter



# Create your views here.

def index(request):
    books_data = Books.objects.all()

    context = {
        'books_data': books_data
    }


    return render(request, 'library_bk/index.html', context)

def about(request):
    return render(request, 'library_bk/about.html')

def new(request):

    if request.method != 'POST':
        form = BooksForm()
    else:
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('search'))

    context = {'form': form}
    return render(request, 'library_bk/new.html', context) 



def search(request):

    query_books = Books.objects.order_by('-publishedDate')

    if 'titles' in request.GET:
        title = request.GET['titles']
        if title:
            query_books = query_books.filter(title__icontains=title)

    if 'author' in request.GET:
        author = request.GET['author']
        if author:
            query_books = query_books.filter(authors__icontains=author)

    if 'lang' in request.GET:
        lang = request.GET['lang']
        if lang:
            query_books = query_books.filter(language__icontains=lang)        

         

    context = {
        'books_data': query_books,
        'publishedDate_choices': publishedDate_choices,
    }

    return render(request, 'library_bk/search.html',context)

def result(request):

    context = {
      'publishedDate_choices': publishedDate_choices,
    }

    return render(request, 'library_bk/result.html',context)

class RestBooks(APIView): 

    def get(self, request):
        book1 = Books.objects.all()
        serializer = BooksSerializer(book1, many=True)
        return Response(serializer.data)    

    def post(self):
        pass    