from datetime import datetime
from django.db import models

# Create your models here.
class Form_edonator(models.Model):
    Name = models.CharField(max_length = 122)
    Contact_no =models.CharField(max_length = 12)
    email =models.CharField(max_length = 122)
    address = models.CharField(max_length = 122)
    e_img = models.FileField(upload_to='', storage=None, max_length=100)
    date = models.DateField()
    