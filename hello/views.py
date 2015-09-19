from django.shortcuts import render
from django.http import HttpResponse
from telegram import Update
import json
from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    # return render(request, 'index.html')
    return HttpResponse('Hallo')


def telegram_callback(request):
    if request.method == 'POST':
        update = Update(**json.loads(request.body))
        _parse_update(update)
        return HttpResponse('OK')


def _parse_update(update):
    print(update)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

