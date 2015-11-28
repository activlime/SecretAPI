from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from secrets.forms import UserForm
from .models import Secret
from django.views.decorators.http import require_http_methods
from . import strings

# Create your views here.

def ownsecrets(request):
    queryset = Secret.objects.all()
    return HttpResponse(serializers.serialize(strings.JSON, queryset=queryset))

def detail(request, secret_id):
    queryset = get_object_or_404(Secret, pk=secret_id)
    return HttpResponse(serializers.serialize(strings.json, queryset=queryset))

def accounts(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            return HttpResponse("success")
        else:
            return render(request, 'adduser.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'adduser.html', {'form': form})







