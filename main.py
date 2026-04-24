import tkinter as tk
import contas as BD


def tela_usuario(nome_usuario, janela_login):
    tela_principal = tk.Toplevel()
    tela_principal.title("Área do Usuário")
    tela_principal.geometry("400x450")
    tela_principal.configure(bg="#f0f0f0")

    def atualizar_saldo():
        saldo = BD.consultar_saldo(nome_usuario)
        label_saldo.config(text=f"Saldo: R$ {saldo:.2f}")

    def fazer_logoff():
        tela_principal.destroy()
        janela_login.deiconify()

    tela_principal.protocol("WM_DELETE_WINDOW", fazer_logoff)

    tk.Label(
        tela_principal,
        text=f"Bem-vindo, {nome_usuario}!",
        font=("Arial", 16, "bold"),
        bg="#f0f0f0"
    ).pack(pady=30)

    label_saldo = tk.Label(
        tela_principal,
        text=f"Saldo: R$ {BD.consultar_saldo(nome_usuario):.2f}",
        font=("Arial", 12),
        bg="#f0f0f0"
    )
    label_saldo.pack(pady=10)

    # --- AÇÕES SIMPLES (EXEMPLO) ---
    def depositar():
        BD.alterar_saldo(nome_usuario, 100)
        atualizar_saldo()

    def sacar():
        BD.alterar_saldo(nome_usuario, -50)
        atualizar_saldo()

    tk.Button(
        tela_principal,
        text="DEPOSITAR +100",
        command=depositar,
        bg="#4CAF50",
        fg="white",
        width=20
    ).pack(pady=5)

    tk.Button(
        tela_principal,
        text="SACAR -50",
        command=sacar,
        bg="#FF9800",
        fg="white",
        width=20
    ).pack(pady=5)

    tk.Button(
        tela_principal,
        text="SAIR / LOGOFF",
        command=fazer_logoff,
        bg="#E53935",
        fg="white",
        width=20
    ).pack(pady=20)
