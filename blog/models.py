# 引入
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Post(文章) Class
class Post(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
