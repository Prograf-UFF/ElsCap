import gdown
import os
import zipfile
import shutil


def baixar_do_drive(url, destino):
    """Baixa o arquivo ZIP do Google Drive."""
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    # fuzzy=True ajuda a encontrar o ID mesmo que o link seja de visualização
    output = gdown.download(url, destino, quiet=False, fuzzy=True)
    return output

def extrair_zip(caminho_zip, pasta_destino):
    """Extrai o ZIP e move train/test/val para fora da pasta ElsCap."""
    print(f"Extraindo {caminho_zip}...")
    
    with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
        zip_ref.extractall(pasta_destino)
    
    # Caminho da pasta pai indesejada
    pasta_els_cap = os.path.join(pasta_destino, "ElsCap")

    if os.path.exists(pasta_els_cap):
        # Listamos tudo o que está dentro de ElsCap (train, test, val, etc)
        subpastas = os.listdir(pasta_els_cap)
        
        for nome_subpasta in subpastas:
            caminho_origem = os.path.join(pasta_els_cap, nome_subpasta)
            caminho_final = os.path.join(pasta_destino, nome_subpasta)
            
            # Se for realmente uma pasta, movemos para o nível acima
            if os.path.isdir(caminho_origem):
                # Remove a pasta de destino se ela já existir para evitar erro de colisão
                if os.path.exists(caminho_final):
                    shutil.rmtree(caminho_final)
                
                shutil.move(caminho_origem, caminho_final)
                print(f"Movido: {nome_subpasta} para {pasta_destino}")

        # Após mover tudo, removemos a pasta ElsCap agora vazia
        shutil.rmtree(pasta_els_cap)