from django.db import models

# Create your models here.

sitepages = (
        ('0', u'Mainpage'),
        ('1', u'Sport'),
        ('2', u'Education'),
        ('3', u'Politics'),
        ('4', u'Nation'),
        ('5', u'State'),
    )
class edittor(models.Model):
    sitepages = (
        ('0', u'Mainpage'),
        ('1', u'Sport'),
        ('2', u'Education'),
        ('3', u'politics'),
        ('4', u'Nation'),
        ('5', u'State'),

    )

    eitName = models.CharField(max_length=200)
    eitPassword = models.CharField(max_length=140)
    accPage = models.CharField(
        max_length=32, choices=sitepages, null=True, blank=True)

    def __str__(self):
        template = '{0.eitName} {0.eitPassword}'
        return template.format(self)


class draft(models.Model):
    sitepages = (
        ('0', u'Mainpage'),
        ('1', u'Sport'),
        ('2', u'Education'),
        ('3', u'Politics'),
        ('4', u'Nation'),
        ('5', u'State'),
    )
    newspage = models.CharField(
        max_length=32, choices=sitepages, null=True, blank=False)
    newsthumbnail = models.ImageField(upload_to='images')
    newstitle = models.CharField(max_length=250, blank=False)
    newspara1 = models.TextField(max_length=800, blank=False)
    newspara2 = models.TextField(max_length=800, blank=False)
    newstime = models.DateTimeField()
    newsauthor = models.CharField(max_length=200, blank=False)
    status = models.CharField(
        max_length=15, blank=False, default='draft', editable=False)

    def __str__(self):
        template = '{0.newspage} {0.newstitle}'
        return template.format(self)


class herosection(models.Model):
    bignewsimage = models.ImageField(upload_to='images')
    bignewshedding = models.CharField(max_length=300, blank=False)
    bignewspara1 = models.TextField(max_length=800, blank=False)
    bignewspara2 = models.TextField(max_length=800, blank=False)
    heroad = models.ImageField(upload_to='images')
    newstime = models.DateTimeField()
    newsauthor = models.CharField(max_length=200, blank=False)


class herosectionnews(models.Model):
    sidecard1image = models.ImageField(upload_to='images')
    sidecard1hedding = models.CharField(max_length=300, blank=False)
    sidecard1para1 = models.TextField(max_length=800, blank=False)
    sidecard1para2 = models.TextField(max_length=800, blank=False)
    newstime = models.DateTimeField()
    newsauthor = models.CharField(max_length=200, blank=False)


class AdvertisementManger(models.Model):
    sitepages = (
        ('0', u'Mainpage'),
        ('1', u'Sport'),
        ('2', u'Education'),
        ('3', u'Politics'),
        ('4', u'Nation'),
        ('5', u'State'),
    )
    topage = models.CharField(
        max_length=32, choices=sitepages, null=True, blank=False)
    mainpagead = models.ImageField(upload_to='images')
    newspagead1 = models.ImageField(upload_to='images')
    newspagead2 = models.ImageField(upload_to='images')
    newspagead3 = models.ImageField(upload_to='images')

    def __str__(self):
        return u"%s" % (self.get_topage_display())
