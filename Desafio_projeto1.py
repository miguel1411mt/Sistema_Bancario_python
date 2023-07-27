account = 0
help_while = 0
score_deposit = 0
score_withdraw = 0
list_deposit = []
list_withdraw = []

while True:
    print("")
    print(10*"=", "banco", 10*"=")
    print("  O que você deseja fazer?")
    print("""[1] Depositar
[2] Sacar
[3] Ver saldo
[4] Sair""")

    user = " "
    while user not in "1234":
        user = str(input("Digite aqui sua escolha: "))

    if user == "1":
        while True:
            user_deposit = input("Digite a quantia que você deseja depositar: ")

            if user_deposit.isnumeric() is True:
                for_int_deposit = float(user_deposit)

                if for_int_deposit > 0:
                    print(f"\033[1;32m Depósito completado com êxito -- Valor: R${for_int_deposit}0 \033[m")
                    account += for_int_deposit
                    list_deposit.append(f"R${for_int_deposit}0")
                    score_deposit += 1
                    break

                else:
                    print("\033[1;31m ERRO: O valor precisa ser maior que zero! \033[m")
            else:
                print("\033[1;31m Ops!!, algo deu errado! \033[m")

    if user == "2":
        while True:
            user_withdraw = input("Digite a quantia que você deseja sacar: ")

            if user_withdraw.isnumeric() is True:
                for_int_withdraw = float(user_withdraw)

                if account < for_int_withdraw:
                    print("\033[1;31m Você não tem saldo suficiente para essa quantia solicitada!\033[m")
                    break

                if 0 < for_int_withdraw <= 500:
                    help_while += 1

                    if help_while > 3:
                        print("\033[1;31m O limite de saque foi atingido!\033[m")
                        break

                    print(f"\033[1;32m Saque completado com êxito -- Valor: R${for_int_withdraw}0 \033[m")
                    account -= for_int_withdraw
                    list_withdraw.append(f"R${for_int_withdraw}0")
                    score_withdraw += 1
                    break

                else:
                    print("\033[1;31m ERRO: O limite máximo é R$500,00 por saque! \033[m")
            else:
                print("\033[1;31m Ops!!, algo deu errado! \033[m")

    if user == "3":
        print(f"Você tem \033[7mR${account}0\033[m reais na sua conta")

    if user == "4":
        break

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

print("")
print(29*"=")
