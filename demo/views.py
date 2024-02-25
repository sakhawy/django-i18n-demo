from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _


def hello_world(request):
    return HttpResponse(_('Hello, World!'))


def hello_world_template(request):
    return render(request, 'demo/hello_world.html')
