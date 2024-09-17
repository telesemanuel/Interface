from modulo import *

if __name__ == "__main__":
  
    #construtor - instaciando o objeto da subclasse
    cc = ContaCorrente('', '', '1001-1', '10010-1', 0)

    #recebendo dados
    cc.nome = input('Informe o nome do titular: ')
    cc.cpf = input('Informe o cpf do titular: ')

    print('\n')
    print(f'{'-'*10}Dados do Titular{'-'*10}')
    print(f'Titular da conta: {cc.nome}.')
    print(f'CPF: {cc.cpf}.')
    print(f'Agencia: {cc.agencia}.')
    print(f'Conta: {cc.conta}.')
    
    while True:
        print('\n')
        print(f'\n{'=' * 20} Serpent Bank |{'=' * 20}\n')

        
        print('1 - Saldo')
        print('2 - Depósito')
        print('3 - Saque')
        print('0 - Sair')

        op = input('Informe a ação que deseja fazer: ')

        if op == '1':
            print('Saldo em conta R$ {cc.saldo}')
            continue
        elif op == '2':
            deposito = int(input('Informe o valor do depósito: '))
            cc.fazer_deposito(deposito)
            print(f'Depósito efetuado com sucesso!')
            continue
        elif op == '3':
            saque = int(input('Informe o valor do saque: '))
            cc.fazer_saque(saque)
            print(f'Saque efetuado no valor de R$ {saque:,.2f}.')
            continue
        else:
            break














