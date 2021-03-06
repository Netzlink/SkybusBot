from django.shortcuts import render
from django.http import HttpResponse
import json
import telegram
import datetime
from .models import Greeting

adrian = {'uii':'3000E20020648118011918005ACC', 'telegram': '17138029', 'username': 'AdrainSo'}
cor = {'uii':'3000E20020648118011914807DAC', 'telegram': '103683331', 'username': 'sirmonkey'}

users = [adrian, cor]
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

def update_location(request):
    if request.method == 'POST':
        loaded = json.loads(request.body)
        print(loaded)
        for user in users:
            if user['uii'] == loaded['tag']:
                    if loaded['incoming']:
                        txt = 'Weg Weg! Von %s!' % loaded['location']
                    else:
                        txt = 'Danke! Kommt nie wieder!'
                    bot.sendMessage(chat_id=user['telegram'], text=txt)
        return HttpResponse('OK')

def parse_command(message):
    raum = 'Saal'
    temperature = '19 C'
    command = message.text.split()
    if(command[0]=='/reg'):
        for user in users:
            if user['username'] == message.from_user['username']:
                user['uii'] = command[1]
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

