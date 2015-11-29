from datetime import timezone, datetime

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from tokenapi.decorators import token_required
from tokenapi.http import JsonResponse, JsonError
from .utility import utility
from secrets.forms import UserForm
from .models import Secret
from django.views.decorators.http import require_http_methods
from . import strings
from django.template.context_processors import csrf

# Create your views here.
@csrf_exempt
def secrets(request):
    if request.method == strings.POST:
        user_id = request.POST['user']
        description = request.POST['description']
        user = get_object_or_404(User, pk=user_id)
        user.secret_set.create(description=description)
        return JsonResponse("Your secrets are safe with us")
    elif request.method == strings.GET:
        user_id = request.GET['user']
        user = get_object_or_404(User, pk=user_id)
        queryset = Secret.objects.filter(user__id=user_id)
        return HttpResponse(serializers.serialize(strings.JSON, queryset=queryset))
    else:
        return JsonResponse("only can have post and get requests")

@token_required
def detail(request, secret_id):
    queryset = get_object_or_404(Secret, pk=secret_id)
    return HttpResponse(serializers.serialize(strings.JSON, queryset=queryset))

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







