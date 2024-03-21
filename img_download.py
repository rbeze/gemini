import requests
import os
import img_path

class Image:
    def __init__(self, img_url):
        self.img_url = img_url
        ext = url.split(".")[-1]
        img_db = os.listdir(img_path.path)

        if len(img_db) != 0:
            for image in img_db:
                self.delete_image(image)

        self.img_name = f"img_0.{ext}"
    
    def delete_image(self, filename):
        try:
            os.remove(filename)
            print(f"Image {filename} deletada com sucesso!")
        except FileNotFoundError:
            print(f"Imagem {filename} não encontrada.")
        except Exception as e:
            print(f"Ocorreu um erro ao deletar a imagem: {e}")

    def download_image(self):
        response = requests.get(self.img_url)

        if response.status_code == 200:
            with open(f"{img_path.path}/{self.img_name}", 'wb') as f:
                f.write(response.content)
            print("Download concluído: ", filename)
        else:
            print("Falha ao fazer o download: ", response.status_code)
        return self.img_name

# Exemplo de uso:
url = "https://t.ctcdn.com.br/lvns56iaSMyHvyTur4JeYS_NYeY=/i606944.png"
db_path = img_path.path_list
nome_arquivo = "imagem.jpg"
#download_image(url, nome_arquivo)
image_download = Image(url, db_path)