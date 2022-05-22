from django.db import models

# Create your models here.
class Contactus(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    emailadress = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    messages = models.CharField(max_length=2000)

    class Meta:
        db_table = 'Contactus'

    def __str__(self):
        return self.lastname