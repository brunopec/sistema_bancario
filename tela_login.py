import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql
import contas as BD
import main

BD.criar_banco()


def cadastrar_usuario():
    janela.withdraw()

    tela_cadastro = tk.Toplevel()
    tela_cadastro.title("Cadastro")
    tela_cadastro.geometry("400x450")
    tela_cadastro.configure(bg="#f0f0f0")

    tk.Label(
        tela_cadastro,
        text="CADASTRO DE USUÁRIO",
        font=("Arial", 18, "bold"),
        bg="#f0f0f0"
    ).pack(pady=30)

    tk.Label(tela_cadastro, text="Usuário:", bg="#f0f0f0").pack()
    entry_usuario = tk.Entry(tela_cadastro)
    entry_usuario.pack(pady=5)

    tk.Label(tela_cadastro, text="Senha:", bg="#f0f0f0").pack()
    entry_senha = tk.Entry(tela_cadastro, show="*")
    entry_senha.pack(pady=5)

    tk.Button(
        tela_cadastro,
        text="CONFIRMAR",
        command=lambda: BD.confirmar_cadastro(
            tela_cadastro, janela, entry_usuario, entry_senha
        ),
        bg="#4CAF50",
        fg="white",
        width=20
    ).pack(pady=10)

    def voltar():
        tela_cadastro.destroy()
        janela.deiconify()

    tela_cadastro.protocol("WM_DELETE_WINDOW", voltar)


def realizar_login():
    usuario = entry_usuario.get().strip()
    senha = entry_senha.get().strip()

    conn = sql.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?",
        (usuario, senha)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        janela.withdraw()
        main.tela_usuario(usuario, janela)
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")


# --- TELA PRINCIPAL ---
janela = tk.Tk()
janela.title("Sistema Bancário")
janela.geometry("400x450")
janela.configure(bg="#f0f0f0")

tk.Label(
    janela,
    text="SISTEMA BANCÁRIO",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0"
).pack(pady=30)

tk.Label(janela, text="Usuário:", bg="#f0f0f0").pack()
entry_usuario = tk.Entry(janela)
entry_usuario.pack(pady=5)

tk.Label(janela, text="Senha:", bg="#f0f0f0").pack()
entry_senha = tk.Entry(janela, show="*")
entry_senha.pack(pady=5)

tk.Button(
    janela,
    text="ENTRAR",
    command=realizar_login,
    bg="#4CAF50",
    fg="white",
    width=20
).pack(pady=5)

tk.Button(
    janela,
    text="CADASTRAR",
    command=cadastrar_usuario,
    bg="#0029E2",
    fg="white",
    width=20
).pack(pady=5)

tk.Button(
    janela,
    text="SAIR",
    command=janela.destroy,
    bg="#f44336",
    fg="white"
).pack(pady=20)

janela.mainloop()
