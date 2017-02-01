from __future__ import unicode_literals

from django.db import models
from ..login.models import User
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=90)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class ReviewManager(models.Manager):
    def new_review(self, data, u_id):
        errors = []
        print data
        print u_id

        # data = request.POST
        if len(data['title']) < 1:
            errors.append('Please enter a valid Book Title')
        # elif not data['title'].isalpha():
        #     errors.append('Please enter a valid Book Title')

        if len(data['author']) < 2:
            errors.append('Please enter an Author name')
        # elif not data['author'].isalpha():
        #     errors.append('Please enter a valid Author')

        if int(data['rating']) < 1:
            errors.append('Please enter your Rating')

        if len(data['review']) < 2:
            errors.append('Please enter your Review')
        # elif not data['review'].isalpha():
        #     errors.append('Please enter a valid Review')

        if errors:
            return (False, errors)
        else:
            user = User.objects.get(pk=u_id)
            print '%'*100
            print user
            title = data['title']
            author = data['author']
            rating = int(data['rating'])
            review = data['review']
            new_book = Books.objects.create(title=title, author=author, rating=rating, review=review, user=user)
            print '^'*100
            print new_book
            return(True, new_book)

        # author = self.objects.get(author=data['author'])
        # elif author == data['author']:
        #     errors.append('Author al')


class Review(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    rating = models.SmallIntegerField(6)
    comments = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = BookManager()
