from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Secret(models.Model):
    description = models.CharField(max_length=200)
    author_id = models.IntegerField()
    pub_date = models.DateTimeField(auto_now=True)