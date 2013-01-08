from django.db import models

# Create your models here.
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length = 64)
    text = models.TextField()
    published = models.BooleanField(db_index = True, default=True)


    def __unicode__(self):
        return u"%s - %s" % (self.name, self.created)
        
