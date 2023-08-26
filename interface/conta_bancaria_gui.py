from services import ContaBancariaService

class ContaBancariaGui:

    def abrir_contar(self):
        print("Selecione o tipo de conta que você deseja abrir")
        print("[01] - conta corrente")
        print("[02] - conta poupanca")
        tipo_conta = int(input())

        valor_inicial = float(input("Digite o Valor do deposito inicial"))

        conta_bancaria_service = ContaBancariaService()

        try:
            conta = conta_bancaria_service.cadastrar(valor_inicial)
            print(f'sua conta foi cadatrastrada com sucesso. Numero Conta {conta.get_numero_conta()}')
        except Exception:
            print("Infelizmente ocorreu um erro ao cadastrar sua conta. Por favor, refaça a operação")

    def consultar_saldo(self):
        conta_bancaria_service = ContaBancariaService()

        numero_conta = input("Por favor, informe o número da sua conta")

        try:
            conta = conta_bancaria_service.consultar_saldo(numero_conta)
        except Exception:
            raise ValueError("A Conta não foi localizada. Por favor, tentar novamente")

