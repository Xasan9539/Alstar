from django.db import models

# Create your models here.
class Alstar(models.Model):
    full_name = models.CharField(max_length=70)
    specialty = models.CharField(max_length=55)
    avatar = models.ImageField(upload_to='alstar/')
