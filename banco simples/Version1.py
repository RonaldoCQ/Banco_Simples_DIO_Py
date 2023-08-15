def Menu():
    print("Menu:")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    Menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input('Informe o valor de depósito:'))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação Falhou! O valor informado é inválido.')

    elif opcao == "2":
        valor = float(input('Informe o valor de saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= limite_saques

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo o suficiente.')

        elif excedeu_limite:
            print('Operação falhou! O valor de saque excede o limite permitido.')
            
        elif excedeu_saque:
            print('Operação falhou! O número máximo de saques foi excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('Operação Falhou! Por favor, tente novamente.')

    elif opcao == "3":
        print("\n============================= Extrato ============================= ")
        print('Não foram realizadas movimentações.'if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('===================================================================\n')

    elif opcao == "4":
        print('Obrigado por utilizar o sistema Braesto, volte sempre!')
        break

    else:
        print('A operação é inválida! Por favor, selecione novamente a operação desejada.')