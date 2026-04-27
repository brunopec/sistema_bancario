from datetime import datetime

def gerar_comprovante(nome, tipo_operacao, valor):
    agora = datetime.now()
    data_titulo = agora.strftime("%d_%m_%Y %H-%M")
    data_hora = agora.strftime("%d/%m/%Y %H:%M:%S")

    nome_arquivo = f"comprovantes_{nome}_{tipo_operacao}_{data_titulo}.txt"

    with open(nome_arquivo, "x", encoding="utf-8") as arquivo:
        arquivo.write("Comprovante de Operação\n")
        arquivo.write(f"Data/Hora: {data_hora}\n")
        arquivo.write(f"Tipo de Operação: {tipo_operacao}\n")
        arquivo.write(f"Valor: R$ {valor:.2f}\n")
        arquivo.write(f"Saldo Atual: R$ {valor:.2f}\n")
        arquivo.write("-" * 30 + "\n")

class Conta:
    def __init__(self, nome, usuario, senha):
        self.nome = nome
        self.usuario = usuario
        self._senha = senha
        self.saldo = 0.0



