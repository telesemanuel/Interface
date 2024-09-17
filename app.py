from modulo import *

if __name__ == "__main__":
  
    #construtor - instaciando o objeto da subclasse
    cc = ContaCorrente(" ", " ", "1001-1", "10010-1", 0)

    #recebendo dados
    cc.nome = input('Informe o nome do titular: ')
    cc.cpf = input('Informe o cpf do titular: ')

    while True:
        print('\n')
        print(f"{'-'*10}Dados do Titular{'-'*10}")
        print(f"Titular da conta: {cc.nome}.")
        print(f"CPF: {cc.cpf}.")
        print(f"Conta: {cc.conta}.")
        print(f"Agencia: {cc.agencia}.")
        print(f"Saldo: R$ {cc.saldo}")
        
        print(f"\n{cc.nome} deseja realizar qual operação?")
        print("1 - saldo")
        print("2 - depósito")
        print("3 - Saque")
        print("4 - Sair")
        
        op = input("escolha uma opcao: ")
        match op:
            case "1":
                print("Consultar Saldo\n")
                print(f"Saldo disponível R$ {cc.consultar_saldo():,.2f}.")
            case "2":
                valor = float(input(" Valor depósito: R$").replace(",","."))
                if valor > 0:
                    cc.saldo = cc.fazer_deposito(valor)
                    print("Depósito efetuado com sucesso.")
                    print(f"Saldo atual: R$ {cc.consultar_saldo():,.2f}")
                else:
                    print("Valor inválido")
                    continue
            case "3":
                valor = float(input("Valor do Saque: R$ ").replace(",","."))
                if valor <= cc.saldo:
                    cc.saldo = cc.fazer_saque(valor)
                    print("Saque efetuado com sucesso.")
                    print(f"Saldo atual: R$ {cc.consultar_saldo:,.2f}")
                else:
                    print("Não foi possível efetuar saque.")
            case "4":
                print("Saindo...")
                break
            case _:
                print("Opção Inválida")
















