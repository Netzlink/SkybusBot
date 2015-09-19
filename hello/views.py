from django.shortcuts import render
from django.http import HttpResponse
import json
import telegram
import datetime
from .models import Greeting


bot = telegram.Bot(token='131813402:AAFrMB1-B7wZisSSavAwKSOIKVN3w6VcRMA')

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
    # bot.sendMessage(chat_id=message.chat['id'], text=message.text)
    parse_command(message)


def parse_command(message):
    raum = 'test'
    temperature = '12 C'
    command = message.text.split()
    if(command[0]=='/reg'):
        bot.sendMessage(chat_id=message.chat['id'], text=" %s wurde mit %s verbunden" % (command[1], message.from_user['username']))
    if(message.text=='/hallo'):
        bot.sendMessage(chat_id=message.chat['id'], text="hallo %s!" % message.from_user['username'])
    if(message.text=='/temperature'or message.text=='/Temperature'):
        bot.sendMessage(chat_id=message.chat['id'], text="Temperature im Raum %s ist: %s" % ('test', temperature))
    if(message.text=='/whereami'):
        bot.sendMessage(chat_id=message.chat['id'], text="Du bist im Raum %s" % raum)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

