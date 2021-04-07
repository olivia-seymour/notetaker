from django.db import models
from datetime import datetime    


# Create your models here.
class noteItem(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    
