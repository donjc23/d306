from django.db import models
from blog.apps.blog_page.managers import CommentManager


# Create your models here.
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length = 64)
    text = models.TextField()
    published = models.BooleanField(db_index = True, default=True)

    objects = CommentManager()

    def __unicode__(self):
        return u"%s - %s" % (self.name, self.created)
        
