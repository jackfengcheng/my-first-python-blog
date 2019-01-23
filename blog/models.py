from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=32,default='Title')
    content=models.TextField(null = True)

#第一步python manage.py makemigrations
#第二部python manage.py migrate
#第三部python manage.py sqlmigrate blog 0001