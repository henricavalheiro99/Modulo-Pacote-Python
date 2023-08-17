from conversor_unidades.conversor import *

escolha = int(input("Digite qual conversão você quer fazer: \n 1-Celsius \n 2-Fahrenheit \n"))
valor = float(input("Digite o valor da temperatura: "))
if escolha == 1:
    temperatura = Fahrenheit_Celsius(valor)
    print(temperatura)
elif escolha == 2:
    temperatura = Celsius_Fahrenheit(valor)
    print(temperatura)
else:
    print("Número inválido")