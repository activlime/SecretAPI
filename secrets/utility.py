import json
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse

from tokenapi.http import JsonResponse, JsonError

from secrets import strings


def authenticate(username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            print("User is valid, active and authenticated")
            return True
        else:
            print("The password is valid, but the account has been disabled!")
            return False
    else:
        # the authentication system was unable to verify the username and password
        print("The username and password were incorrect.")
        return False

def username_present(user_id):
    if User.objects.filter(pk=user_id).exists():
        return True

    return False

def returnJsonQuery(queryset):
    return HttpResponse(serializers.serialize(strings.JSON, queryset=queryset))

def createJsonFromObject(ob):
    return json.dumps(vars(ob))

class Secret:
    def __init__(self, id, description, pub_date):
        self.id = id
        self.description = description
        self.pub_date = pub_date

    def __str__(self):
        return "secret" + self.id

