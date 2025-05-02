from datetime import datetime
from random import randint
import locale

class transacao:
    def __init__(self, tipo, valor, hora):
        self.tipo = tipo
        self.valor = valor
        self.hora = hora


locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

saldo_conta = 0.00
limite = 500.00
numero_de_saques = 0
numero_de_transacao = 0
LIMITE_DE_SAQUE = 3
LIMITE_DE_TRANSACAO = 10

clientes = {}
contas = {}
extrato = []

def CadastrarCliente(nome, nascimento, CPF, logradoro, numero, bairro, cidade):
    
    global clientes
    
    cliente = {
        "nome" : nome,
        "nascimento" : nascimento,
        "CPF" : CPF ,
        "endereco" : {
            "Logradouro" : logradoro,
            "Numero" : numero,
            "Bairro" : bairro,
            "Cidade/UF" : cidade
        }
    }
    
    clientes[CPF] = cliente
    print("="*30)
    print(" Cliente cadastrado com sucesso!".center(30))
    print("="*30)


def GerarNumeroConta():
    return str(randint(10000000, 99999999))


def criar_nova_conta(cpf):
    """Cria uma nova conta corrente para um cliente com o CPF fornecido."""
    numero_conta = GerarNumeroConta()
    while True:
        if numero_conta not in contas.values():
            break

    agencia = "0001"
    banco = "0123"
    numero_completo = f"{numero_conta}-{randint(0, 9)}"
    conta_completa = f"Agência {agencia}, Conta {numero_completo}, Banco {banco}"
    
    if cpf in contas:
        contas[cpf].append(conta_completa)
        
    else:
        contas[cpf] = [conta_completa]

    print(f"Conta Corrente Criada com Sucesso, para o cliente {clientes[cpf]['nome']}: {conta_completa}")
    
    
def Realizar_deposito():
    saldo_deposito = float(input("Digite o Valor desejado: "))
    global saldo_conta, numero_de_transacao
        
    if excedeu_limite_transacao:
        print("")
        print("="*43)
        print("   Você fez o seu Maximo de transações\n   permitidos pelo banco no dia de Hoje,\n   volte Amanhã! \n   Obrigado!")
        print("="*43)
    
    else:
        if saldo_deposito > 0:
            saldo_conta += saldo_deposito
            numero_de_transacao += 1
            extrato.append(transacao("Depósito", saldo_deposito, horario_transacao))
            
            print("")
            print("="*30)
            print("   Deposito efetuado.")
            print(f"   Saldo R${saldo_conta:.2f}")
            print("="*30)
        
        else:
            print("")
            print("="*42)
            print("    Valor Invalido \n    Deposite um valor valido!")
            print("="*42)
    

def Realizar_saque():
    valor_saque = float(input("Digite o valor de seu saque: "))
    
    global saldo_conta, numero_de_saques, numero_de_transacao
    
    excedeu_saldo = valor_saque > saldo_conta
    excedeu_limite = valor_saque > limite
    excedeu_limite_saque = numero_de_saques >=  LIMITE_DE_SAQUE
    
    
    if valor_saque > 0:
        if excedeu_limite_transacao:
            print("")
            print("="*42)
            print("Você fez o seu Maximo de transações permitidos pelo banco no dia de Hoje, Volte Amanhã! \nObrigado!")
            print("="*42)
        
        else:
            if excedeu_limite:
                print("")
                print("="*42)
                print("   Infelizmente essa Valor ultrapassa o\n   Limite permitido por saque!")
                print("="*42)
                
            elif excedeu_saldo:
                print("")
                print("="*42)
                print(" Valor ultrapassou seu saldo disponivel,\n acesse seu extrato e verifique seu\n saldo dispoivel para saque.")
                print("="*42)
            
            elif excedeu_limite_saque:
                print("")
                print("="*42)
                print("     Você fez o seu Maximo de saques\n     permitidos pelo banco no dia de\n     hoje, volte Amanhã! \n     Obrigado!")
                print("="*42)
            
            else:
                saldo_conta -= valor_saque
                numero_de_saques += 1
                numero_de_transacao += 1
                extrato.append(transacao("Saque", valor_saque, horario_transacao))
                
                print("")
                print("="*30)
                print("   Saque efetuado.")
                print(f"   Saldo R${saldo_conta:.2f}")
                print("="*30)
                
    else:
        print("")
        print("="*42)
        print("    Valor Invalido \n    Insira um valor valido!")
        print("="*42)


