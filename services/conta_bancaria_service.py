from entities import ContaBancaria
from repositories import ContaBancariaRepository
import uuid


class ContaBancariaService:

    def cadastrar(self, valor_inicial: float):
        if valor_inicial < 100:
            raise ValueError("O deposito inicial deve ser no mínimo de R$ 100")

        numero_conta = str(uuid.uuid1())
        conta_bancaria = ContaBancaria(numero_conta, valor_inicial)

        conta_bancaria_repository = ContaBancariaRepository()
        conta_bancaria_repository.inserir(conta_bancaria)

        return conta_bancaria

    def __consultar(self, numero_conta: str):
        conta_bancaria_repository = ContaBancariaRepository()
        return conta_bancaria_repository.consultar(numero_conta)

    def consultar_saldo(self, numero_conta: str):
        return self.__consultar(numero_conta).get_saldo()

    def creditar(self, numero_conta: str, valor: float):
        conta = self.__consultar(numero_conta)

        conta.creditar(valor)

        conta_bancaria_repository = ContaBancariaRepository()
        conta_bancaria_repository.atualizar_saldo(conta)

    def debitar(self, numero_conta: str, valor: float):
        conta = self.__consultar(numero_conta)

        if conta.get_saldo() < valor:
            raise ValueError("Saldo insuficiente para operação")

        conta.sacar(valor)

        conta_corrente_repository = ContaBancariaRepository()
        conta_corrente_repository.atualizar_saldo(conta)

