from django.db import models
from django.conf import settings
from accounts.models import User

class Post(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    title = models.CharField(max_length=14, null=False, blank=False)
    photo = models.ImageField(upload_to='post_photo', null=False, blank=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True, null = False, blank=False)
    post = models.ForeignKey('postapp.Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    
    def __str__(self):
        return self.comment
        