def Mostrar_extrato():
    if extrato == []:
        print("")
        print("="*42)
        print("Não houve movimentações em sua conta".center(42))
        print("="*42)
        print(f"Seu saldo atual é de R${saldo_conta:.2f}".center(42))
        print("="*42)
        
    else:
        print("")
        print("="*42)
        for transacao_obj in extrato:
            print(f"Tipo: {transacao_obj.tipo.capitalize()}")
            print(f"Data/Hora: {transacao_obj.hora}")
            print(f"Valor: R${transacao_obj.valor:.2f}")
            print("=" * 42)
        print("="*42)
        print(f"Seu saldo atual é de R${saldo_conta:.2f}".center(42))
        print("="*42)


def Novo_usuario():
    print("\n" + "="*70)
    nome_cliente = input("   Nome completo: ")
    
    while True:
        print("="*70)
        try:
            data_de_nascimento = int(input("   Data de nascimento (apenas numeros): "))
            break
        except ValueError:
            print("="*70)
            print("   Erro: Por favor, digite apenas números para a data de nascimento.")
    
    while True:        
        print("="*70)
        try:
            cpf = int(input("   CPF (apenas numeros): "))
            contagemCPF = len(str(cpf))
            if contagemCPF < 11 or contagemCPF > 11:
                print("="*70)
                print("   Numero de CPF invalido, aplique um CPF valido.")
            else:
                break
        
        except ValueError:
            print("="*70)
            print("   Erro: Por favor, digite apenas números para CPF.")
            
    print("="*70)
    logradouro_end = input("   Endereço (apenas logradouro): ")
    print("="*70)
    numero_end = input("   Endereço (apenas Numero + complemento se tiver): ")
    print("="*70)
    bairro_end = input("   Endereço (apenas bairro): ")
    print("="*70)
    Cidade_end = input("   Endereço (apenas Cidade e UF, ex = São Paulo/SP): ")
    print("="*70)
    
    CadastrarCliente(nome_cliente, data_de_nascimento, cpf, logradouro_end, numero_end, bairro_end, Cidade_end)
    print(clientes)

def CriarConta():
    consultaCPF = int(input('Digite seu numero de CPF: '))
            
    if consultaCPF not in clientes:
        print("="*70)
        print("   Cliente não localizado, verifique CPF e tente novamente.\n   Caso não tenha cadastrado, volte na opção anterior, leva apenas\n   alguns segundos, Obrigado.")
        print("="*70)
        
    elif consultaCPF in contas:
        print("="*70)
        print("   Vejo que você Já possui uma conta, deseja abrir uma nova?\n   [1] Sim e [2] Não")
        print("="*70)
        
        while True:
            retorno = int(input())
            if retorno == 1:
                criar_nova_conta(consultaCPF)
                
                break
            
            elif retorno == 2:
                print("="*70)
                print("   Tudo bem, Obrigado.")
                print("="*70)
                break
            else:
                print("="*70)
                print("   Ops, esse valor não é valido, digite um valor valido.")
                print("="*70)
    
    else:
        criar_nova_conta(consultaCPF)
      

def ListarConta():
    consultaCPF = input('Digite seu numero de CPF: ')
            
    if consultaCPF in contas:
        print(f"Nome cliente: {clientes[consultaCPF]["nome"]}")
        for conta in contas[consultaCPF]:
            print(f"=> {conta}")
    
    else:
        print("Nenhum CPF encontrado.")
        
                
def main():
    menu = """
      # MENU #
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Novo Usuario
    [5] Criar Conta
    [6] Listar Contas
    [0] Sair
    --------------------
    Digite aqui: """

    global excedeu_limite_transacao, horario_transacao, extrato, clientes

    
    
    while True:
        opcao = int(input(menu.center(10)))
        excedeu_limite_transacao = numero_de_transacao >= LIMITE_DE_TRANSACAO
        horario_transacao = datetime.now().strftime('%a %d/%m/%Y %H:%M:%S')
        
        # Deposito
        if opcao == 1:
            Realizar_deposito()
                    
        # Saque
        elif opcao == 2:
            Realizar_saque()
                
        # Extrato
        elif opcao == 3:
            Mostrar_extrato()
        
        # Cadastro Cliente
        elif opcao == 4:
            Novo_usuario()
        
        # Criar Conta
        elif opcao == 5:
            CriarConta()
        
        # Listar Conta
        elif opcao == 6:
            ListarConta()
            
        # Sair
        elif opcao == 0:
            break
        
        else:
            print("valor invalido")

main()