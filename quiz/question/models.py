from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.CharField(max_length=256)
    option_a = models.CharField(max_length=32)
    option_b = models.CharField(max_length=32)
    option_c = models.CharField(max_length=32)
    option_d = models.CharField(max_length=32)
    answer  = models.CharField(max_length=32)
