import requests
import os.path
from PIL import Image

def get_image():
    # Retrieving the resource located at the URL
    # and storing it in the file name image.png
    img_url = "https://www.98fmcuritiba.com.br/wp-content/uploads/2024/03/08132532/dragon-bol.jpg"
    r = requests.get(url=img_url)
    img_file = Image.open(r.content)
    img_file.save('/rbeze/Desktop/gemini/img/dragonball.jpg', 'JPEG')

    #img_file = open('image.png', 'wb').write(r.content)
    
    return img_file