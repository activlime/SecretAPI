from django.contrib import admin

# Register your models here.
from secrets.models import Secret

admin.site.register(Secret)