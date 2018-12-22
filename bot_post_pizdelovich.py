#!/usr/bin/env python
import requests
import telebot
import time
import urllib

bot = telebot.TeleBot('')
CHANNEL_NAME = '@' # Канал
PABLIK_PIZDIM = '' # Паблик, откуда пиздим
VK_ACCESS_TOKEN = ''
POST_KOL = '100' # Колличество спизженных постов от 0 и до ..
def id():
    global id_last
    id_last = json_data['response']['items'][0]['id']  # id
    print(id_last)
    # global text
    try:
        global text
        text = json_data['response']['items'][0]['text']  # text
        print(text)
        send()
    except:
        send()

def send():
    #post_id = 1 ####### -ID- ###########
    print("SEND DEF")
    #print(id_last + ">"+post_id+"?")
    try:
        send_text()
    except:
        print("След пост")
    #else:
     #   print("В ###-ID-### ЗАЛУПА")
def send_photo():
    print("send_photo def")
    ph = open('out.jpg', 'wb')
    ph.write(urllib.request.urlopen(url_photo).read())
    ph.close()
    img = open('out.jpg', 'rb')
    print("SEND_PHOTO Пытаюсь отправить фото")
    bot.send_chat_action(CHANNEL_NAME, 'upload_photo')
    bot.send_photo(CHANNEL_NAME, img)
    img.close()
    img = open('out.jpg', 'w')
    img.close()
    post_id = open('post_id.txt', 'w')
    post_id.write(str(id_last))
    post_id.close()

def send_text():
    print("SEND_TEXT Пытаюсь отправить text")
    bot.send_message(CHANNEL_NAME, text)
    post_id = open('post_id.txt', 'w')
    post_id.write(str(id_last))
    post_id.close()
    time.sleep(30)




def photo():
   try:
       for cou in range(0, 20):
            global url_photo
            #url_photo = json_data['response']['items'][0]['attachments'][0]['photo']['sizes'][4]['url']#photo_url
            url_photo = json_data['response']['items'][0]['attachments'][cou]['photo']['sizes'][4]['url']
            print(url_photo)
            send_photo()

   except:
       id()

def request():
    try:
        feed = requests.get(VK)
        global json_data
        json_data = feed.json()
        try:
            json_data['response']['items'][0]['is_pinned']
            print("Закреп пропускаем")
        except:
            photo()

    except:
        time.sleep(60)
        request()

for i in range(0,int(POST_KOL)):
    #time.sleep(40)
    ZNACH = str(i)
    print(ZNACH)
    VK = str('https://api.vk.com/method/wall.get?v=5.92&domain=')+ str(PABLIK_PIZDIM)+('&fields=all&offset=') + str(ZNACH) + str('&count=1&filter=owner&access_token=')+str(VK_ACCESS_TOKEN)
    request()
