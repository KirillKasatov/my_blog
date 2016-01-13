from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from sorl.thumbnail import ImageField

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __unicode__(self):
        return self.title


class Comment(MPTTModel):
    article = models.ForeignKey(Article, related_name='comments')
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', db_index=True)
    text = models.TextField()
    time = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return self.text
