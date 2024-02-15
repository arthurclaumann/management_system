import sqlite3
from tkinter import messagebox
from datetime import date

class Backend():
    def conecta_db(self):
        # Criar a conexão com o banco de dados
        self.conn = sqlite3.connect('system_management.db')
        self.cursor = self.conn.cursor()

        # print('Banco de dados conectado.')


    def desconecta_db(self):
        self.conn.close()
        # print('Banco de dados desconectado.')


    def cria_tabela(self):
        self.conecta_db()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    usuario TEXT NOT NULL, 
                    senha TEXT NOT NULL,
                    confirma_senha TEXT NOT NULL
        );
        ''')

        self.conn.commit()
        # print('Tabela criada com sucesso')
        self.desconecta_db()


    def cadastrar_usuario(self, usuario, senha, confirma_senha, limpa_entry_cadastro):
        self.username_cadastro = usuario
        self.senha_cadastro = senha
        self.confirma_senha_cadastro = confirma_senha

        self.conecta_db()
        self.cursor.execute("""INSERT INTO Users (usuario, senha, confirma_senha) VALUES(:usuario, :senha, :confirma_senha)
                            """,{'usuario': self.username_cadastro, 'senha': self.senha_cadastro, 'confirma_senha': self.confirma_senha_cadastro})

        try:
            if(self.username_cadastro =="" or self.senha_cadastro == "" or self.confirma_senha_cadastro == ""):
                messagebox.showerror(title = 'Sistema de Login', message='Preencha todos os campos!')
            elif(len(self.username_cadastro) < 4):
                messagebox.showerror(title = 'Sistema de Login', message = 'O nome de usuário deve conter pelo menos\n4 carácteres.')
            elif(len(self.senha_cadastro) < 4):
                messagebox.showerror(title = 'Sistema de Login', message = 'A senha deve conter pelo menos\n4 carácteres.')
            elif(self.senha_cadastro != self.confirma_senha_cadastro):
                messagebox.showerror(title = 'Sistema de Login', message='As senhas informadas são diferentes!')
            else:
                self.conn.commit()
                messagebox.showinfo(message = 'Cadastro realizado com sucesso.')
                self.desconecta_db()
                limpa_entry_cadastro()
        except:
            messagebox.showerror(title = 'Sistema de Login', message='Erro no processo de cadastramento.')
            self.desconecta_db()


    def cria_tabela_os(self):
        self.conecta_db()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS ordem_servico (
                    os INT NOT NULL,
                    data DATE NOT NULL, 
                    cliente TEXT NOT NULL,
                    carro TEXT NOT NULL,
                    motorista TEXT NOT NULL,
                    servico TEXT NOT NULL,
                    receita FLOAT,
                    cod_receita INT,
                    despesa FLOAT,
                    cod_despesa INT,
                    situacao TEXT NOT NULL DEFAULT 'Pendente'
        );
        ''')

        self.conn.commit()
        # print('Tabela criada com sucesso')
        self.desconecta_db()


    def cadastrar_os_aberta_db(self, os, data, cliente, carro, motorista, servico, situacao):
        self.os = os
        self.data = data
        self.cliente = cliente
        self.carro = carro
        self.motorista = motorista
        self.servico = servico
        # self.valor = valor
        self.situacao = situacao


        self.conecta_db()
        self.cursor.execute("""INSERT INTO ordem_servico (os, data, cliente, carro, motorista, servico, situacao) VALUES(:os, :data, :cliente, :carro, :motorista, :servico, :situacao)
                            """,{'os': self.os, 'data': self.data, 'cliente': self.cliente, 'carro': self.carro, 'motorista': self.motorista, 'servico': self.servico, 'situacao': self.situacao})

        try:
            if(self.os =="" or self.data =="" or self.cliente =="" or self.carro =="" or self.motorista =="" or self.motorista ==''):
                messagebox.showerror(title ='', message='Preencha todos os dados!')
            else:
                self.conn.commit()
                messagebox.showinfo(title='', message = 'Ordem de serviço cadastrada com sucesso.')
                self.desconecta_db()
        except:
            messagebox.showerror(title = '', message='Erro no processo de cadastramento.')
            self.desconecta_db()


    def verifica_login(self, usuario, senha, limpa_entry_login, remove_tela_login, tela_menu):
        self.username_login = usuario
        self.senha_login = senha

        self.conecta_db()

        self.cursor.execute("SELECT * FROM Users WHERE usuario=:usuario AND senha=:senha", {'usuario': usuario, 'senha': senha})

        self.verifica_dados = self.cursor.fetchone()

        try:
            if(self.username_login =="" or self.senha_login == ""):
                messagebox.showerror(title = 'Sistema de Login', message= 'Usuário e/ou senha incompletos.')              

            if(self.username_login in self.verifica_dados and self.senha_login in self.verifica_dados):
                messagebox.showinfo( title = 'Sistena de Login', message='Login realizado com sucesso.')
                self.desconecta_db()
                limpa_entry_login()
                remove_tela_login()
                tela_menu()
        except:
            messagebox.showerror(title = 'Sistema de Login', message= 'Usuário e/ou senha incorretos.')


    def ver_os_aberta_db(self):
        self.conecta_db()
        self.cursor.execute("SELECT * FROM ordem_servico WHERE situacao='Aberta' or situacao='Pendente'")

        try:

            self.verifica_dados = self.cursor.fetchall()

            if self.verifica_dados == '':
                messagebox.showinfo(title = '', message='Nenhuma ordem de serviço aberta')
                self.desconecta_db()
            else:
                self.desconecta_db()
                return self.verifica_dados
        except:
            messagebox.showerror(message='Ainda não há ordem de serviço aberta') 

    def ver_os_fechada_db(self):
        self.conecta_db()

        self.cursor.execute("SELECT * FROM ordem_servico WHERE situacao='Fechada'")

        self.verifica_dados = self.cursor.fetchall()

        if self.verifica_dados == '':
            messagebox.showinfo(title = '', message='Nenhuma ordem de serviço fechada')
            self.desconecta_db()
        else:
            self.desconecta_db()
            return self.verifica_dados
            

    def filtro_db_os(self, coluna, valor, situacao):
        try:
            self.conecta_db()

            self.cursor.execute(f"SELECT * FROM ordem_servico WHERE {coluna}=:valor AND situacao =:situacao", {'valor': valor, 'situacao': situacao})

            self.verifica_dados = self.cursor.fetchall()

            if not self.verifica_dados:
                messagebox.showinfo(title='', message='Nenhuma ordem de serviço encontrada')
                return None
            else:
                return self.verifica_dados
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.desconecta_db()
        
        