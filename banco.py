menu = """
      # MENU #
    [1] Depósito
    [2] Saque
    [3] Extrato
    [0] Sair
    -------------
    Digite aqui: """

saldo_conta = 0.00
limite = 500.00
numero_de_saques = 0
LIMITE_DE_SAQUE = 3
extrato = " "

while True:
    opcao = int(input(menu.center(10)))
    
    # Deposito
    if opcao == 1:
        saldo_deposito = float(input("Digite o Valor desejado: "))
        if saldo_deposito > 0:
            saldo_conta += saldo_deposito
            extrato += f"\n   Depósito Realizado! \n    R${saldo_deposito:.2f} \n==========================="
            
        else:
            print("\n===========================\nValor Invalido \n Deposite um valor valido!\n===========================\n")
            
    # Saque
    elif opcao == 2:
        valor_saque = float(input("Digite o valor de seu saque: "))
        
        excedeu_saldo = valor_saque > saldo_conta
        excedeu_limite = valor_saque > limite
        excedeu_limite_saque = numero_de_saques >=  LIMITE_DE_SAQUE
        
        if excedeu_limite:
            print("\n===========================\nInfelizmente essa Valor ultrapassa o Limite permitido por saque!\n===========================\n")
            
        elif excedeu_saldo:
            print("\n===========================\nValor ultrapassou seu saldo disponivel, acesse seu extrato e verifique seu saldo dispoivel para saque.\n===========================\n")
        
        elif excedeu_limite_saque:
            print("\n===========================\nVocê fez o seu Maximo de saques permitidos pelo banco no dia de Hoje, Volte Amanhã! \nObrigado!\n===========================\n")
        
        else:
            saldo_conta -= valor_saque
            numero_de_saques += 1
            extrato += f"\n      Saque Realizado! \n      R${valor_saque:.2f} \n==========================="
    
    # Extrato
    elif opcao == 3:
        if extrato == " ":
            print("\n===========================\nNão houve movimentações em sua conta \n===========================")
            print(f"Seu saldo atual é de R${saldo_conta:.2f}\n===========================")
        else:
            print("\n===========================" + extrato)
            print(f"Seu saldo atual é de R${saldo_conta:.2f}\n===========================")
        
    # Sair
    elif opcao == 0:
        break
    
    else:
        print("valor invalido")
    