import pickle

#declaração das variaveis
usuario = 0 
menu1 = 0 
menu2 = 0 
menu3 = 0 
nomeC = "Jobnelson Clovisdeison"
saldoC = 500.00 
rend = 0 
senha = 0
logado = 0

while True:

    print("Bem vindo ao Sistema Bancário\n 1. Acessar como Cliente\n 2. Acessar como Gerente\n 3. Encerrar programa")  
    menu1 = int(input("Escolha uma opção:"))

    if menu1 < 1 or menu1 > 3: #verifica se foi colocado a opção citada.
        continue

    if menu1 == 3: #encerra o programa
        break
    #if menu1 == 1:
        #area de criação do cliente
    if menu1 == 2:
        for x in range(0, 3):
            senha = input("Digite a senha:")
            if senha == "banco":
                print("Continuação do código de gerente")
                logado = True
                break
            else:
                print("Senha incorreta.")
        print(x)
        if x == 2:
            print("Senha incorreta digitada varias vezes, fim do programa!")
            break