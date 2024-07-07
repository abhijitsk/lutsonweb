from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='img/%y')
    lutsImage1 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage2 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage3 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage4 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage5 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage6 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage7 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage8 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage9 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage10 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage11 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage12 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage13 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage14 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage15 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage16 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage17 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage18 = models.ImageField(upload_to='output/',null=True, blank=True)
    lutsImage19 = models.ImageField(upload_to='output/',null=True, blank=True)

    def __str__(self):

        return self.caption