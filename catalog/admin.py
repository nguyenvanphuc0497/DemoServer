from django.contrib import admin
from .models import Book, BookInstance, Author, Genre

# Register your models here.
admin.site.register(BookInstance)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
