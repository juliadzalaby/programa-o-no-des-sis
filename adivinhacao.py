print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)
chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    if(chute > numero_secreto):
       print("Você errou! O seu numero foi maior que o numero secreto")
    elif(chute < numero_secreto):
       print("Você errou! O seu numero foi menor que o numero secreto")

print("Fim do jogo")
