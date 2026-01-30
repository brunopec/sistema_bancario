from conta import Conta

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, nome, usuario, senha):
        if usuario in self.contas:
            return False
        self.contas[usuario] = Conta(nome, usuario, senha)
        return True

    def acessar_conta(self, usuario, senha):
        conta = self.contas.get(usuario)
        if conta and conta.auth(senha):
            return conta
        return None
