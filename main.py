import cv2
import numpy as np
import os

def encontrarPlaca(path, filename, dir):
    img = cv2.imread(os.path.join(path, filename))
    #cv2.imshow('Imagem Original', img)

    #Converte para escala de cinza
    img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('Imagem Cinza', img_cinza)

    #Suavilização com filtro de convolução
    #Remove o ruído e suaviza as bordas da imagem
    img_suavizada = cv2.GaussianBlur(img_cinza, (3, 3), 0)
    #cv2.imshow('Imagem Suavizada GausianBlur(3x3)', img_suavizada)

    #Detecção de borda Sobel, usando derivada apenas no eixo x
    img_sobel = cv2.Sobel(img_suavizada, cv2.CV_8U, 1, 0, ksize=3)
    #cv2.imshow('Imagem Sobel', img_sobel)

    #Limirialização com binaria usando treshold automático
    img_limirializada = cv2.threshold(img_sobel, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    #cv2.imshow('Imagem Limirializada', img_limirializada)

    kernel = np.ones((1, 60), np.uint8)
    #Operação morfológica para fechamento, conectar lacunas
    img_fechamento = cv2.morphologyEx(img_limirializada, cv2.MORPH_CLOSE, kernel)
    #cv2.imshow('Imagem Fechamento', img_fechamento)

    kernel = np.ones((6, 1), np.uint8)
    #Operação morfológica para abertura, reduz pontos e tamanho de objetos
    img_abertura = cv2.morphologyEx(img_fechamento, cv2.MORPH_OPEN, kernel)
    #cv2.imshow('Imagem Abertura', img_abertura)

    kernel = np.ones((5, 5), np.uint8)
    #Operação morfológica para dilatação, aumtnar tamanho
    img_dilatacao = cv2.dilate(img_abertura, kernel, iterations=1)
    #cv2.imshow('Imagem dilatada', img_dilatacao)

    #Encontra contornos fechados
    contornos, _ = cv2.findContours(img_dilatacao, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cont in contornos:
        perimetro = cv2.arcLength(cont, True)
        if perimetro > 450:
            aprox = cv2.approxPolyDP(cont, 0.03 * perimetro, True)
            if len(aprox) == 4:
                (x, y, lar, alt) = cv2.boundingRect(cont)
                cv2.rectangle(img, (x, y), (x + lar, y + alt), (0, 255, 0), 2)
                placa_img = cv2.getRectSubPix(img, (lar + 20, alt + 10), (x + lar//2, y + alt//2))
                cv2.imwrite(dir + filename, placa_img)
                cv2.imshow('placa', placa_img)
                cv2.waitKey(0)

if __name__ == "__main__":
    #Nome do diretótio onde se encontra as imagens
    path = 'imagens_placas'
    dir = 'output/'
    #Pecorre todas as imagens
    for filename in os.listdir(path):
        if filename.endswith('.jpg'):
            encontrarPlaca(path, filename, dir)
