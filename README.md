# 🏦 Sistema Bancário Simples em Python 🐍

**Bem-vindo ao seu banco na linha de comando!**

Este é um sistema bancário básico desenvolvido em Python para demonstrar funcionalidades essenciais como depósito, saque e visualização de extrato. Uma solução simples e direta para gerenciar suas finanças... de mentirinha, é claro! 😉

## ✨ Funcionalidades Principais

* **Depósito:** Adicione fundos à sua conta de forma rápida e fácil.
* **Saque:** Retire dinheiro da sua conta, respeitando um limite por saque e um número máximo de saques diários.
* **Extrato:** Visualize todas as movimentações da sua conta, incluindo depósitos e saques, além do seu saldo atual.
* **Segurança (Limitada):** Impõe limites de saque para simular um ambiente bancário com restrições.

## 🚀 Como Executar

1.  **Pré-requisitos:** Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo em [https://www.python.org/downloads/](https://www.python.org/downloads/).
2.  **Salve o Código:** Copie o código Python fornecido e salve-o em um arquivo com a extensão `.py` (por exemplo, `banco.py`).
3.  **Abra o Terminal:** Navegue até o diretório onde você salvou o arquivo `banco.py` usando o terminal (ou prompt de comando).
4.  **Execute o Script:** Digite o seguinte comando e pressione Enter:

    ```bash
    python banco.py
    ```

5.  **Interaja:** O menu do sistema bancário será exibido no seu terminal. Digite o número da opção desejada e siga as instruções.

## ⚙️ Detalhes Técnicos

* **Linguagem:** Python 3
* **Estrutura:** Um loop `while` principal controla a interação com o usuário, apresentando um menu de opções.
* **Variáveis:**
    * `saldo_conta`: Armazena o saldo atual da conta (inicializado em 0.00).
    * `limite`: Define o limite máximo para cada saque (R$ 500.00).
    * `numero_de_saques`: Contador do número de saques realizados no dia (inicializado em 0).
    * `LIMITE_DE_SAQUE`: Define o número máximo de saques permitidos por dia (3).
    * `extrato`: Uma string que armazena o histórico de transações.

## 🤔 Próximos Passos (Ideias para Melhorias)

Este é um sistema bem básico! Aqui estão algumas ideias para torná-lo ainda mais interessante:

* **Autenticação:** Implementar um sistema de login com usuário e senha.
* **Transferências:** Adicionar a funcionalidade de transferir fundos entre contas.
* **Histórico Persistente:** Salvar o histórico de transações em um arquivo para que os dados não sejam perdidos ao fechar o programa.
* **Interface Gráfica:** Desenvolver uma interface gráfica de usuário (GUI) para uma experiência mais visual e amigável.
* **Tratamento de Erros Mais Robusto:** Adicionar mais validações de entrada para evitar comportamentos inesperados.

**Divirta-se explorando o mundo da programação bancária!** 😉
