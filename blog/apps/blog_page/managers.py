from django.db import models

class CommentManager(models.Manager):
    def published_comments(self):
        return self.model.objects.filter(published = True)
        
