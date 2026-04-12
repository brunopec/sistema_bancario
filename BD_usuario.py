import sqlite3 as connector
from conta import Conta

class BD_usuario:
    ## Função para criar o Banco de dados do sistema bancario 
    def criar_banco():
        conexao = connector.connect('banco.db')
        cursor = conexao.cursor()   
        cursor.execute('''CREATE TABLE IF NOT EXISTS contas (
                    nome TEXT NOT NULL,
                    usuario TEXT PRIMARY KEY NOT NULL,
                    senha TEXT NOT NULL
    )''')
        conexao.commit()
        cursor.close()
        conexao.close()

    ## Função para criar tabela de saldo dos usuarios
    def saldo_usuario():
        conexao = connector.connect('banco.db')
        cursor = conexao.cursor()   
        cursor.execute('''CREATE TABLE IF NOT EXISTS saldo (
                        usuario TEXT PRIMARY KEY NOT NULL,
                        saldo REAL NOT NULL,
                        FOREIGN KEY (usuario) REFERENCES contas (usuario)
        )''')
        conexao.commit()
        cursor.close()
        conexao.close()

    #Funçao para cadastrar o usuario no banco de dados
    def cadastrar_usuario(conta):
        try:
            conexao = connector.connect('banco.db')
            cursor = conexao.cursor()
            
            cursor.execute('''INSERT INTO contas (usuario,senha,nome)
                            VALUES (:usuario, :senha, :nome)''',
                            {'usuario': conta.usuario, 'senha': conta._senha, 'nome': conta.nome})
            cursor.execute('''INSERT INTO saldo (usuario,saldo)
                            VALUES (:usuario, 0.0)''',
                            {'usuario': conta.usuario})
            conexao.commit()
            return True

        except Exception as e:
            print("ERRO:", e)
            return False

        finally:
            cursor.close()
            conexao.close()
    #definir autentificação do usuario
    def auth(usuario, senha):
        conexao = connector.connect('banco.db')
        cursor = conexao.cursor()      
        comando = '''SELECT * FROM contas
                    WHERE usuario = :usuario AND senha = :senha'''
        cursor.execute(comando, {'usuario': usuario, 'senha': senha})
        autenth = cursor.fetchall()
        cursor.close() 
        conexao.close()
        return autenth
    

