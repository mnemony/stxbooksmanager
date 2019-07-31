from django.db import models


# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=250)
    authors = models.CharField(max_length=250)
    publishedDate = models.DateField(blank=True, null=True)
    isbn13 = models.CharField(max_length=25)
    isbn10 = models.CharField(max_length=25)
    pageCount = models.IntegerField(blank=True, null=True)
    imageLinks = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=5)

    def __str__(self):
        return self.title

