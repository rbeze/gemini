# import sys
import time
import telepot
import env
from vision import Gemini
from telepot.loop import MessageLoop

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        if "https" in msg['text']:
            ai_msg = Gemini(msg['text']).vision()
            bot.sendMessage(chat_id, ai_msg)
        else:
            ai_msg = Gemini(msg['text']).nlp()
            bot.sendMessage(chat_id, ai_msg)

#TOKEN = sys.argv[1]  # get token from command-line
TOKEN = env.TELEGRAM

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)