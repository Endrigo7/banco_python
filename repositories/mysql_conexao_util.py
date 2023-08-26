import mysql.connector


class MySQLConexaoUtil:
    __conexao = None

    @classmethod
    def __get_conexao(cls):
        if MySQLConexaoUtil.__conexao is None:
            MySQLConexaoUtil.__conexao = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='123',
                database='serpro_python'
            )
        return MySQLConexaoUtil.__conexao

    @classmethod
    def get_cursor(cls):
        return MySQLConexaoUtil.__get_conexao().cursor()

    @classmethod
    def commit(cls):
        MySQLConexaoUtil.__get_conexao().commit()
