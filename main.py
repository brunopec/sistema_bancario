from BD_usuario import BD_usuario as BD
from conta import Conta
from operacoes_bancarias import conta_funcionalidades


def main():
    
    while True:
        print("\n1. Criar conta\n2. Acessar conta\n3. Sair")
        escolha = input("Escolha: ")

        if escolha == '1':
            nome = input("Nome: ")
            usuario = input("Usuário: ")
            senha = input("Senha: ")
            conta = Conta(nome, usuario, senha)
            if BD.cadastrar_usuario(conta):
                print("Conta criada!")
            else:
                print("Usuário já existe.")

        elif escolha == '2':
            usuario = input("Usuário: ")
            senha = input("Senha: ")
            autenth = BD.auth(usuario, senha)
            if autenth:
                print(f"Bem-vindo, {autenth[0][0]}!")
                conta = Conta(autenth[0][0], usuario, senha)
                conta_funcionalidades(conta)
            else:
                print("Login inválido.")

        elif escolha == '3':
            break

if __name__ == "__main__":
    main()
