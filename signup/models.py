from django.db import models

# Create your models here.
class Registration(models.Model):
    useremail = models.EmailField(max_length=200)
    password = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(delfault= True)

    class Meta:
        db_table = 'Registration'

    def __str__(self):
        return self.useremail