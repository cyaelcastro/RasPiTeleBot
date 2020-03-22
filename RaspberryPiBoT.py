from tokenfile import token
import telebot
import os


SSID = os.popen("iwgetid")
IP = os.popen("hostname -I")

bot = telebot.TeleBot(str(token))

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
	bot.reply_to(message, "Hello, I'm RaspberryPiBot, for now, only i can help you getting the IP and SSID with /ip and /SSID")

@bot.message_handler(commands=["SSID", "ssid"])
def send_welcome(message):
        bot.reply_to(message, "SSID: "+ SSID.read())

@bot.message_handler(commands=["IP","ip","Ip"])
def send_welcome(message):
        bot.reply_to(message, "IP: "+ IP.read())


bot.polling()
