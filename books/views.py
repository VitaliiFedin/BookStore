from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View, FormView
from .models import Book
from django.urls import reverse_lazy
from django.urls import reverse
from .forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic.detail import SingleObjectMixin


# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    template_name = 'books/book_list.html'
    model = Book
    context_object_name = 'book_list'
    login_url = 'account_login'


class ReviewGet(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    login_url = 'account_login'
    permission_required = 'books.special_status'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm
        return context


class ReviewPost(SingleObjectMixin, FormView):
    model = Book
    form_class = ReviewForm
    template_name = 'books/book_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        review = form.save(commit=False)
        review.book = self.object
        review.author = self.request.user
        review.save()
        return super().form_valid(form)

    def get_success_url(self):
        book = self.get_object()
        return reverse('book_detail', kwargs={'pk': book.id})


class BookDetailView(LoginRequiredMixin,  View):
    def get(self, request, *args, **kwargs):
        view = ReviewGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ReviewPost.as_view()
        return view(request, *args, **kwargs)


class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = 'books/book_create.html'
    model = Book
    fields = (
        'title',
        'author',
        'price',
        'cover'
    )

    def form_valid(self, form):
        form.instance.post_author = self.request.user
        return super().form_valid(form)


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    success_url = reverse_lazy('book_list')
    model = Book
    template_name = 'books/book_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.post_author == self.request.user


class BookEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    template_name = 'books/book_edit.html'
    fields = (
        'title',
        'author',
        'price',
        'cover',
    )

    def test_func(self):
        obj = self.get_object()
        return obj.post_author == self.request.user
