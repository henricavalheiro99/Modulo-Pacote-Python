import random

num = random.randrange(1, 100)

tentativas = 8

while tentativas > 0:
    pergunta = int(input("Adivinhe o número: "))
    if pergunta == num:
        print("Parabéns acertou")
        break
    elif pergunta > num:
        print("O número é menor")
    elif pergunta < num:
        print("O número é maior")
    else:
        print("número inválido")
    tentativas -= 1
    print(f"tentativas restantes: {tentativas}")
    if tentativas == 0:
        print(f"Você perdeu, o número era {num}")
