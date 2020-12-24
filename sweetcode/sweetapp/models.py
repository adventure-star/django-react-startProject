from django.db import models

class Post (models.Model):
   author = models.CharField(max_length=100)
   title = models.CharField(max_length=100)
   content = models.TextField(max_length=1000)

   def __str__(self):
       return self.title
