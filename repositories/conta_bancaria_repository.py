from repositories.mysql_conexao_util import MySQLConexaoUtil
from entities import ContaBancaria

class ContaBancariaRepository:

    def inserir(self, conta_bancaria):
        comando_sql = f'insert into conta_bancaria (numero_conta, saldo) values ("{conta_bancaria.get_numero_conta()}", "{conta_bancaria.get_saldo()}")'

        cursor = MySQLConexaoUtil.get_cursor()
        cursor.execute(comando_sql)
        MySQLConexaoUtil.commit()
        cursor.close()

    def consultar(self, numero_conta):
        comando_sql = f'select numero_conta, saldo from conta_bancaria where numero_conta = "{numero_conta}"'
        cursor = MySQLConexaoUtil.get_cursor()
        cursor.execute(comando_sql)
        row = cursor.fetchone()
        cursor.close()

        if row is None:
            raise ValueError(f'Conta {numero_conta} não foi encontrada ')

        return ContaBancaria(row[0], row[1])

    def atualizar_saldo(self, conta_bancaria):
        comando_sql = f'update conta_bancaria set saldo = "{conta_bancaria.get_saldo()}" where numero_conta = "{conta_bancaria.get_numero_conta()}"'
        cursor = MySQLConexaoUtil.get_cursor()
        cursor.execute(comando_sql)
        MySQLConexaoUtil.commit()
        cursor.close()
