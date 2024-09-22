# Detecção de Placas com OpenCV

Este projeto utiliza a biblioteca **OpenCV** para realizar a detecção de placas de veículos em imagens. A técnica aplicada envolve processamento de imagens, como conversão para escala de cinza, suavização, detecção de bordas e operações morfológicas, com o objetivo de isolar e detectar as placas.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada.
- **OpenCV**: Biblioteca de visão computacional para manipulação e processamento de imagens.
- **NumPy**: Biblioteca para suporte a operações matriciais.
- **OS**: Biblioteca padrão para manipulação de arquivos e diretórios.

## Funcionalidades

O script realiza as seguintes etapas:

1. **Leitura da imagem**: As imagens são carregadas a partir de um diretório.
2. **Conversão para escala de cinza**: Facilita a extração de características das imagens.
3. **Suavização**: Filtro Gaussiano para remover ruídos.
4. **Detecção de bordas (Sobel)**: Realiza a detecção de bordas na imagem.
5. **Limiarização**: Cria uma imagem binária com base nas bordas detectadas.
6. **Operações morfológicas**: Fechamento, abertura e dilatação para conectar contornos e refinar os resultados.
7. **Detecção de contornos**: Identifica contornos fechados nas imagens e os filtra com base em seu tamanho e formato.
8. **Extração da placa**: A partir dos contornos, a placa é isolada e salva em um diretório de saída.

## Como Executar

### Pré-requisitos

Certifique-se de ter o Python e as bibliotecas necessárias instaladas:

```bash
pip install opencv-python numpy
```

### Execução

1. Execute o script com o seguinte comando:

```bash
python nome_do_script.py
```
As placas detectadas serão salvas no diretório `output`.
