from django.http import HttpResponse
from django.utils.translation import gettext as _

def hello_world(request):
    return HttpResponse(_('Hello, World!'))
