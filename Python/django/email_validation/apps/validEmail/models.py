from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
# Create your models here.
class EmailManager(models.Manager):
    def valid_email(self, email):
        errors = []
        if not re.match(EMAIL_REGEX, email):
            errors.append('Please enter a valid Email')
        elif len(email) < 1:
            errors.append('Please enter an Email')
        if len(errors) > 0:
            return(False, errors)
        else:
            v = Email.objects.create(email=email)
            v.save()
            return(True, v)
    def delete_email(self, id):
        d = Email.objects.get(id=id)
        if not d: #if the passed in id does not equal an id in the database...
            err_mess = 'Sorry, email not found.'
            return(False, err_mess)
        else:
            d.delete()
            return(True, d)

class Email(models.Model):
    email = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    # updated_at = models.DateField(auto_now=True)

    objects = EmailManager()
