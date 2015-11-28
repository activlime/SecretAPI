from datetime import timezone, datetime

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from tokenapi.decorators import token_required
from tokenapi.http import JsonResponse, JsonError
from .utility import utility
from secrets.forms import UserForm
from .models import Secret
from django.views.decorators.http import require_http_methods
from . import strings
from django.template.context_processors import csrf

# Create your views here.
@csrf_protect
@token_required
def secrets(request):
    if request.method == strings.POST:
        user_id = request.POST['user']
        if (utility.username_present(user_id)):
            JsonError("incorrect user_id")
        description = request.POST['description']
        s = Secret(description=description, author_id=user_id)
        s.save()
        return JsonResponse("Your secrets are safe with us")
    elif request.method == strings.GET:
        queryset = Secret.objects.all()
        return HttpResponse(serializers.serialize(strings.JSON, queryset=queryset))

    else:
        return JsonResponse("only can have post and get requests")

@token_required
def detail(request, secret_id):
    queryset = get_object_or_404(Secret, pk=secret_id)
    return HttpResponse(serializers.serialize(strings.json, queryset=queryset))

def accounts(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)

            return JsonResponse(new_user.id)
        else:
            return render(request, 'adduser.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'adduser.html', {'form': form})







