import pickle
import os

#declaração das idclienteiaveis
usuario = 0 
menu2 = 0 
menu3 = 0 
rend = 0 
logado = False

base_dir = os.path.dirname(__file__) # Pega o caminho do arquivo atual
cliente_dir = os.path.join(base_dir, 'Clientes') # Cria o caminho do diretório teste dentro do diretório atual
os.mkdir(cliente_dir) if not os.path.exists(cliente_dir) else None # Cria o diretório teste se não existir

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print("Bem vindo ao Sistema Bancário\n 1. Acessar como Cliente\n 2. Acessar como Gerente\n 3. Encerrar programa")  
    menu1 = int(input("Escolha uma opção: "))

    if menu1==1:
        
        os.system('cls' if os.name == 'nt' else 'clear')
        idcliente = input("Insira o número da conta: ")
        clientenom = "cliente" + str(idcliente) + ".pickle"
        try: 
            file_path = os.path.join(cliente_dir, clientenom)
            with open(file_path, 'rb') as cliente:
                infoclient = pickle.load(cliente)
            os.system('cls' if os.name == 'nt' else 'clear')
            logado = True
        except:
            print("Não há uma conta com este número. Contate seu gerente.")
            input()
            continue
        
        while logado == True:
            
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("Menu Cliente:\n 1.Consultar saldo\n 2.Depositar\n 3.Sacar\Pix\n 4.Simular Rendimento\n 5.Voltar ao menu principal")
            menu2=int(input("Escolha uma opção: "))

            if menu2==1:
                os.system('cls' if os.name == 'nt' else 'clear')
                with open(file_path, 'rb') as cliente:
                    infoclient = pickle.load(cliente)
                print('Saldo: R$', infoclient['saldo'])
                input("Pressione Enter para continuar... ")
                
            if menu2 == 5:
                logado = False
    
    if menu1 == 3: #encerra o programa
        exit()
    #if menu1 == 1:
        #area de criação do cliente
    if menu1 == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        for x in range(0, 3):
            senha = input("Digite a senha: ")
            if senha == "banco":
                # Continuação do código de gerente
                logado = True
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Senha incorreta.")
        if x == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Senha incorreta digitada 3 vezes, fim do programa!")
            input()
            exit()
        while logado == True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Menu Gerente:\n1. Cadastrar ou Trocar Nome do Cliente\n2. Corrigir Saldo do Cliente\n3. Consultar Status do Cliente\n4. Voltar ao Menu Principal")
            menu2 = int(input("Escolha uma opção: "))
                
            if menu2 == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                idcliente = input("Insira o número da conta: ")
                clientenom = "cliente" + str(idcliente) + ".pickle"
                file_path = os.path.join(cliente_dir, clientenom)
                try: 
                    with open(file_path, 'rb') as gerente:
                        infoclient = pickle.load(gerente)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    infoclient['nome'] = input("Digite o novo nome do cliente: ")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Nome do cliente alterado com sucesso!")
                    input("Pressione Enter para continuar... ")
                except:
                    infoclient = {'id': idcliente, 'nome': "", 'saldo':  0.0,}
                    os.system('cls' if os.name == 'nt' else 'clear')
                    infoclient['nome'] = input("Cliente não encontrado. Digite o nome do novo cliente:")
                    with open(file_path, 'wb') as gerente:
                        pickle.dump(infoclient, gerente)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Cliente cadastrado com sucesso!")
                    input("Pressione Enter para continuar... ")

            if menu2 == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                idcliente = input("Insira o número da conta: ")
                clientenom = "cliente" + str(idcliente) + ".pickle"
                file_path = os.path.join(cliente_dir, clientenom)
                try: 
                    with open(file_path, 'rb') as gerente:
                        infoclient = pickle.load(gerente)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    infoclient['saldo'] = input("Digite o novo saldo do cliente: ")
                    with open(file_path, 'wb') as gerente:
                        pickle.dump(infoclient, gerente)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Saldo do cliente alterado com sucesso!")
                    input("Pressione Enter para continuar... ")
                except:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Cliente não encontrado. Cadastre-o com a opção 1.")
                    input("Pressione Enter para continuar...")

            if menu2 == 3:
                idcliente = input("Insira o número da conta: ")
                clientenom = "cliente" + str(idcliente) + ".pickle"
                file_path = os.path.join(cliente_dir, clientenom)
                try: 
                    with open(file_path, 'rb') as gerente:
                        infoclient = pickle.load(gerente)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("ID:", infoclient['id'], "\nNome:", infoclient['nome'], "\nSaldo: R$", infoclient['saldo'])
                    input("Pressione Enter para continuar... ")
                except:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Cliente não encontrado. Cadastre-o com a opção 1.")
                    input("Pressione Enter para continuar... ")

            if menu2 == 4:
                break
        
