import telebot
import time
import paho.mqtt.client as mqtt

bot = telebot.TeleBot('1309028910:AAFB3yozhS8dEHz_gQvd0U4VLPSpjEqbghw')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('информация')
keyboard1.row('включить','выключить')
def on_connectt(client,userdata,flags,rc):
	print('Connected with code'+str(rc))
	    #Sub
	client.subscribe("Relay/#")
    client.subscribe("Informing/#")
def on_messagee(client,userdata,msg):
	print( str(msg.payload) )
	print('ok')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!\n Ты попал в интерфейс управления системой освещения! Для продолжения введите ваше имя и через пробел пароль')
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'Сергей 12345678':
        bot.send_message(message.from_user.id, "Доступ к системе управления разрешен! Добро пожаловать!",reply_markup=keyboard1);
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
        bot.send_message(message.from_user.id, str(msg.payload))
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
@bot.message_handler(content_types=['text'])
def text_analyze(message):
    if "включить" in message.text.lower():
        client=mqtt.Client()
        run=1
        client.on_connect=on_connectt
        client.on_message=on_messagee
        client.connect("m16.cloudmqtt.com",11729,60)
        client.username_pw_set("tizzoqtl", "sqCYE8vpFV1P")
        client.loop_start()
        while run<3:
            client.publish("Relay/",'1')
            time.sleep(1.2)
            run+=1
            print(run)
        client.loop_stop()
        client.disconnect()
    elif 'выключить' in message.text.lower():
        client=mqtt.Client()
        run=1
        client.on_connect=on_connectt
        client.on_message=on_messagee
        client.connect("m16.cloudmqtt.com",11729,60)
        client.username_pw_set("tizzoqtl", "sqCYE8vpFV1P")
        client.loop_start()
        while run<3:
            client.publish("Relay/",'0')
            time.sleep(1.2)
            run+=1
            print(run)
        client.loop_stop()
        client.disconnect()
    elif 'информация' in message.text.lower():
        client=mqtt.Client()
        run=1
        client.on_connect=on_connectt
        client.on_message=on_messagee
        client.connect("m16.cloudmqtt.com",11729,60)
        client.username_pw_set("tizzoqtl", "sqCYE8vpFV1P")
        client.loop_start()
        while run<3:
            client.publish("Informing/",'1')
            time.sleep(1.2)
            run+=1
            print(run)
        client.loop_stop()
        client.disconnect()
bot.polling()
