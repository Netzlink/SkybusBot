from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    # return render(request, 'index.html')
    return HttpResponse('Hallo')


def telegram_callback(request):
    if request.method == 'POST':
        print(request.body)
        return HttpResponse('OK')
    if request.method == 'GET':
        return HttpResponse('GET')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

