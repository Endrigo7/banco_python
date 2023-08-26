from services import ContaBancariaService


class ContaBancariaGui:

    def abrir_contar(self):
        print("Selecione o tipo de conta que você deseja abrir")
        print("[01] - conta corrente")
        print("[02] - conta poupanca")
        tipo_conta = int(input())

        senha = input("Digite a senha para a sua conta ")
        confirmacao_senha = input("Digite a confirmação da senha para sua conta ")

        valor_inicial = float(input("Digite o Valor do deposito inicial "))

        conta_bancaria_service = ContaBancariaService()

        try:
            conta = conta_bancaria_service.cadastrar(senha, confirmacao_senha, valor_inicial)
            print(f'sua conta foi cadatrastrada com sucesso. Numero Conta {conta.get_numero_conta()}')
        except Exception as e:
            print(f'Infelizmente ocorreu um erro ao cadastrar sua conta. Por favor, refaça a operação. Erro: {e.args}')

    def consultar_saldo(self):
        conta_bancaria_service = ContaBancariaService()

        numero_conta = input("Por favor, informe o número da sua conta! ")
        senha = input("Por favor, informe a senha da sua conta ")

        try:
            saldo = conta_bancaria_service.consultar_saldo(numero_conta, senha)
            print(f'O saldo da sua conta é: {saldo}')
        except Exception as e:
            print(f'Erro ao consultar saldo. Erro: {e.args}')

    def creditar(self):
        numero_conta = input("Por favor, informe o numero da conta ")
        senha = input("Por favor, informe a senha da sua conta ")
        valor = float(input("Por favor, informe o valor a ser creditado "))

        conta_bancaria_serivce = ContaBancariaService()

        try:
            conta_bancaria_serivce.creditar(numero_conta, senha, valor)
        except Exception as e:
            print(f'Não foi possível realizar o crédito na conta {numero_conta}. Erro: {e.args}')

    def debitar(self):
        numero_conta = input("Por favor, informe o número da conta ")
        senha = input("Por favor, informe a senha da sua conta ")
        valor = float(input("Por favor, informe informe o valor do debito "))

        conta_bancaria_serivce = ContaBancariaService()

        try:
            conta_bancaria_serivce.debitar(numero_conta, senha, valor)
        except Exception as e:
            print(f'Não foi possível realizar o debito na conta  {numero_conta}. Erro: {e.args}')
