#curl -o image.jpeg https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQ_Kevbk21QBRy-PgB4kQpS79brbmmEG7m3VOTShAn4PecDU5H5UxrJxE3Dw1JiaG17V88QIol19-3TM2wCHw

import google.generativeai as genai
from PIL import Image, PngImagePlugin

# https://aistudio.google.com/app/apikey
import env 

def gemini_vision(user_img):
    genai.configure(api_key=env.GOOGLE_API_KEY)

    # path='/home/jinx/Documentos/projects/gemini/image.jpg'
    with Image.frombytes('RGB', (3, 2), user_img) as img:
    # img.show()
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(img)
    #print(response.text)

        response = model.generate_content(
        [
        "Write a short, engaging blog post based on this picture.",
        img
        ],
        stream=True
        )
        response.resolve()
        ai_response = response.text
        return ai_response