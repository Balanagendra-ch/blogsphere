from django.db import models

from django.db.models import Model

class RegistrationModel(Model):
    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default="yes")

class ArticleModel(models.Model):
    title= models.CharField(max_length=5000)
    description= models.CharField(max_length=5000)
    date= models.CharField(max_length=100)
    userid= models.CharField(max_length=50)
    category= models.CharField(max_length=5000)
    banner_image= models.FileField(upload_to="images")
    resource_link= models.CharField(max_length=5000)

class CommentModel(models.Model):

    text = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.CharField(max_length=60)
    article = models.CharField(max_length=60)

class SearchHistoryModel(models.Model):

    keyword = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.CharField(max_length=60)

class LikeOrDisLikeModel(models.Model):
    status = models.CharField(max_length=100)
    user = models.CharField(max_length=60)
    article = models.CharField(max_length=60)