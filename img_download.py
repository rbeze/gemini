import requests
import os

def name_img():
    img_db = os.listdir("/home/rbeze/Desktop/gemini/img")
    print(img_db)
    if len(img_db) == 0:
        img_name = "img_0"
    else:

        img_number = img_db[0].split("_")[1].split(".")[0]
        img_name = f"img_{int(img_number) + 1}" 
        print(img_name)

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print("Download concluído: ", filename)
    else:
        print("Falha ao fazer o download: ", response.status_code)

# Exemplo de uso:
url = "https://t.ctcdn.com.br/lvns56iaSMyHvyTur4JeYS_NYeY=/i606944.png"
nome_arquivo = "imagem.jpg"
#download_image(url, nome_arquivo)
name_img()