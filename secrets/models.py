from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey

# Create your models here.

class Secret(models.Model):
    description = models.CharField(max_length=200)
    user = ForeignKey(User)
    pub_date = models.DateTimeField(auto_now=True)
