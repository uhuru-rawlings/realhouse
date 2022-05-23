from django.db import models

# Create your models here.
class Houses(models.Model):
    location = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    areaofland = models.IntegerField()
    lengthofhouse = models.IntegerField(default= 1)
    widthofhouse = models.IntegerField(default= 1)
    price = models.IntegerField()
    interiorimage1 = models.ImageField(upload_to = 'images')
    interiorimage2 = models.ImageField(upload_to = 'images')
    exteriorimage = models.ImageField(upload_to = 'images')
    description = models.CharField(max_length=7000, default="No description")

    class Meta:
        db_table = 'Houses'

    def __str__(self):
        return self.location