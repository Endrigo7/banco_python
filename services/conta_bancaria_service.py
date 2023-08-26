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

    def consultar(self, numero_conta: str):
        conta_bancaria_repository = ContaBancariaRepository()
        return conta_bancaria_repository.consultar(numero_conta)

    def consultar_saldo(self, numero_conta: str):
        return self.consultar(numero_conta).get_saldo()
