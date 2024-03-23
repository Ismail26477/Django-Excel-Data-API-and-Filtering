from django.db import models

# Create Model as per your Excel columns
class ExcelData(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

