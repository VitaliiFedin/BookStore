from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookDeleteView, BookEditView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('delete/<uuid:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('edit/<uuid:pk>',BookEditView.as_view(), name='book_edit'),
]