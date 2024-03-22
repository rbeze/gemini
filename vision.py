#curl -o image.jpeg https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQ_Kevbk21QBRy-PgB4kQpS79brbmmEG7m3VOTShAn4PecDU5H5UxrJxE3Dw1JiaG17V88QIol19-3TM2wCHw

import google.generativeai as genai
import img_download, img_path
from PIL import Image
from img_download import ImageProcessing

# https://aistudio.google.com/app/apikey
import env 

class Gemini():
    def __init__(self, user_msg):
        self.user_msg = user_msg
        genai.configure(api_key=env.GOOGLE_API_KEY)
    
    def nlp(self):

        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)
        
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(self.user_msg)

        return response.text

    def vision(self):
        img_url = self.user_msg
        img_proc = ImageProcessing(img_url)
        img_name = img_proc.download_img()

        img_path = f'{img_path.path}/{img_name}'
        img = Image.open(img_path)
        # img.show()

        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(img)
        img_proc.delete_image(img_path)

        return response.text