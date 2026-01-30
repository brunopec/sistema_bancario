from conta import Conta
def conta_funcionalidades(conta):
    while True:
        print("\n--- Menu da Conta ---")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Transferir")  
        print("5. Pagar conta")
        print("6. Logout")

        escolha = input("Escolha: ")

        if escolha == '1':
            print(f"Saldo atual: R$ {conta.saldo:.2f}")

        elif escolha == '2':
            valor = float(input("Valor para depósito: "))
            conta.saldo += valor
            print("Depósito realizado.")

        elif escolha == '3':
            valor = float(input("Valor para saque: "))
            if valor <= conta.saldo:
                conta.saldo -= valor
                print("Saque realizado.")
            else:
                print("Saldo insuficiente.")

        elif escolha == '6':
            print("Logout realizado.")
            break

        else:
            print("Opção inválida.")
