from Exercicios.Ex1 import *

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um outro número: "))
operacao = int(input("Digite a operacao escolhida \n 1-Soma \n 2-Subtração \n 3-Multiplicação \n 4-Divisão \n"))

resultado = 0

if operacao == 1:
    resultado = adicao(n1, n2)
elif operacao == 2:
    resultado = subtracao(n1, n2)
elif operacao == 3:
    resultado = multiplicacao(n1, n2)
elif operacao == 4:
    resultado = divisao(n1, n2)
else:
    resultado = "operação inválida"

print(resultado)