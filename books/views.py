from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
# Create your views here.


class BookListView(ListView):
    template_name = 'books/book_list.html'
    model = Book
    context_object_name = 'book_list'


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
