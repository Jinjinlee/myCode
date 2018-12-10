from django.db import models

class jobs(models.Model):
    image = model.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
