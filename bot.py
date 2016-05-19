import pprint
import time
import sys
import telepot

TOKEN = sys.argv[1]

def handle(msg):
	pprint.pprint(msg)
	if 'салам' in  msg['text'].lower():
		bot.sendMessage("@caucasus_it", "Ва алейкум ассалам брат, как ты? Как семья?")

	if '/rules' in msg['text'].lower():
		bot.sendMessage("@caucasus_it", "Наши правила: не материться, говорить на общепонятном языке, уважать друг друга, уважать бота.")

	if '/sources' in msg['text'].lower():
		bot.sendMessage("@caucasus_it", "Полезные источники: http://stackoverflow.com, http://tutorialspoint.com ...")

	if '/books' in msg['text'].lower():
		pass

bot = telepot.Bot(TOKEN)
#bot.sendMessage("@caucasus_it", "I want to be an admin =(((")
bot.message_loop(handle)
print("Listening...")

while 1:
	time.sleep(10)
