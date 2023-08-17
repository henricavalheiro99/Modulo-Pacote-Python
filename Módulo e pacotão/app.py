from Exercicios.Geometria.formas import *

escolha = int(input("Qual área você quer calcular? \n 1-Quadrado \n 2-Círculo \n"))
area = 0


if escolha == 1:
    lado = float(input("Digite o valor do lado: "))
    area = areaQuadrado(lado)
    print(area)

elif escolha == 2:
    raio = float(input("Digite o valor do raio: "))
    area = areaCirculo(raio)
    print(area)

else:
    area = "valor inválido"
    print(area)
