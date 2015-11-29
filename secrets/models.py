from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import ForeignKey


class Secret(models.Model):
    description = models.CharField(max_length=200)
    user = ForeignKey(User)
    pub_date = models.DateTimeField(auto_now=True)
