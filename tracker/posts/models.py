from django.db import models

# Create your models here.
class Post(models.Model):
    Year = models.PositiveSmallIntegerField(blank=True, null=True)
    Month = models.TextField()
    Date = models.DateTimeField()






    pub_data = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()
