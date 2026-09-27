"""Exercício de saldo em memória; não representa uma aplicação bancária real."""
import math


def validar_valor(texto):
    try:
        valor = float(texto.replace(",", "."))
    except ValueError:
        raise ValueError("Digite um número válido.") from None
    if not math.isfinite(valor) or valor <= 0:
        raise ValueError("Digite um valor positivo e finito.")
    return valor


def depositar(saldo, valor):
    return saldo + valor


def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente.")
    return saldo - valor


def main():
    saldo = 0.0
    while True:
        print("\n1 - Depositar | 2 - Sacar | 3 - Ver saldo | 4 - Sair")
        opcao = input("Escolha: ").strip()
        if opcao == "4":
            print("Encerrando...")
            break
        if opcao == "3":
            print(f"Saldo: R$ {saldo:.2f}")
        elif opcao in {"1", "2"}:
            try:
                valor = validar_valor(input("Valor: R$ "))
                saldo = depositar(saldo, valor) if opcao == "1" else sacar(saldo, valor)
                print(f"Operação concluída. Saldo: R$ {saldo:.2f}")
            except ValueError as exc:
                print(exc)
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
