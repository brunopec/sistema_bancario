from banco import Banco
from operacoes_bancarias import conta_funcionalidades
def main():
    banco = Banco()

    while True:
        print("\n1. Criar conta\n2. Acessar conta\n3. Sair")
        escolha = input("Escolha: ")

        if escolha == '1':
            nome = input("Nome: ")
            usuario = input("Usuário: ")
            senha = input("Senha: ")
            if banco.criar_conta(nome, usuario, senha):
                print("Conta criada!")
            else:
                print("Usuário já existe.")

        elif escolha == '2':
            usuario = input("Usuário: ")
            senha = input("Senha: ")
            conta = banco.acessar_conta(usuario, senha)

            if conta:
                print(f"Bem-vindo, {conta.nome}")
                conta_funcionalidades(conta)
            else:
                print("Login inválido.")

        elif escolha == '3':
            break

if __name__ == "__main__":
    main()
