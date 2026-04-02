import json
import requests
from urllib.parse import urlparse
import os, shutil


def save_image_from_url(url_image: str, path_save:str) -> None:
    r = requests.get(url_image, stream=True)
    if r.status_code == 200:
        with open(path_save, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f) 

def save_image(url_image, apikey, path_save) -> None:
    a = urlparse(url_image)
    url_request = a.scheme + "://" + a.netloc + a.path + "?apikey=" + apikey
    save_image_from_url(url_image=url_request, path_save=path_save)

def processar_e_baixar_imagens(caminho_json, pasta_destino, apikey):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    with open(caminho_json, 'r') as f:
        data = json.load(f)
        
    try:
        save_image(data['image']['url'], apikey, os.path.join(pasta_destino, os.path.basename(caminho_json)[:-5]+".jpg"))
    except:
        pass