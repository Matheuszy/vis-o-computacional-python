Parceiro de Programacao
Entendido! Você quer um arquivo README.md para o seu projeto de controle do mouse com a mão. Um README é essencial para qualquer projeto, pois explica o que ele faz, como rodar, e para que serve.

Vamos criar um README.md que seja claro e informativo para o seu código.

Controle de Cursor com Gesto de Mão (Python)
🚀 Visão Geral do Projeto
Este projeto em Python utiliza a biblioteca MediaPipe para detectar e rastrear os marcos (landmarks) de uma mão em tempo real a partir de uma webcam. As coordenadas da ponta do dedo indicador são usadas para controlar diretamente o cursor do mouse do sistema operacional, graças à biblioteca PyAutoGUI.

É uma demonstração prática de interação humano-computador, transformando o movimento da sua mão em um controle de mouse.

✨ Funcionalidades
Detecção de Mãos em Tempo Real: Utiliza o modelo hand_landmarker do MediaPipe para identificar mãos e seus 21 landmarks.
Controle do Cursor do Mouse: Move o cursor do mouse do sistema operacional com base na posição da ponta do dedo indicador (landmark 8) da primeira mão detectada.
Visualização: Exibe o feed da câmera com as marcações da mão e as conexões entre os landmarks.
Integração pyautogui: Permite o controle programático do mouse.
🛠️ Tecnologias Utilizadas
Python 3.x
OpenCV (cv2): Para captura de vídeo e exibição do feed da câmera.
MediaPipe (mediapipe): Para detecção e rastreamento de mãos.
PyAutoGUI (pyautogui): Para automação do controle do mouse.
📦 Como Instalar e Rodar
Siga estes passos para configurar e executar o projeto em sua máquina:

1. Pré-requisitos
Certifique-se de ter o Python 3.x instalado.

2. Instalação das Dependências
Abra seu terminal ou prompt de comando e execute os seguintes comandos para instalar as bibliotecas necessárias:

Bash

pip install opencv-python mediapipe pyautogui
3. Modelo do MediaPipe
Este projeto requer o arquivo de modelo hand_landmarker.task. Você precisa baixá-lo e colocá-lo na pasta ./modelo dentro do seu projeto.

Crie a pasta:

Bash

mkdir modelo
Baixe o modelo: Acesse este link e baixe o arquivo hand_landmarker.task:
https://developers.google.com/mediapipe/solutions/vision/hand_landmarker#model_card

Mova o arquivo: Coloque o arquivo hand_landmarker.task dentro da pasta modelo que você acabou de criar.

Sua estrutura de pastas deve ficar assim:

seu_projeto/
├── main.py
└── modelo/
    └── hand_landmarker.task
4. Executando o Projeto
Após instalar as dependências e baixar o modelo, você pode rodar o script principal:

Bash

python main.py
⚠️ Observações de Segurança (PyAutoGUI)
O parâmetro pyautogui.FAILSAFE = False foi definido no código. Isso desativa o recurso de segurança do PyAutoGUI que pararia o programa se o mouse fosse movido rapidamente para um canto da tela.
Atenção: Com o FAILSAFE desativado, se o controle do mouse ficar errático ou descontrolado, a forma mais rápida de parar o script é usar o atalho de teclado de emergência do seu sistema operacional:
Windows: Ctrl + Alt + Del e use o Gerenciador de Tarefas para encerrar o processo Python.
macOS: Cmd + Option + Esc para forçar o encerramento do aplicativo do terminal ou IDE.
🤝 Contribuição
Sinta-se à vontade para explorar, modificar e aprimorar este projeto. Sugestões e pull requests são sempre bem-vindos!

