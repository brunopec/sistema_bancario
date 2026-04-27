import sqlite3 as sql
from tkinter import messagebox

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


# ------------------ SALDO ------------------
def consultar_saldo(usuario):
    conn = sql.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute("SELECT saldo FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()

    conn.close()
    return resultado[0] if resultado else 0.0


# ------------------ DEPOSITAR ------------------
def depositar(usuario, valor):
    if valor <= 0:
        messagebox.showerror("Erro", "Valor inválido!")
        return False

    conn = sql.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE usuarios SET saldo = saldo + ? WHERE usuario = ?",
        (valor, usuario)
    )

    conn.commit()
    conn.close()
    return True


# ------------------ SACAR ------------------
def sacar(usuario, valor):
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
    return True


# ------------------ TRANSFERIR ------------------
def transferir(origem, destino, valor):
    if origem == destino:
        messagebox.showerror("Erro", "Não pode transferir para si mesmo!")
        return False

    if valor <= 0:
        messagebox.showerror("Erro", "Valor inválido!")
        return False

    saldo = consultar_saldo(origem)

    if valor > saldo:
        messagebox.showerror("Erro", "Saldo insuficiente!")
        return False

    conn = sql.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute("SELECT usuario FROM usuarios WHERE usuario = ?", (destino,))
    if not cursor.fetchone():
        messagebox.showerror("Erro", "Usuário destino não existe!")
        conn.close()
        return False

    cursor.execute("UPDATE usuarios SET saldo = saldo - ? WHERE usuario = ?", (valor, origem))
    cursor.execute("UPDATE usuarios SET saldo = saldo + ? WHERE usuario = ?", (valor, destino))

    conn.commit()
    conn.close()
    return True