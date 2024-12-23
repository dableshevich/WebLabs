from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='Unknown')
    score = models.DecimalField(max_digits=2, decimal_places=1, default=1.0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)