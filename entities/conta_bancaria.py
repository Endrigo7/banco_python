class ContaBancaria:

    def __init__(self, numero_conta: str, senha: str, valor_inicial: float):
        self.__numero_conta = numero_conta
        self.__senha = senha
        self.__saldo = valor_inicial

    def get_numero_conta(self):
        return self.__numero_conta

    def get_saldo(self):
        return self.__saldo

    def get_senha(self):
        return self.__senha

    def creditar(self, valor: float):
        self.__saldo += valor

    def sacar(self, valor: float):
        self.__saldo -= valor

    def transferir(self, conta_bancaria, valor: float):
        conta_bancaria.debitar(valor)
        self.creditar(valor)

    def to_string(self):
        return f'numero_conta: {self.__numero_conta} saldo: {self.__saldo}'
