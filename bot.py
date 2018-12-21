import requests
import telebot
import time
import urllib
VK = 'https://api.vk.com/method/wall.get?v=5.92&domain=spb_today&fields=all&offset=2&count=1&filter=owner&access_token='
post_id = open('post_id.txt', 'r') #Последний пост
global id_last_post
id_last_post = post_id.read()
bot = telebot.TeleBot('')
CHANNEL_NAME = '@'


def main():
    try:
        feed = requests.get(VK)
        json_data = feed.json()
        global id_last
        id_last = json_data['response']['items'][0]['id'] #id
        print(id_last)
        global text
        text = json_data['response']['items'][0]['text'] #text
        global url_photo
        url_photo = json_data['response']['items'][0]['attachments'][0]['photo']['sizes'][4]['url']#photo_url
        print(url_photo)
        if str(id_last) > str(id_last_post):
            ph = open('out.jpg', 'wb')
            ph.write(urllib.request.urlopen(url_photo).read())
            ph.close()
            img = open('out.jpg', 'rb')
            bot.send_chat_action(CHANNEL_NAME, 'upload_photo')
            bot.send_photo(CHANNEL_NAME, img)
            img.close()
            bot.send_message(CHANNEL_NAME, text)
            post_id = open('post_id.txt', 'w')
            post_id.write(str(id_last))
            post_id.close()
            time.sleep(30)
            main()


        else:
            print("Нет новых постов")
            time.sleep(60*4)
            main()


    except:
        main()



if __name__ == '__main__':
    main()


