from __future__ import unicode_literals

from django.db import models
from ..login.models import User
# Create your models here.

class BookManager(models.Manager):
    def new_book_review(self, data):
        errors = []

        if len(data['title']) < 1:
            errors.append('Please enter a valid Book Title')
        elif not data['title'].isalpha():
            errors.append('Please enter a valid Book Title')

        if len(data['author']) < 2:
            errors.append('Please enter a valid Author')
        elif not data['author'].isalpha():
            errors.append('Please enter a valid Author')

        if len(data['rating']) < 1:
            errors.append('Please enter your Rating')

        if len(data['review']) < 2:
            errors.append('Please enter your Review')
        elif not data['review'].isalpha():
            errors.append('Please enter a valid Review')

        if errors:
            return (False, errors)
        else:
            title = data['title']
            author = data['author']
            rating = int(data['rating'])
            review = data['review']
            new_book = Books.objects.create(title=title, author=author, rating=rating, review=review)
            return(True, new_book)
        
        # author = self.objects.get(author=data['author'])
        # elif author == data['author']:
        #     errors.append('Author al')






class Books(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=90)
    rating = models.SmallIntegerField(6)
    review = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

objects = BookManager()
