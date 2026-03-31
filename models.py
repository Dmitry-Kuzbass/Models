from django.db import models
from datetime import datetime

# Create your models here.

class Author(models.Model):
    total_post_rating = models.IntegerField(default = 0) #суммарный рейтинг каждой статьи автора умножаемый на 3
    comments_author = models.IntegerField(default = 0) #суммарный рейтинг всех комментариев автора
    post_comments_rating = models.IntegerField(default = 0) #суммарный рейтинг всех комментариев к статьям автора
    User = models.ForeignKey(User, on_delete=models.CASCADE)

