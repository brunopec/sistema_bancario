import sqlite3 as sql
from tkinter import messagebox

def criar_banco():
    connection = sql.connect('usuarios.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            usuario TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            saldo REAL DEFAULT 0.0
        )
    ''')

    connection.commit()
    connection.close()


def confirmar_cadastro(janela_cadastro, janela_login, campo_usuario, campo_senha):
    usuario = campo_usuario.get().strip()
    senha = campo_senha.get().strip()

    if not usuario or not senha:
        messagebox.showwarning("Atenção", "Preencha todos os campos!", parent=janela_cadastro)
        return

    conn = sql.connect('usuarios.db')
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO usuarios (usuario, senha) VALUES (?, ?)",
            (usuario, senha)
        )
        conn.commit()

        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")

        janela_cadastro.destroy()
        janela_login.deiconify()

    except sql.IntegrityError:
        messagebox.showerror("Erro", "Este usuário já existe!", parent=janela_cadastro)

    finally:
        conn.close()


def consultar_saldo(nome_usuario):
    conn = sql.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT saldo FROM usuarios WHERE usuario = ?",
        (nome_usuario,)
    )

    resultado = cursor.fetchone()
    conn.close()

    return resultado[0] if resultado else 0.0
