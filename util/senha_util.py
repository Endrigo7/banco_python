import hashlib


class SenhaUtil:

    @classmethod
    def cria_hash(cls, senha: str):
        return hashlib.sha256(senha.encode('utf-8')).hexdigest()