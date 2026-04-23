import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql
import contas as BD
import main 

BD.criar_banco()

# --- FUNÇÕES ---
def cadastrar_usuario():
    janela.withdraw()
    tela_cadastro = tk.Tk()
    tela_cadastro.title("Sistema Bancário")
    tela_cadastro.geometry("400x450")
    tela_cadastro.configure(bg="#f0f0f0")
    tk.Label(tela_cadastro, text="CADASTRO DE USUÁRIO", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333").pack(pady=30)
    tk.Label(tela_cadastro, text="Usuário:", bg="#f0f0f0", font=("Arial", 10)).pack()
    entry_usuario = tk.Entry(tela_cadastro, font=("Arial", 12))
    entry_usuario.pack(pady=5)
    tk.Label(tela_cadastro, text="Senha:", bg="#f0f0f0", font=("Arial", 10)).pack()
    entry_senha = tk.Entry(tela_cadastro, show="*", font=("Arial", 12))
    entry_senha.pack(pady=5)
    botao_confirmar = tk.Button(tela_cadastro, text="CONFIRMAR", command=lambda: BD.confirmar_cadastro(tela_cadastro, entry_usuario, entry_senha), 
                               bg="#4CAF50", fg="white", width=20, font=("Arial", 10, "bold"))
    botao_confirmar.pack(pady=5)

    def voltar_para_login():
        tela_cadastro.destroy()
        janela.deiconify()
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    if usuario == "" or senha == "":
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return
    tela_cadastro.protocol("WM_DELETE_WINDOW", voltar_para_login)


def realizar_login():
    usuario = entry_usuario.get().strip()
    senha = entry_senha.get().strip()

    conn = sql.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
    user_found = cursor.fetchone() # Busca apenas um resultado
    conn.close()

    if user_found:
        janela.withdraw()
        main.tela_usuario(entry_usuario.get(), janela)

        
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

janela = tk.Tk()
janela.title("Sistema Bancário")
janela.geometry("400x450")
janela.configure(bg="#f0f0f0")

label_titulo = tk.Label(janela, text="SISTEMA BANCÁRIO", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
label_titulo.pack(pady=30)

# Campos de Entrada (Globais para a janela)
tk.Label(janela, text="Usuário:", bg="#f0f0f0", font=("Arial", 10)).pack()
entry_usuario = tk.Entry(janela, font=("Arial", 12))
entry_usuario.pack(pady=5)

tk.Label(janela, text="Senha:", bg="#f0f0f0", font=("Arial", 10)).pack()
entry_senha = tk.Entry(janela, show="*", font=("Arial", 12))
entry_senha.pack(pady=5)

# Botões
botao_entrar = tk.Button(janela, text="ENTRAR", command=realizar_login, 
                         bg="#4CAF50", fg="white", width=20, font=("Arial", 10, "bold"))
botao_entrar.pack(pady=5)

botao_cadastrar = tk.Button(janela, text="CADASTRAR", command=cadastrar_usuario, 
                            bg="#0029E2", fg="white", width=20, font=("Arial", 10, "bold"))
botao_cadastrar.pack(pady=5)

botao_sair = tk.Button(janela, text="Sair do Sistema", command=janela.destroy, 
                       bg="#f44336", fg="white", width=15)
botao_sair.pack(pady=20)

janela.mainloop()
