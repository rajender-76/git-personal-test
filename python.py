
from django.db import models

class students(models.Models):
    name = models.CharField(max_length = 200)
    age = models.CharField()
    section = models.CharField()
