from django.db import models
from django.utils.timezone import now
category = (    
    ('India','India'),
    ('Sport','Sport'),
    ('Education','Education')
)
section =(
('Main Page Hero Horizontal','Main Page Hero Horizontal'),
('Main Page Hero slide 1','Main Page Hero slide 1'),
('Main Page Hero slide 2','Main Page Hero slide 2'),
('Main Page Hadding News','Main Page Hadding News'),
('Main Page Sport News','Main Page Sport News'),
('Main Page Sport Polites','Main Page Sport Polites')
)
class MainNews(models.Model):
    headding  = models.CharField(max_length=600,blank=True)
    location = models.CharField(max_length=100,blank=True)
    para1  = models.CharField(max_length=1200,blank=True)
    para2  = models.CharField(max_length=1200,blank=True)
    tag = models.CharField(max_length=600,blank=True)
    img = models.ImageField(upload_to='images')
    date = models.DateTimeField(default=now, editable=False)
    author = models.CharField(max_length=350,blank=False)
    # category = models.CharField(max_length=100, choices=category, default='India')
    # category = models.CharField(max_length=100, choices=section, default='Main Page Hero Horizontal')
    category = models.CharField(max_length=100,blank=True, default = "None")
    section = models.CharField(max_length=100,blank=True, default = "None")
