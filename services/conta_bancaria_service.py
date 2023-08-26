from entities import ContaBancaria
from repositories import ContaBancariaRepository
from util import SenhaUtil
import uuid


class ContaBancariaService:

    def cadastrar(self, senha:str, confirmacao_senha: str, valor_inicial: float):
        if senha != confirmacao_senha:
            raise Exception("A senha não deve ser diferente da confirmação da senha")

        if valor_inicial < 100:
            raise ValueError("O deposito inicial deve ser no mínimo de R$ 100")

        numero_conta = str(uuid.uuid1())
        senha_hash = SenhaUtil.cria_hash(senha)

        conta_bancaria = ContaBancaria(numero_conta, senha_hash, valor_inicial)

        conta_bancaria_repository = ContaBancariaRepository()
        conta_bancaria_repository.inserir(conta_bancaria)

        return conta_bancaria

    def __consultar(self, numero_conta: str, senha: str):
        conta_bancaria_repository = ContaBancariaRepository()
        conta = conta_bancaria_repository.consultar(numero_conta)

        if conta.get_senha() != SenhaUtil.cria_hash(senha):
            raise Exception("Senha invalida")

        return conta

    def consultar_saldo(self, numero_conta: str, senha: str):
        return self.__consultar(numero_conta, senha).get_saldo()

    def creditar(self, numero_conta: str, senha: str, valor: float):
        conta = self.__consultar(numero_conta, senha)

        conta.creditar(valor)

        conta_bancaria_repository = ContaBancariaRepository()
        conta_bancaria_repository.atualizar_saldo(conta)

    def debitar(self, numero_conta: str, senha:str, valor: float):
        conta = self.__consultar(numero_conta, senha)

        if conta.get_saldo() < valor:
            raise ValueError("Saldo insuficiente para operação")

        conta.sacar(valor)

        conta_corrente_repository = ContaBancariaRepository()
        conta_corrente_repository.atualizar_saldo(conta)

