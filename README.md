# ElsCap
We created the ElsCap dataset, meticulously compiled from a vast collection of open-access scientific articles on the ScienceDirect platform, a comprehensive repository of peer-reviewed academic literature managed by Elsevier.

meu_projeto_dataset/
│
├── data/                  # Pasta onde as imagens serão salvas
|  ├── imgs/               # Pasta para as imagens
|  ├── info/               # Pasta para os arquivos JSON baixados
│
├── main.py                # Ponto de entrada (orquestra o processo)
├── downloader_info.py          # Lógica para baixar do Google Drive
├── processor.py           # Lógica para ler os JSONs e extrair URLs das imagens e baixar
│
├── requirements.txt       # Bibliotecas necessárias (gdown, requests)
└── README.md              # Documentação do projeto
