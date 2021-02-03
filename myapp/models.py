from django.db import models

class Post(models.Model):
    name = models.CharField(max_length = 250)
    description = models.TextField()
    price = models.IntegerField()
        
    class Meta:
        db_table = "posts"

