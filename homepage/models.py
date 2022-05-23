from django.db import models

# Create your models here.
class Houses(models.Model):
    location = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    areaofland = models.IntegerField()
    areaofhouse = models.IntegerField()
    price = models.IntegerField()
    interiorimage1 = models.ImageField(upload_to = 'images')
    interiorimage2 = models.ImageField(upload_to = 'images')
    exteriorimage = models.ImageField(upload_to = 'images')

    class Meta:
        db_table = 'Houses'

    def __str__(self):
        return self.location