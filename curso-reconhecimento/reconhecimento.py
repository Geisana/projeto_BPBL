#instalar o openCV
#ler a imagem e depois reconhecer os caracteres
import cv2
import pytesseract
import numpy as np


#lendo imagem
img = cv2.imread(r"C:\Users\frgei\Projetos\projeto_BPBL\ACERVO\imagem_aproximada.png")
#apontar caminho do tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

cv2.imshow('Imagem',img) #BGR
cv2.waitKey(0)
cv2.destroyAllWindows()

rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('Imagem',rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

texto = pytesseract.image_to_string(rgb)
print(texto)
#cd "C:\Program Files\Tesseract-OCR"
#tesseract --list-langs

texto = pytesseract.image_to_string(rgb, lang='por')
print(texto)
l,