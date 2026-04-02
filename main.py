import os
import glob
import argparse
from downloader_info import baixar_do_drive, extrair_zip
from processor import processar_e_baixar_imagens

def main():
    # Configuração do Argparse
    parser = argparse.ArgumentParser(description="Pipeline de download e processamento de dataset.")
    
    # Flags de ação
    parser.add_argument("--download", action="store_true", help="Baixa o ZIP do Google Drive e extrai.")
    parser.add_argument("--process", action="store_true", help="Processa os arquivos JSON e baixa as imagens.")
    parser.add_argument("--full", action="store_true", help="Executa o pipeline completo (Download + Processamento).")

    # Parâmetros customizáveis
    parser.add_argument("--apikey", type=str, help="API Key do Elsevier.")
    parser.add_argument("--id", type=str, help="ID do arquivo no Google Drive (opcional se já definido no script).")
    parser.add_argument("--dest", type=str, default="data/imgs/", help="Pasta de destino das imagens.")

    args = parser.parse_args()

    # --- CONFIGURAÇÕES PADRÃO ---
    ID_DRIVE_ZIP = args.id if args.id else "https://drive.google.com/file/d/1Vc7NqE7vQg9qcTwe7RV_qJ6mBm1G0YVb/view?usp=sharing"
    CAMINHO_ZIP = "data/dataset.zip"
    PASTA_EXTRACAO = "data/info/"
    PASTA_IMAGENS = args.dest

    # Lógica de Execução
    executar_download = args.download or args.full
    executar_processamento = args.process or args.full

    if not executar_download and not executar_processamento:
        parser.print_help()
        return

    # 1. ETAPA DE DOWNLOAD E EXTRAÇÃO
    if executar_download:
        print("=== Iniciando Etapa de Download ===")
        baixar_do_drive(ID_DRIVE_ZIP, CAMINHO_ZIP)
        extrair_zip(CAMINHO_ZIP, PASTA_EXTRACAO)
        
        if os.path.exists(CAMINHO_ZIP):
            os.remove(CAMINHO_ZIP)
            print(f"Arquivo {CAMINHO_ZIP} removido.")

    # 2. ETAPA DE PROCESSAMENTO
    if executar_processamento:
        print("=== Iniciando Etapa de Processamento ===")
        
        # O padrão "**/*.json" com recursive=True busca em todas as subpastas
        # (train, test e val) de uma só vez.
        padrao_busca = os.path.join(PASTA_EXTRACAO, "**", "*.json")
        arquivos_json = glob.glob(padrao_busca, recursive=True)
        
        if not arquivos_json:
            print(f"Erro: Nenhum JSON encontrado em {PASTA_EXTRACAO}.")
            return

        print(f"Foram encontrados {len(arquivos_json)} arquivos JSON.")

        for caminho_json in arquivos_json:
            # Opcional: extrair o nome da partição (train/test/val) para organizar as imagens
            particao = os.path.basename(os.path.dirname(caminho_json))
            destino_especifico = os.path.join(PASTA_IMAGENS, particao)
            
            print(f"Processando [{particao}]: {os.path.basename(caminho_json)}")
            processar_e_baixar_imagens(caminho_json, destino_especifico, args.apikey)

    print("\nTarefa concluída!")

if __name__ == "__main__":
    main()