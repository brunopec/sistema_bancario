import sqlite3 as connector

# Função auxiliar para garantir que a tabela exista e evitar erros de "Table not found"
def inicializar_banco():
    conexao = connector.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS saldo (
            usuario TEXT PRIMARY KEY,
            saldo REAL DEFAULT 0.0
        )
    ''')
    conexao.commit()
    conexao.close()

# ------------------ VER SALDO ------------------
def ver_saldo(conta):
    try:
        conexao = connector.connect('banco.db')
        cursor = conexao.cursor()

        cursor.execute('SELECT saldo FROM saldo WHERE usuario = ?', (conta.usuario,))
        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]
        else:
            # Se o usuário não tem linha no saldo, cria com 0
            cursor.execute('INSERT INTO saldo (usuario, saldo) VALUES (?, ?)', (conta.usuario, 0.0))
            conexao.commit()
            return 0.0
    except Exception as e:
        print(f"Erro ao buscar saldo: {e}")
        return 0.0
    finally:
        conexao.close()

# ------------------ DEPOSITAR ------------------
def depositar(conta, valor):
    if valor <= 0:
        print("Valor inválido para depósito.")
        return False
    try:
        conexao = connector.connect('banco.db')
        cursor = conexao.cursor()

        # Tenta atualizar. Se não existir (rowcount == 0), insere.
        cursor.execute('UPDATE saldo SET saldo = saldo + ? WHERE usuario = ?', (valor, conta.usuario))
        
        if cursor.rowcount == 0:
            cursor.execute('INSERT INTO saldo (usuario, saldo) VALUES (?, ?)', (conta.usuario, valor))

        conexao.commit()
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        return True
    except Exception as e:
        print("Erro no depósito:", e)
        return False
    finally:
        conexao.close()

# ------------------ SACAR ------------------
def sacar(conta, valor):
    saldo_atual = ver_saldo(conta)

    if valor <= 0:
        print("Valor inválido.")
    elif valor <= saldo_atual:
        try:
            conexao = connector.connect('banco.db')
            cursor = conexao.cursor()
            cursor.execute('UPDATE saldo SET saldo = saldo - ? WHERE usuario = ?', (valor, conta.usuario))
            conexao.commit()
            print(f"Saque de R${valor:.2f} realizado.")
        except Exception as e:
            print("Erro no saque:", e)
        finally:
            conexao.close()
    else:
        print(f"Saldo insuficiente. Seu saldo é R${saldo_atual:.2f}")

# ------------------ TRANSFERIR ------------------
def transferir(conta):
    try:
        conexao = connector.connect('banco.db')
        cursor = conexao.cursor()

        # Lista usuários destinos existentes na tabela saldo
        cursor.execute('SELECT usuario FROM contas WHERE usuario != ?', (conta.usuario,))
        usuarios = cursor.fetchall()

        if not usuarios:
            print("Nenhum outro usuário encontrado no sistema.")
            return

        print("\nDestinos disponíveis:")
        for u in usuarios: print(f"- {u[0]}")

        destino = input("Usuário destino: ")
        valor = float(input("Valor da transferência: "))

        saldo_origem = ver_saldo(conta)

        if valor > saldo_origem:
            print("Saldo insuficiente.")
            return

        # Verifica se destino existe
        cursor.execute('SELECT usuario FROM saldo WHERE usuario = ?', (destino,))
        if cursor.fetchone():
            # Operação Atômica (ou faz tudo ou não faz nada)
            cursor.execute('UPDATE saldo SET saldo = saldo - ? WHERE usuario = ?', (valor, conta.usuario))
            cursor.execute('UPDATE saldo SET saldo = saldo + ? WHERE usuario = ?', (valor, destino))
            conexao.commit()
            print("Transferência concluída!")
        else:
            print("Usuário destino não existe.")

    except ValueError:
        print("Digite um valor numérico válido.")
    except Exception as e:
        print("Erro na transferência:", e)
    finally:
        conexao.close()

# ------------------ MENU ------------------
def conta_funcionalidades(conta):
    inicializar_banco() # Garante que a tabela existe ao iniciar
    while True:
        print(f"\n--- Menu (Usuário: {conta.usuario}) ---")
        print("1. Ver saldo\n2. Depositar\n3. Sacar\n4. Transferir\n5. Logout")
        
        escolha = input("Escolha: ")

        if escolha == '1':
            s = ver_saldo(conta)
            print(f"Saldo Atual: R${s:.2f}")
        elif escolha == '2':
            v = float(input("Valor: "))
            depositar(conta, v)
        elif escolha == '3':
            v = float(input("Valor: "))
            sacar(conta, v)
        elif escolha == '4':
            transferir(conta)
        elif escolha == '5':
            break
        else:
            print("Opção inválida.")