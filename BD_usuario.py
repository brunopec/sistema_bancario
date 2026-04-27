import sqlite3 as sql
from tkinter import messagebox
import conta as conta


# ------------------ BANCO ------------------
def criar_banco():
    conn = sql.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            nome TEXT NOT NULL,
            usuario TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            saldo REAL DEFAULT 0.0
        )
    ''')

    conn.commit()
    conn.close()


# ------------------ CADASTRO ------------------
def confirmar_cadastro(janela_cadastro, janela_login, entry_nome, entry_usuario, entry_senha):
    nome = entry_nome.get().strip()
    usuario = entry_usuario.get().strip()
    senha = entry_senha.get().strip()

    if not nome or not usuario or not senha:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    conn = sql.connect('banco.db')
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO usuarios (nome, usuario, senha, saldo) VALUES (?, ?, ?, ?)",
            (nome, usuario, senha, 0.0)
        )
        conn.commit()

        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        janela_cadastro.destroy()
        janela_login.deiconify()

    except sql.IntegrityError:
        messagebox.showerror("Erro", "Usuário já existe!")

    finally:
        conn.close()


# ------------------ LOGIN ------------------
def realizar_login(janela_login, abrir_tela_usuario, entry_usuario, entry_senha):
    usuario = entry_usuario.get().strip()
    senha = entry_senha.get().strip()

    if not usuario or not senha:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    conn = sql.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute("SELECT senha FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado and resultado[0] == senha:
        janela_login.withdraw()
        abrir_tela_usuario(usuario, janela_login)
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

#--------------------NOME------------------
def obter_nome(usuario):
    conn = sql.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else "Usuário"

# ------------------ SALDO ------------------
def consultar_saldo(usuario):
    conn = sql.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute("SELECT saldo FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()

    conn.close()
    return resultado[0] if resultado else 0.0



# ------------------ DEPOSITAR ------------------
def depositar(nome, usuario, valor, funcao_gerar_comprovante):
    if valor <= 0:
        messagebox.showerror("Erro", "Valor inválido!")
        return False

    conn = sql.connect('banco.db')
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE usuarios SET saldo = saldo + ? WHERE usuario = ?",
            (valor, usuario)
        )
        conn.commit()
        
        funcao_gerar_comprovante(nome,"deposito", valor) 
        return True 

    except Exception as e:
        messagebox.showerror("Erro", f"Falha na operação: {e}")
        return False
    finally:
        conn.close()
       

# ------------------ SACAR ------------------
def sacar(nome, usuario, valor, gerar_comprovante):
    saldo = consultar_saldo(usuario)

    if valor <= 0:
        messagebox.showerror("Erro", "Valor inválido!")
        return False

    if valor > saldo:
        messagebox.showerror("Erro", "Saldo insuficiente!")
        return False

    conn = sql.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE usuarios SET saldo = saldo - ? WHERE usuario = ?",
        (valor, usuario)
    )

    conn.commit()
    conn.close()
    gerar_comprovante(nome, "saque", valor)
    return True
    


# ------------------ TRANSFERIR ------------------

def transferir(nome, origem, destino, valor, gerar_comprovante):
    
    
    conn = sql.connect('banco.db')
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE usuarios SET saldo = saldo - ? WHERE usuario = ?", (valor, origem))
        cursor.execute("UPDATE usuarios SET saldo = saldo + ? WHERE usuario = ?", (valor, destino))
        conn.commit()
        
        
        gerar_comprovante(nome, "transferencia", valor)
        return True
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Erro", f"Erro na transferência: {e}")
        return False
    finally:
        conn.close()
    
