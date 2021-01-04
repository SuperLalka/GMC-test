from django.contrib import admin

from library.models import (
    Author, Book, Category, User
)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'author', 'category')
    list_filter = ('author', 'category')
    search_fields = ['title', 'isbn']
    list_per_page = 50


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'supercategory')
    search_fields = ['name']
    list_per_page = 50


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    search_fields = ['last_name']
    list_per_page = 50


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_group', 'is_active', 'is_staff')
    list_filter = ('user_group', 'is_staff')
    list_per_page = 20
