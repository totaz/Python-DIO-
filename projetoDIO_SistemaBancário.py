import textwrap

def menu():
    menu = '''
    (d)     depositar
    (s)     sacar
    (e)     extrato
    (nc)    nova conta
    (lc)    listar contas
    (nu)    novo usuário
    (q)     sair
        =>'''
    return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato, /):
    if valor > 0 :
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n '
    else:
        print('Operação falhou! O valor informado é inválido.')
    
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saque >= limite_saque

    if excedeu_saldo:
        print('Operação falhou! Você não tem saldo suficiente.')
        
    elif excedeu_limite:
            print('Operação falhou! O valor do saque excedeu o limite.')

    elif excedeu_saques:
            print('Operação falhou! Número maximo de saques excedido.')

    elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saque += 1

    else:
            print('Operação falhou! O valor informado é inválido')
    
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ===============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (Somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('Usuário não encontrado, fluxo de criação de conta encerrado!')

def listar_contas(contas):
    for conta in contas:
        linha  = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    agencia = '0001'
    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    limite_saque = 3
    usuarios = []
    contas = []


    while True:
        opcao = menu()
    
        if opcao == 'd':
            valor = float(input('informe o valor do depósito: '))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('informe o valor do Saque: '))

            saldo, extrato = saque(
                saldo = saldo,
                valor = valor, 
                extrato = extrato, 
                limite = limite, 
                numero_saque = numero_saque, 
                limite_saque = limite_saque,
                )
            
        elif opcao == 'e':
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
             numero_conta = len(contas) + 1
             conta = criar_conta(agencia, numero_conta, usuarios)

             if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)
             
        elif opcao == 'q':
            break

        else:
            print('Operação inválida, por favor selecione novamente a operação desejada.')

main()