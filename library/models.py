from django.db import models
from django.contrib.auth.models import AbstractUser

from gmc_test.utils import transliterate


class Book(models.Model):
    isbn = models.CharField(max_length=13, help_text="Enter the ISBN of the book")
    title = models.CharField(max_length=75, help_text="Enter the title of the book")
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    description = models.TextField(max_length=255, help_text="Enter a description for the book")
    category = models.ForeignKey('Category', related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.isbn} / {self.title}'


class Author(models.Model):
    first_name = models.CharField(max_length=50, help_text="Enter the author's first name")
    last_name = models.CharField(max_length=50, help_text="Enter the author's last name")

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Category(models.Model):
    supercategory = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=75, help_text="Enter category name")
    slug = models.CharField(max_length=100, editable=False, null=True, blank=True)

    def __str__(self):
        if self.supercategory:
            return f'{self.name} /{self.supercategory}'
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = transliterate(self.name)
        return super(Category, self).save()

    class Meta:
        verbose_name_plural = 'Categories'


class User(AbstractUser):
    USER_GROUPS = [
        ('admin', 'administrator'),
        ('client', 'client'),
    ]
    user_group = models.CharField(max_length=10, choices=USER_GROUPS,
                                  help_text='Select user group', default='client')

    def check_group(self, group):
        return group == self.user_group
