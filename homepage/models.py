from django.db import models

# Create your models here.
class Houses(models.Model):
    HOUSE_TYPE = [("Single-Family Homes",("Single-Family Homes")),
                 ("Semi-Detached Home",("Semi-Detached Home")),
                 ("Multifamily Homes",("Multifamily Homes")),
                 ("Townhomes",("Townhomes")),
                 ("Apartments",("Apartments")),
                 ("Condominiums",("Condominiums")),
                 ("Co-Ops",("Co-Ops")),
                 ("Tiny Home ",("Tiny Home ")),
                 ("Mobile Home",("Mobile Home")),
    ]
    location = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    areaofland = models.IntegerField()
    lengthofhouse = models.IntegerField(default= 1)
    widthofhouse = models.IntegerField(default= 1)
    price = models.IntegerField()
    choices = models.CharField(choices=HOUSE_TYPE, max_length=100, default="Townhomes")
    interiorimage1 = models.ImageField(upload_to = 'images')
    interiorimage2 = models.ImageField(upload_to = 'images')
    exteriorimage = models.ImageField(upload_to = 'images')
    description = models.CharField(max_length=7000, default="No description")

    class Meta:
        db_table = 'Houses'

    def __str__(self):
        return self.location


class Availability(models.Model):
    useremails = models.CharField(max_length=100)
    telephoneno = models.CharField(max_length=100)
    availabilitymessage = models.CharField(max_length=990)

    class Meta:
        db_table = 'Availability'

    def __str__(self):
        return self.useremails