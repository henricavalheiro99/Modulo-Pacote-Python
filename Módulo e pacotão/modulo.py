#Primeira forma
#import math
#raiz = math . sqrt(10)
#print(raiz)


#Segunda forma
#from math import sqrt
#raiz = sqrt(3249)
#print(raiz)

#import Uteis
#gato = Uteis.desenhar_gato()
#print(gato)

#from Uteis import *
#* importa tudo
#pizza = emoji_pizza()
#print(pizza)

#from Pacotão import OpMat
#raiz = OpMat.raiz_quadrada(3249)
#print(raiz)

#from Pacotão.OpMat import *
#raiz = raiz_quadrada(3249)
#print(raiz)

#from Pacotão.Emoji import *
#from Pacotão.Desenho import *
#from Pacotão.Data import *
#from Pacotão.OpMat import *
#from Pacotão.String import *
#teste = emoji_surpreso()
#print(teste)

#from googletrans import Translator
#tradutor = Translator()
#texto = str(input("Digite o texto: "))
#ingles = tradutor.translate(texto, dest="en")
#print("Texto em inglês: " + ingles.text)


import cv2
camera = cv2.VideoCapture(0)
while True:
    ret,frame = camera.read()
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()