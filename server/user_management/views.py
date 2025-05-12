# user_management/views.py
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello, Django is working!")
