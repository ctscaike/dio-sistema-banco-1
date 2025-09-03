# App baseado no template sugerido no Desafio da DIO

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print("Bem vindo ao Banco V1.6!")

def main():
    global saldo, limite, extrato, numero_saques
    
    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            print(f'o numero atual de saques é: {numero_saques}')
            valor = float(input("Informe o valor a sacar: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )
        elif opcao == "e":
            mostra_extrato(saldo, extrato=extrato)
        elif opcao == "q":
            print("Saindo do APP")
            break
        else:
            print(f"Opção '{opcao}' inválida. Por favor selecione uma operação válida!\n")
            opcao = input(menu)

def menu():
    print("Selecione uma das opções abaixo pra realizar uma operação:\n")

    print("[d] Realizar Depósito")
    print("[s] Realizar Saque")
    print("[e] Visualizar Extrato")
    print("[q] Sair")
    
    return input("Escolha uma opção: ")

def depositar(saldo, valor, extrato):
    if (valor > 0):
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!\n")
    else:
        print("Valor inválido para depósito")
    
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if (valor > saldo):
        print("Saldo insuficiente. Falha na operação")
    elif (valor > limite):
        print("O valor solicitado excede o limite de saque. Falha na operação")
    elif (numero_saques > LIMITE_SAQUES):
        print("Número máximo de saques atingido. Falha na operação")
    elif (valor > 0):
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!\n")
        numero_saques = (numero_saques + 1)
    else:
        print("Valor inválido para saque")

    return saldo, extrato, numero_saques

def mostra_extrato(saldo, extrato):
    print("\n" + "*" * 30)
    print("EXTRATO")
    print("*" * 30)
    print("Não existem movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("*" * 30)

if __name__ == "__main__":
    main()