from django.db import models
from django.contrib.auth.models import User


class BlogArticle(models.Model):
    title = models.CharField(max_length = 500)
    blog_content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    #here author is the user that log-in, so author and user should have same id