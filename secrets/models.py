from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Secret(models.Model):
    description = models.CharField(max_length=200)
    author = models.ForeignKey(User, unique=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.description