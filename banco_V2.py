import string

account_users = []
account = 0
help_while = 0
score_deposit = 0
score_withdraw = 0
list_deposit = []
list_withdraw = []

def menu():
    print("")
    print(10*"=", "banco", 10*"=")
    print("  O que você deseja fazer?")
    print("""[1] Criar usuário e Conta corrente
[2] Depositar
[3] Sacar
[4] Ver saldo
[5] Sair""")

def user_create(dict):
    print('\033[1;32m CRIANDO USUÁRIO \033[m')
    print('')
    dict = []

    while True:
        name = input('Nome: ').title()
        remove_space_name = name.translate({ord(c): None for c in string.whitespace})

        if remove_space_name.isalpha() is True:
            break
        else:
            print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')

    print(20*'=')
    print('\033[1;32m DATA DE NASCIMENTO \033[m')

    while True:
        year = input('Ano: ')

        if year.isnumeric() is True:
            mouth = input('mês: ')

            if mouth.isnumeric() is True:
                day = input('Dia: ')

                if day.isnumeric() is True:
                    break

                else:
                    print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')
            else:
                print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')
        else:
            print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')

    print(20*'=')
    while True:
        cpf = input('CPF: ')

        if cpf.isnumeric() is True:

            if cpf.__len__() == 11:

                for data in account_users:
                    while data == cpf:
                        print('\033[1;31m CPF já existente!! \033[m')
                        cpf = input('CPF: ')

                if cpf.isnumeric() is True:

                    if cpf.__len__() == 11:
                        break

                    else:
                        print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')
                else:
                    print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')
            else:
                print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')
        else:
            print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')

    print('\033[1;32m ENDEREÇO \033[m')
    while True:
        street = input('Rua: ').title()
        remove_space_street = street.translate({ord(c): None for c in string.whitespace})

        if remove_space_street.isalpha() is True:
            break
        else:
            print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')

    while True:
        number = input('Número: ')

        if number.isnumeric() is True:
            break
        else:
            print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')

    while True:
        district = input('Bairro: ').title()
        remove_space_district = district.translate({ord(c): None for c in string.whitespace})

        if remove_space_district.isalpha() is True:
            city = input('Cidade: ').title()
            remove_space_city = city.translate({ord(c): None for c in string.whitespace})

            if remove_space_city.isalpha() is True:
                state = input('Estado: ').title()
                remove_space_state = state.translate({ord(c): None for c in string.whitespace})

                if remove_space_state.isalpha() is True:
                    dict.append([cpf, name, year, mouth, day, street, number, district, city, state])
                    break

                else:
                    print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')
            else:
                print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')
        else:
            print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')

    print('\033[1;32m CRIAÇÃO DE CONTA \033[m')
    question = ' '
    print('Deseja criar uma conta?')

    while question not in '12':
        question = input('[1] SIM ---- [2] NÃO: ')

        if question == '1':
            print('\033[1;32m CONTA CRIADA \033[m')
            print(f'Usuario: {name}')
            print(f'CPF: {cpf}')
            print('Número da agencia: 0001')

        elif question == '2':
            print('\033[1;31m CRIAÇÃO DE CONTA ENCERRADA \033[m')

    return dict

def deposit(for_sum, score, /):
    cpf = input('Digite seu CPF para prosseguir: ')

    if cpf.isnumeric() is True:

        if cpf.__len__() == 11:

            for list_of_users in account_users:

                if cpf in list_of_users:
                    print('\033[1;32m CPF ENCONTRADO \033[m')

                    while True:
                        user_deposit = input("Digite a quantia que você deseja depositar: ")

                        if user_deposit.isnumeric() is True:
                            for_int_deposit = float(user_deposit)

                            if for_int_deposit > 0:
                                print(f"\033[1;32m Depósito completado com êxito -- Valor: R${for_int_deposit}0 \033[m")
                                for_sum += for_int_deposit
                                list_deposit.append(f"R${for_int_deposit}0")
                                score += 1
                                break

                            else:
                                print("\033[1;31m ERRO: O valor precisa ser maior que zero! \033[m")
                        else:
                            print("\033[1;31m Ops!!, algo deu errado! \033[m")
                else:
                    print(print('\033[1;31m CPF NÃO ENCONTRADO \033[m'))
        else:
            print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')
    else:
        print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')

    return for_sum, score

def withdraw(*, Help_while, for_subtraction, score):

    cpf = input('Digite seu CPF para prosseguir: ')

    if cpf.isnumeric() is True:

        if cpf.__len__() == 11:

            for list_of_users in account_users:

                if cpf in list_of_users:
                    print('\033[1;32m CPF ENCONTRADO \033[m')

                    while True:
                        user_withdraw = input("Digite a quantia que você deseja sacar: ")

                        if user_withdraw.isnumeric() is True:
                            for_int_withdraw = float(user_withdraw)

                            if account < for_int_withdraw:
                                print("\033[1;31m Você não tem saldo suficiente para essa quantia solicitada!\033[m")
                                break

                            elif 0 < for_int_withdraw <= 500:
                                Help_while += 1

                                if Help_while > 3:
                                    print("\033[1;31m O limite de saque foi atingido!\033[m")
                                    break

                                print(f"\033[1;32m Saque completado com êxito -- Valor: R${for_int_withdraw}0 \033[m")
                                for_subtraction -= for_int_withdraw
                                list_withdraw.append(f"R${for_int_withdraw}0")
                                score += 1
                                break

                            else:
                                print("\033[1;31m ERRO: O limite máximo é R$500,00 por saque! \033[m")
                        else:
                            print("\033[1;31m Ops!!, algo deu errado! \033[m")
                else:
                    print(print('\033[1;31m CPF NÃO ENCONTRADO \033[m'))
        else:
            print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')
    else:
        print('\033[1;31m Ops!!, algo deu errado. Tente novamente! \033[m')

    return Help_while, for_subtraction, score

def extract():
    print("")
    print(10*"=", "EXTRATO", 10*"=")

    print("DEPÓSITOS:")
    print(f"Quantidade de depósitos: {score_deposit}")
    for data in list_deposit:
        print(f"== {data} ==")

    print("SAQUES:")
    print(f"Quantidade de saques: {score_withdraw}")
    for data in list_withdraw:
        print(f"== {data} ==")

    print(f'Seu saldo atual: R${account}0')

    print("")
    print(29*"=")

while True:

    menu()

    user = " "
    while user not in "12345":
        user = str(input("Digite aqui sua escolha: "))

    if user == '1':
        account_users = user_create(account_users)

    if user == "2":
        account, score_deposit = deposit(account, score_deposit)

    elif user == "3":
        help_while, account, score_withdraw = withdraw(Help_while=help_while, for_subtraction=account, score=score_withdraw)

    elif user == "4":
        print(f"Você tem \033[7mR${account}0\033[m reais na sua conta")

    elif user == "5":
        break

extract()
