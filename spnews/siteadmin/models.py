from django.db import models
from django.utils.timezone import now
# Create your models here.
class News(models.Model):
    headding  = models.CharField(max_length=600,blank=True)
    para1  = models.CharField(max_length=1200,blank=True)
    para2  = models.CharField(max_length=1200,blank=True)
    img = models.ImageField(upload_to='images')
    tag = models.CharField(max_length=600,blank=True)
    location = models.CharField(max_length=100,blank=True)
    date = models.DateTimeField(default=now, editable=False)
    status = models.CharField(max_length=500,default="DRAFT",editable=False)
    rejectreason = models.CharField(max_length=600,default="none",editable=False)
    author = models.CharField(max_length=350,blank=False)