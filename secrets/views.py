import json
from datetime import timezone, datetime

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework.decorators import api_view
from tokenapi.decorators import token_required
from tokenapi.http import JsonResponse, JsonError
from . import utility
from secrets.forms import UserForm
from .models import Secret
from django.views.decorators.http import require_http_methods
from . import strings
from django.template.context_processors import csrf

# Create your views here.
@csrf_exempt
@token_required
def secrets(request):
    user_id = request.GET['user']
    user = get_object_or_404(User, pk=user_id)

    if request.method == strings.POST:
        description = request.POST['description']
        user.secret_set.create(description=description)
        return JsonResponse({})

    elif request.method == strings.GET:
        secrets = Secret.objects.filter(user__id=user.id)

        listofsecrets = []
        dictofsecrets = {}

        for secret in secrets:
           listofsecrets.append(utility.Secret(secret.id, secret.description, str(secret.pub_date)).__dict__)

        dictofsecrets["secrets"] = listofsecrets

        return JsonResponse(dictofsecrets)
    else:
        return JsonError("only can have post and get requests")

@csrf_exempt
def detail(request, secret_id):
    try:
        user_id = request.GET['user']
    except:
        JsonError("key error")

    try:
        user = get_object_or_404(User, pk=user_id)
    except ObjectDoesNotExist:
        JsonError("User " + user_id + "does not exist")

    if request.method == strings.POST:
        description = request.POST['description']

        try:
            selected_secret = user.secret_set.get(pk=secret_id)
        except (ObjectDoesNotExist):
            return JsonError("Secret id " + secret_id + " does not exist")

        selected_secret.description = description
        selected_secret.save()

        return JsonResponse({})

    elif request.method == strings.GET:
        try:
            selected_choice = user.secret_set.get(pk=secret_id)
        except (ObjectDoesNotExist):
            return JsonError("Secret id " + secret_id + " does not exist")

        secret = utility.Secret(selected_choice.id, selected_choice.description, str(selected_choice.pub_date)).__dict__

        return JsonResponse(secret)

    elif request.method == strings.DELETE:
        try:
            selected_secret = user.secret_set.get(pk=secret_id)
        except (ObjectDoesNotExist):
            return JsonError("Secret id " + secret_id + " does not exist")

        selected_secret.delete()
        return JsonResponse({})

    else:
        return JsonError("Only can post, put, get, delete")


def accounts(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            dict = userdict(new_user.id)
            return JsonResponse(dict)
        else:

            return render(request, 'adduser.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'adduser.html', {'form': form})

def userdict(new_user_id):
    dict = {}
    dict[strings.USER] = new_user_id
    return dict









