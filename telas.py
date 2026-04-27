import tkinter as tk
from tkinter import messagebox
import BD_usuario as BD

# ------------------ LOGIN ------------------
def tela_login():
    janela_login = tk.Tk()
    janela_login.title("Sistema Bancário")
    janela_login.geometry("400x450")
    janela_login.configure(bg="#f0f0f0")

    tk.Label(janela_login, text="SISTEMA BANCÁRIO", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=30)

    tk.Label(janela_login, text="Usuário:", bg="#f0f0f0").pack()
    entry_usuario = tk.Entry(janela_login)
    entry_usuario.pack(pady=5)

    tk.Label(janela_login, text="Senha:", bg="#f0f0f0").pack()
    entry_senha = tk.Entry(janela_login, show="*")
    entry_senha.pack(pady=5)

    tk.Button(
        janela_login,
        text="ENTRAR",
        command=lambda: BD.realizar_login(janela_login, tela_usuario, entry_usuario, entry_senha),
        bg="#4CAF50", fg="white", width=20
    ).pack(pady=5)

    tk.Button(
        janela_login,
        text="CADASTRAR",
        command=lambda: tela_cadastro(janela_login),
        bg="#0029E2", fg="white", width=20
    ).pack(pady=5)

    tk.Button(
        janela_login,
        text="SAIR",
        command=janela_login.destroy,
        bg="#f44336", fg="white"
    ).pack(pady=20)

    janela_login.mainloop()


# ------------------ CADASTRO ------------------
def tela_cadastro(janela_login):
    janela_login.withdraw()

    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro de Usuário")
    janela_cadastro.geometry("400x450")
    janela_cadastro.configure(bg="#f0f0f0")

    tk.Label(janela_cadastro, text="CADASTRO DE USUÁRIO", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=30)

    tk.Label(janela_cadastro, text="Nome:", bg="#f0f0f0").pack()
    entry_nome = tk.Entry(janela_cadastro)
    entry_nome.pack(pady=5)

    tk.Label(janela_cadastro, text="Usuário:", bg="#f0f0f0").pack()
    entry_usuario = tk.Entry(janela_cadastro)
    entry_usuario.pack(pady=5)

    tk.Label(janela_cadastro, text="Senha:", bg="#f0f0f0").pack()
    entry_senha = tk.Entry(janela_cadastro, show="*")
    entry_senha.pack(pady=5)

    tk.Button(
        janela_cadastro,
        text="CADASTRAR",
        command=lambda: BD.confirmar_cadastro(janela_cadastro, janela_login, entry_nome, entry_usuario, entry_senha),
        bg="#00E20B"
    ).pack(pady=10)

    tk.Button(
        janela_cadastro,
        text="VOLTAR",
        command=lambda: [janela_cadastro.destroy(), janela_login.deiconify()],
        bg="#f44336", fg="white"
    ).pack(pady=5)


# ------------------ USUÁRIO ------------------
def tela_usuario(usuario, janela_login):
    tela = tk.Toplevel()
    tela.title("Área do Usuário")
    tela.geometry("400x450")
    tela.configure(bg="#f0f0f0")

    def atualizar():
        saldo = BD.consultar_saldo(usuario)
        label_saldo.config(text=f"Saldo: R$ {saldo:.2f}")

    def sair():
        tela.destroy()
        janela_login.deiconify()

    tk.Label(tela, text=f"Bem-vindo!", font=("Arial", 16, "bold")).pack(pady=30)

    label_saldo = tk.Label(tela, text=f"Saldo: R$ {BD.consultar_saldo(usuario):.2f}")
    label_saldo.pack(pady=10)

    tk.Button(tela, text="DEPOSITAR", command=lambda: tela_deposito(usuario, atualizar), bg="#4CAF50", fg="white", width=20).pack(pady=5)
    tk.Button(tela, text="SACAR", command=lambda: tela_saque(usuario, atualizar), bg="#FF9800", fg="white", width=20).pack(pady=5)
    tk.Button(tela, text="TRANSFERIR", command=lambda: tela_transferencia(usuario, atualizar), bg="#2196F3", fg="white", width=20).pack(pady=5)

    tk.Button(tela, text="SAIR", command=sair, bg="#f44336", fg="white", width=20).pack(pady=20)


# ------------------ DEPÓSITO ------------------
def tela_deposito(usuario, atualizar):
    tela = tk.Toplevel()
    tela.title("Depósito")

    tk.Label(tela,
            text="Valor para depósito:"
            ).pack(pady=5)
    entry = tk.Entry(tela)
    entry.pack(pady=10)

    tk.Button(
        tela,
        text="CONFIRMAR",
        bg="#4CAF50", fg="white",
        command=lambda: [BD.depositar(usuario, float(entry.get())), atualizar()]
    ).pack()


# ------------------ SAQUE ------------------
def tela_saque(usuario, atualizar):
    tela = tk.Toplevel()
    tela.title("Saque")

    tk.Label(tela,
            text="Valor para saque:"
            ).pack(pady=5)
    entry = tk.Entry(tela)
    entry.pack(pady=10)

    tk.Button(
        tela,
        text="CONFIRMAR",
        bg="#4CAF50", fg="white",
        command=lambda: [BD.sacar(usuario, float(entry.get())), atualizar()]
    ).pack()


# ------------------ TRANSFERÊNCIA ------------------
def tela_transferencia(usuario, atualizar):
    tela = tk.Toplevel()
    tela.title("Transferência")
    tk.Label(tela,
              text="Usuário destino:"
            ).pack(pady=5)
    entry_destino = tk.Entry(tela)
    entry_destino.pack(pady=5)
    tk.Label(tela,
              text="Valor:"
            ).pack()
    entry_valor = tk.Entry(tela)
    entry_valor.pack(pady=5)

    tk.Button(
        tela,
        text="TRANSFERIR",
        command=lambda: [
            BD.transferir(usuario, entry_destino.get(), float(entry_valor.get())),
            atualizar()
        ]
    ).pack()