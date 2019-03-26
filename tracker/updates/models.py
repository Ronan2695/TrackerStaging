from django.db import models
import datetime
# Create your models here.
class Update(models.Model):
    Date = models.DateTimeField(null=False)
    Topic = models.CharField(max_length=100,null=False)
    From = models.CharField(max_length=100,null=False)
    Description = models.TextField(null=True, blank=False)
    Status = models.TextField(null=False, default='Active')
