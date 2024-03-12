import sys
import time
import telepot
import env
from img_downloader import get_image as img
from nlp import gemini_nlp as nlp
from vision import gemini_vision as vision
from telepot.loop import MessageLoop

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        #if "https" in msg['text']:
            # mudar o argumento vision para o caminho da imagem com que foi feito o download utilizando Python
            #bot.sendMessage(chat_id, vision(msg['text']))
        #else:
            image = img()
            bot.sendMessage(chat_id, vision(image))

#TOKEN = sys.argv[1]  # get token from command-line
TOKEN = env.TELEGRAM

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)