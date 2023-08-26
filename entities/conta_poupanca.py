from entities.conta_bancaria import ContaBancaria


class ContaPoupaunca(ContaBancaria):

    __taxa_juros = 0.002

    def __int__(self, numero_conta: str, valor_inicial: float):
        super().__int__(numero_conta, valor_inicial)

    def render_juros(self):
        juros = self.get_saldo() * ContaPoupaunca.__taxa_juros
        self.creditar(juros)

