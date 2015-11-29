from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse

from secrets import strings


class utility:
    def authenticate(self, username, password):
        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                print("User is valid, active and authenticated")
                return True
            else:
                print("The password is valid, but the account has been disabled!")
                return False
                re
        else:
            # the authentication system was unable to verify the username and password
            print("The username and password were incorrect.")
            return False

    def username_present(self, user_id):
        if User.objects.filter(pk=user_id).exists():
            return True

        return False

    def returnJsonQuery(self, queryset):
        return HttpResponse(serializers.serialize(strings.JSON, queryset=queryset))