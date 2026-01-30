from datetime import datetime

class Conta:
    def __init__ (self, nome, usuario, senha):
        self.nome = nome
        self.usuario = usuario
        self._senha = senha
        self.saldo = 0.0
    def auth(self, senha):
        return self._senha == senha
    def depositar(self, valor):
        if valor > 0:
           self.saldo += valor
           return True
        return False 
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False
    def _gerar_comprovante(self, tipo_operacao, valor):
        agora = datetime.now()
        data_hora = agora.strftime("%d/%m/%Y %H:%M:%S")
        nome_arquivo = f"comprovantes_{self.usuario}_{tipo_operacao}.txt"
        with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Data/Hora: {data_hora}\n")
            arquivo.write(f"Tipo de Operação: {tipo_operacao}\n")
            arquivo.write(f"Valor: R$ {valor:.2f}\n")
            arquivo.write(f"Saldo Atual: R$ {self.saldo:.2f}\n")
            arquivo.write("-" * 30 + "\n")