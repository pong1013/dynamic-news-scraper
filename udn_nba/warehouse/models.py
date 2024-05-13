from django.db import models
import datetime
# Create your models here.
class UdnFocus(models.Model):
    title = models.CharField(max_length= 127)
    author = models.CharField(max_length=64, default='Unknown')
    publish_time = models.DateTimeField(default=datetime.datetime.now)
    content = models.TextField()
    
    
    def __str__(self):
        return self.title
    
