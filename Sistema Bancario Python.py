python banco.py

def mostrar_menu():
    print("\n===== SISTEMA BANCÁRIO =====")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")


def validar_valor(valor_str):
    try:
        valor = float(valor_str)
        if valor <= 0:
            print("⚠️ Digite um valor positivo.")
            return None
        return valor
    except ValueError:
        print("⚠️ Entrada inválida! Digite um número.")
        return None


def depositar(saldo):
    valor = validar_valor(input("Valor para depósito: R$ "))
    if valor is not None:
        saldo += valor
        print("✅ Depósito realizado com sucesso!")
    return saldo


def sacar(saldo):
    valor = validar_valor(input("Valor para saque: R$ "))
    if valor is None:
        return saldo

    if valor > saldo:
        print("❌ Saldo insuficiente!")
        return saldo

    saldo -= valor
    print("✅ Saque realizado com sucesso!")
    return saldo


def ver_saldo(saldo):
    print(f"💰 Saldo atual: R$ {saldo:.2f}")


def main():
    saldo = 0.0

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            saldo = depositar(saldo)

        elif opcao == "2":
            saldo = sacar(saldo)

        elif opcao == "3":
            ver_saldo(saldo)

        elif opcao == "4":
            print("👋 Encerrando sistema...")
            break

        else:
            print("⚠️ Opção inválida!")


if __name__ == "__main__":
    main()