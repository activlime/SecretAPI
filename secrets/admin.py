from django.contrib import admin

# Register your models here.
from secrets.models import Secret


class SecretAdmin(admin.ModelAdmin):
    list_display = ['description', 'pub_date']

admin.site.register(Secret, SecretAdmin)