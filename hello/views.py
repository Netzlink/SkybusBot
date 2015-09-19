from django.shortcuts import render
from django.http import HttpResponse
import json
import telegram
import datetime
from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    # return render(request, 'index.html')
    return HttpResponse('Hallo')


def telegram_callback(request):
    if request.method == 'POST':
        print(request.body)
        update = telegram.Update.de_json(request.body)
        _parse_update(update)
        return HttpResponse('OK')


def _parse_update(update):
    print(update)
    message = telegram.Message(chat=update.message['chat'],
                               message_id=update.message['message_id'],
                               from_user=update.message['from'],
                               date=datetime.time())
    print(message)
    print("Hallo %s" % message.from_user)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

