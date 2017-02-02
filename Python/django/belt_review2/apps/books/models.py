from __future__ import unicode_literals

from django.db import models
from ..login.models import User

# Create your models here.
class AuthorManager(models.Manager):
    def valid_author(self, data):
        errors = []
        print '%'*75
        print data
        # print data['author_name']
        if len(data) < 2:
            errors.append('Please enter an Author name')
        # elif not data['author_name'].isalpha():
        #     errors.append('Please enter a valid Author')
        else:
            if errors:
                return(False, errors)
            else:
                author_name = data
                author = self.create(author_name=author_name)
                return(True, author)
            # try:
            #     author = self.get[author_name=data['author_name']]
            # except:
            #     author_name = data['author_name']
            #     author = self.create(author_name=author_name)


class Author(models.Model):
    author_name = models.CharField(max_length=45)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = AuthorManager()

class BookManager(models.Manager):
    def book_validation(self, data, u_id):
        errors = []
        if len(data['title']) < 1:
            errors.append('Please enter a valid Book Title')
        #have to check how to do .isalpha validations on unicode strings in django
        # elif not data['title'].isalpha():
        #     errors.append('Please enter a valid Book Title')
        # elif data['title'] == Book.objects.get(title=data['title']):
        #     errors.append('Title already exists. Please select book title from homepage to submit a new review')
        else:
            if errors:
                return(False, errors)
            else:
                try:
                    author = Author.objects.get(author=data['author_name'])
                    print '$'*60
                except:
                    author = Author.objects.valid_author(data['author_name'])
                print '#'*60

        if author[0] == False:
            return(False, author[1])
        else:
            title = data['title']
            user = User.objects.get(pk=u_id)
            print author[1].id
            print '<-----------------------here is my author tuple'
            author_id = author[1].id
            author = Author.objects.get(pk=author_id)
            book = self.create(title=title, author=author, user=user)
            return(True, book)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author)
    user = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = BookManager()

class ReviewManager(models.Manager):
    def valid_review(request, data, u_id):
        errors = []
        print '='*75
        print data
        print '+'*75
        print u_id
        if len(data['comments'])<2:
            errors.append('Please enter your review')
        # elif not data['comments'].isalpha():
        #     errors.append('Please enter a valid format for your review')
        else:
            pass

        if int(data['rating'])<1:
            errors.append('Please enter your rating')
        else:
            pass

        if errors:
            return(False, errors)
        else:
            # try:
            #     add_book = Book.objects.get(title=data['title'])
            #     print add_book
            #
            #     # add_author = Author.objects.get(author_name=data['author_name'])
            # except:
                # add_author = Author.objects.valid_author['author_name']
                add_book = Book.objects.book_validation(data, u_id)
                '#'*75
                print add_book

        # if add_author[0] == False:
        #     return(False, add_author[1])
        if add_book[0] == False:
            return(False, add_book[1])
        else:
            print 'L'*75
            print add_book[1].id
            book_id = add_book[1].id
            book = Book.objects.get(pk=book_id)
            print add_book[1].author
            author = add_book[1].author
            user = User.objects.get(pk=u_id)
            comments = data['comments']
            rating = int(data['rating'])
            new_review = Review.objects.create(book=book, user=user, comments=comments, rating=rating) #author=author?
            return(True, new_review)#, add_book[1].title, add_author[1].author_name

    def recent_review(self):
        reviews = self.order_by('-updated_at')[:3] #.filter(book__title)
        # user = User.objects.get(user__user_name).filter
        print reviews
        return(reviews)#, user

    def book_all_reviews(self, b_id):
        reviews = self.order_by('-updated_at').get(book=b_id) #.get(user__user_name)
        print reviews
        return(reviews)

    def add_new_review(self, data):
        errors = []
        if len(data['comments'])<2:
            errors.append('Please enter your review')
        elif not data['review'].isalpha():
            errors.append('Please enter a valid format for your review')
        else:
            pass
        if int(data['rating'])<1:
            errors.append('Please enter your rating')
        else:
            pass

        if errors:
            return(False, errors)
        else:
            book = Book.get(id=data['b_id'])
            user = request.session['u_id']
            rating = data['rating']
            comments = data['comments']
            self.create(book=book, user=user, rating=rating, comments=comments)
            recent_review()
            return(True)

    def destroy_review(self, r_id):
        pass

class Review(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    rating = models.SmallIntegerField(6)
    comments = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = ReviewManager()
