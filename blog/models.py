# blog/models.py
from django.db import models


class Post(models.Model):
    """ブログ"""
    title = models.CharField('タイトル', max_length=40)
    text = models.TextField('本文')
