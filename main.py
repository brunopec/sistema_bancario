from ast import main
import tkinter as tk
import contas as BD

def tela_usuario(nome_usuario, janela_login): 
    tela_principal = tk.Toplevel()
    tela_principal.title("Área do Usuário")
    tela_principal.geometry("400x450")
    tela_principal.configure(bg="#f0f0f0")

    
    def fazer_logoff(nome_usuario, janela_login):
        tela_principal.destroy()      
        janela_login.deiconify()      

    
    tela_principal.protocol("WM_DELETE_WINDOW", lambda: fazer_logoff(nome_usuario, janela_login))

    tk.Label(tela_principal, text=f"Bem-vindo, {nome_usuario}!", 
             font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=30)
    saldo_usuario = tk.Label(tela_principal, text=f"Saldo: R$: {BD.consultar_saldo(nome_usuario):.2f}", font=("Arial", 12), bg="#f0f0f0")
    saldo_usuario.pack(pady=10)

    botao_depositar = tk.Button(tela_principal, text="DEPOSITAR", command=lambda: main.tela_deposito(nome_usuario, tela_principal),
                               bg="#4CAF50", fg="white", width=20, font=("Arial",   10, "bold"))
    botao_depositar.pack(pady=5)
    botao_sacar = tk.Button(tela_principal, text="SACAR", command=lambda: main.tela_saque(nome_usuario, tela_principal),
                            bg="#FF9800", fg="white", width=20, font=("Arial", 10, "bold"))
    botao_sacar.pack(pady=5)
    botao_transferir = tk.Button(tela_principal, text="TRANSFERIR", command=lambda: main.tela_transferencia(nome_usuario, tela_principal),
                                bg="#2196F3", fg="white", width=20, font=("Arial", 10, "bold"))
    botao_transferir.pack(pady=5)   

    # Botão SAIR agora chama o logoff
    botao_sair = tk.Button(tela_principal, text="SAIR/LOGOFF", command=lambda: fazer_logoff(nome_usuario, janela_login),
                           bg="#E53935", fg="white", width=20, font=("Arial", 10, "bold"))
    botao_sair.pack(pady=20)
