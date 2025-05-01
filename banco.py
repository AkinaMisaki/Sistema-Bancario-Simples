import pickle
import os

#declaração das variaveis
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

    if menu1==1:#Opção do cliente selecionada
        
        os.system('cls' if os.name == 'nt' else 'clear')
        idcliente = input("Insira o número da conta: ")
        clientenom = "cliente" + str(idcliente) + ".pickle"
        try:                                                    #Confirma se a conta do cliente existe
            file_path = os.path.join(cliente_dir, clientenom)
            with open(file_path, 'rb') as cliente:
                infoclient = pickle.load(cliente)
            os.system('cls' if os.name == 'nt' else 'clear')
            logado = True
        except:                                                 #Caso não exista, consultar um gerente para criar a conta.
            print("Não há uma conta com este número. Contate seu gerente.")
            input()
            continue
        
        while logado == True: #Caminho do cliente selecionado
            
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("Menu Cliente:\n 1.Consultar saldo\n 2.Depositar\n 3.Sacar\Pix\n 4.Simular Rendimento\n 5.Voltar ao menu principal")
            menu2=int(input("Escolha uma opção: "))

            if menu2==1:                                         #Opção de consulta de saque selecionada
                os.system('cls' if os.name == 'nt' else 'clear')
                with open(file_path, 'rb') as cliente:
                    infoclient = pickle.load(cliente)
                print('Saldo: R$', infoclient['saldo'])
                input("Pressione Enter para continuar... ")

            if menu2==2:                                         #Opção de Deposito selecionada
                os.system('cls' if os.name == 'nt' else 'clear')
                with open(file_path, 'rb') as cliente:
                    infoclient = pickle.load(cliente)
                valor = int(input("Digite o valor a ser depositado:"))

                while valor <=0:                                 #Garantia que o valor selecionado não seja negativo nem zero
                    os.system('cls' if os.name == 'nt' else 'clear')
                    valor = int(input("Valor negativo ou zero não suportado para deposito, digite novamente:"))

                valatual = infoclient['saldo']
                valatual = int(valatual)
                valatual = valatual + valor
                infoclient['saldo'] = valatual
                with open(file_path, 'wb') as cliente:
                    pickle.dump(infoclient, cliente)
                input("Valor depositado com sucesso, pressione enter para continuar ...")

            if menu2==3:                                         #Opção de saque selecionada
                os.system('cls' if os.name == 'nt' else 'clear')
                with open(file_path, 'rb') as cliente:
                    infoclient = pickle.load(cliente)
                valor = int(input("Digite o valor a ser sacado:"))

                while valor <=0:                                 #Garantia que o valor selecionado não seja negativo nem zero
                    os.system('cls' if os.name == 'nt' else 'clear')
                    valor = int(input("Valor negativo ou zero não suportado para deposito, digite novamente:"))

                valatual = infoclient['saldo']
                valatual = int(valatual)
                valatual = valatual - valor
                infoclient['saldo'] = valatual
                with open(file_path, 'wb') as cliente:
                    pickle.dump(infoclient, cliente)
                input("Valor sacado com sucesso, pressione enter para continuar ...")
            
            if menu2==4:                                        #Opção de rendimento selecionada
                os.system('cls' if os.name == 'nt' else 'clear')
                with open(file_path, 'rb') as cliente:
                    infoclient = pickle.load(cliente)
                valatual = infoclient['saldo']
                valatual = int(valatual)

                for x in range(1, 13):
                    valatual = valatual *1.011
                    print(f"Mês {x}, valor rendido: R${valatual}")
                input("Pressione enter para continuar ...")
                
            if menu2 == 5:
                logado = False
    
    if menu1 == 3: #encerra o programa
        exit()

    if menu1 == 2:                                          #Opção de gerente selecionada
        os.system('cls' if os.name == 'nt' else 'clear')
        for x in range(0, 3):                               #Solicitação de autenticação do gerente
            senha = input("Digite a senha: ")
            if senha == "banco":
                # Continuação do código de gerente
                logado = True
                break
            else:                                           
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Senha incorreta.")
        if x == 2:                                          #Força finalização do programa caso a senha do cliente seja digitada incorretamente mais de 3 vezes
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Senha incorreta digitada 3 vezes, fim do programa!")
            input()
            exit()

        while logado == True:                               #Logado como gerente com a autenticação correta
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Menu Gerente:\n1. Cadastrar ou Trocar Nome do Cliente\n2. Corrigir Saldo do Cliente\n3. Consultar Status do Cliente\n4. Voltar ao Menu Principal")
            menu2 = int(input("Escolha uma opção: "))
                
            if menu2 == 1:                                  #Opção 1 selecionada do menu de gerente
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
                os.system('cls' if os.name == 'nt' else 'clear')
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
