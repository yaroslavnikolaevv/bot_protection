import telebot
import time
import paho.mqtt.client as mqtt

bot = telebot.TeleBot('976834670:AAEIr2cuM9pbYwj_yceKmy8-TtBUxRADwNQ')




@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!\n Ты попал в интерфейс охранной системы! Для продолжения введите ваше имя и через пробел пароль')
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'Ярослав 159763':
        bot.send_message(message.from_user.id, "Доступ к системе управления разрешен! Добро пожаловать!");
        bot.register_next_step_handler(message, mq1); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Войдите в систему');
# print("ok")
def mq1(message):
    def on_connect(client,userdata,flags,rc):
        print('Connected with code'+str(rc))
        #Sub
        client.subscribe("Inform/#")
    def on_message(client,userdata,msg):
        # print( str(msg.payload) )
        bot.send_message(message.from_user.id, 'Зафиксировано движение')
    client=mqtt.Client()
    client.on_connect=on_connect
    client.on_message=on_message

    client.connect("m16.cloudmqtt.com",11729,60)
    client.username_pw_set("tizzoqtl", "sqCYE8vpFV1P")

    time.sleep(1)
    client.loop_start()
    while True:
        continue

    client.loop_stop()
    client.disconnect()
bot.polling()
