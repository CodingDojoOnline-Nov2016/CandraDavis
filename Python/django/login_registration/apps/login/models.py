from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserManager(models.Manager):
    def new_user(self, request):
        errors = []
        print reg_user
        print '9'*50
        if len(request.POST['first_name']) < 2:
            errors.append('Please enter a valid First Name')
        elif not request.POST['first_name'.isalpha():
            errors.append('Please enter a valid First Name')
        if len(request.POST['last_name']) < 2: 
            errors.append('Please enter a valid Last Name')
        elif not request.POST['last_name'].isalpha():
            errors.append('Please enter a valid Last Name')
        elif len(request.POST['email']) < 1:
            errors.append('Please enter your email')
        elif not re.match(EMAIL_REGEX, request.POST['email']):
            errors.append('Please enter a valid Email address')
        elif not request.POST['password'].encode() == request.POST['pw_confirm'].encode():
            errors.append('Please enter matching passwords')
        elif not len(request.POST['password'].encode()) < 8:
            errors.append('Password must be at least 8 characters')
        if len(errors) > 0:
            return(False, errors)
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            pw_confirm = request.POST['pw_confirm'].encode()
            pw_hash = bcrypt.hashpw(pw_confirm, bcrypt.gensalt())
            u = User.objects.create(first_name=first_name, last_name=last_name, email=email, pw_hash=pw_hash)
            u.save()
            return(True, u)

    def login(self, session):
        errors = []
        u = User.objects.get(request.session['email']=email)
        if len(request.session['email']) < 1:
            errors.append('Please enter your email')
        elif not re.match(EMAIL_REGEX, request.session['email']):
            errors.append('Please enter a valid email')
        elif not len(request.session['password']) > 8:
            errors.append('Invalid email')
        elif not bcrypt.hashpw(request.session['password'], hashed) == u.pw_hash:
            errors.append('Invlaid password')
            return(False, errors)
        else:
            return(True, u)

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()
