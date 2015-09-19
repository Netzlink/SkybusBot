from django.shortcuts import render
from django.http import HttpResponse
import json
import telegram
from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    # return render(request, 'index.html')
    return HttpResponse('Hallo')


def telegram_callback(request):
    if request.method == 'POST':
        update = telegram.Update(**json.loads(request.body))
        print(request.body)
        _parse_update(update)
        return HttpResponse('OK')


def _parse_update(update):
    print(update)
    date = telegram.Message._fromtimestamp(update.message['date'])
    message = telegram.Message(chat=update.message['chat'],
                               message_id=update.message['message_id'],
                               from_user=update.message['from'],
                               date=date,
                               text=update.message['text'])
    print(message)
    print("Hallo %s!" % message.from_user['username'])
    print("Dein command war: %s" % message.text)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

