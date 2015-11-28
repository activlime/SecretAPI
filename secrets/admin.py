from django.contrib import admin

# Register your models here.
from secrets.models import Secret


class SecretAdmin(admin.ModelAdmin):
    list_display = ['description', 'author_id', 'pub_date']
    list_filter = ['author_id']

admin.site.register(Secret, SecretAdmin)


