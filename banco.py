import pickle
import os

#declaração das variaveis
usuario = 0 
menu2 = 0 
menu3 = 0 
rend = 0 
logado = False
cliente1 = {'nome': "Jobnelson Clovisdeison", 'saldo':  500.0,}
clientenom = "cliente1" + ".pickle"



base_dir = os.path.dirname(__file__) # Pega o caminho do arquivo atual
cliente_dir = os.path.join(base_dir, 'Clientes') # Cria o caminho do diretório teste dentro do diretório atual
os.mkdir(cliente_dir) if not os.path.exists(cliente_dir) else None # Cria o diretório teste se não existir
file_path = os.path.join(cliente_dir, clientenom) # Cria o caminho do arquivo teste dentro do diretório teste

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print("Bem vindo ao Sistema Bancário\n 1. Acessar como Cliente\n 2. Acessar como Gerente\n 3. Encerrar programa")  
    menu1 = int(input("Escolha uma opção:"))

    if menu1 < 1 or menu1 > 3: #verifica se foi colocado a opção citada.
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    if menu1==1:
        menu2=int(input("Menu Cliente:\n 1.Consultar saldo\n 2.Depositar\n 3.Sacar\Pix\n 4.Simular Rendimento\n 5.Voltar ao menu principal"))

        if menu2==1:
            with open(file_path, 'rb') as cliente:
                cliente1['saldo'] = pickle.load(cliente)
                print(cliente1['saldo'])


        input()
        exit()


    
    
    if menu1 == 3: #encerra o programa
        exit()
    #if menu1 == 1:
        #area de criação do cliente
    if menu1 == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        for x in range(0, 3):
            senha = input("Digite a senha:")
            if senha == "banco":
                # Continuação do código de gerente
                logado = True
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Senha incorreta.")
        if x == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Senha incorreta digitada varias vezes, fim do programa!")
            input()
            exit()
        while logado == True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Menu Gerente:\n1. Cadastrar ou Trocar Nome do Cliente\n2. Corrigir Saldo do Cliente\n3. Consultar Status do Cliente\n4. Voltar ao Menu Principal")
            menu2 = int(input("Escolha uma opção:"))
                
            if menu2 < 1 or menu2 > 4:
                continue
                
            if menu2 == 1:
                cliente1['nome'] = input("Digite o novo nome do cliente:")
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Nome do cliente alterado com sucesso!")
                input("Pressione Enter para continuar...")
                with open(file_path, 'wb') as gerente:
                    pickle.dump(cliente1, gerente)

            if menu2 == 2:
                cliente1['saldo'] = float(input("Digite o novo saldo do cliente:"))
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Saldo do cliente alterado com sucesso!")
                input("Pressione Enter para continuar...")
                with open(file_path, 'wb') as gerente:
                    pickle.dump(cliente1, gerente)
                
            if menu2 == 4:
                break
