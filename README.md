# 🏦 Sistema Bancário com Interface Gráfica (Tkinter)

Este projeto é um sistema bancário simples desenvolvido em **Python**, com interface gráfica utilizando **Tkinter** e persistência de dados com **SQLite**.

O sistema permite o gerenciamento básico de usuários e operações financeiras, sendo ideal como projeto de estudo e portfólio para iniciantes em desenvolvimento de software.

---

## 🚀 Funcionalidades

* 👤 Cadastro de usuários
* 🔐 Login com validação de credenciais
* 💰 Consulta de saldo
* ➕ Depósito
* ➖ Saque com validação de saldo
* 🔄 Transferência entre usuários
* 🚪 Logoff e controle de sessões

---

## 🧱 Estrutura do Projeto

```
📁 projeto/
│
├── main.py                # Arquivo principal (inicialização do sistema)
├── telas.py              # Interface gráfica (Tkinter)
├── BD_usuario.py         # Manipulação do banco de dados (SQLite)
├── conta.py              # Classe Conta (POO - modelo do usuário)
├── banco.db              # Banco de dados (criado automaticamente)
```

---

## 🛠️ Tecnologias Utilizadas

* Python 3.x
* Tkinter (interface gráfica)
* SQLite3 (banco de dados local)

---

## ▶️ Como Executar

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse a pasta do projeto:

```
cd seu-repositorio
```

3. Execute o sistema:

```
python main.py
```

---

## 💡 Como o Sistema Funciona

* O banco de dados é criado automaticamente na primeira execução

* Cada usuário possui:

  * Nome
  * Usuário (login único)
  * Senha
  * Saldo inicial (R$ 0,00)

* As operações financeiras atualizam diretamente o saldo no banco

---

## ⚠️ Validações Implementadas

* Não permite cadastro com campos vazios
* Não permite usuários duplicados
* Impede saque com saldo insuficiente
* Impede transferência para usuário inexistente
* Não permite valores negativos

---

## 📚 Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

* Praticar lógica de programação
* Aprender manipulação de banco de dados (SQLite)
* Desenvolver interfaces gráficas com Tkinter
* Aplicar conceitos básicos de organização de código

---

## 🔮 Possíveis Melhorias

* Histórico de transações
* Criptografia de senha
* Interface mais moderna (ex: CustomTkinter)
* Sistema de múltiplas contas
* Integração com APIs externas
* Arquitetura em camadas (MVC)

---

## 👨‍💻 Autor

Projeto desenvolvido por **Bruno Luan Pecorari Britez**

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais.
