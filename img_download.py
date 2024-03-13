import requests

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
download_image(url, nome_arquivo)