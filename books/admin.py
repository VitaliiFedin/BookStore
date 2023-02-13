from django.contrib import admin
from .models import Book, Review


class ReviewInLine(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInLine
    ]
    list_display = ('title', 'author', 'price', 'post_author')


admin.site.register(Book, BookAdmin)
admin.site.register(Review)
