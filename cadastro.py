import customtkinter as ctk
from tkinter import * 
from tkinter import messagebox
from CTkTable import *
import datetime
from validate_docbr import CPF, CNPJ
from datetime import datetime


class Cadastro():
    def __init__(self, master, menu, backend):
        self.master = master
        self.menu = menu
        self.backend = backend
        self.backend.cria_tabela_veiculos()
        self.backend.cria_tabela_clientes()
        self.backend.cria_tabela_motoristas()


    def tela_cadastro(self):
        self.menu.limpa_menu()
        
        # Frame do menu de cadastro
        self.frame_menu_cadastro = ctk.CTkFrame(self.master, width = 400, height = 500)
        self.frame_menu_cadastro.grid_columnconfigure(0, weight=1)
        self.frame_menu_cadastro.grid(row = 0,  column = 0, pady = 30)

        # título
        self.lbtitle = ctk.CTkLabel(master = self.frame_menu_cadastro, text = 'Menu de cadastros', font = ('Roboto', 18))
        self.lbtitle.grid(row = 0, column = 0, padx = 10, pady = 10)     


        # Botões de opções
        # Veículo
        self.btn_cadastro_veiculo = ctk.CTkButton(master = self.frame_menu_cadastro, text= 'Cadastrar veículo', width = 300, font=('Roboto', 14), corner_radius= 20, command = self.tela_cadastro_veiculo)                           
        self.btn_cadastro_veiculo.grid(row = 1, column = 0, padx = 10, pady = 10)

        # Cliente
        self.btn_cadastro_cliente = ctk.CTkButton(master = self.frame_menu_cadastro, text= 'Cadastrar cliente', width = 300, font=('Roboto', 14), corner_radius= 20, command = self.tela_cadastro_cliente)                           
        self.btn_cadastro_cliente.grid(row = 2, column = 0, padx = 10, pady = 10)
        

        # Motorista
        self.btn_cadastro_motorista = ctk.CTkButton(master = self.frame_menu_cadastro, text= 'Cadastrar motorista', width = 300, font=('Roboto', 14), corner_radius= 20, command = self.tela_cadastro_motorista)                           
        self.btn_cadastro_motorista.grid(row = 3, column = 0, padx = 10, pady = 10)


        # Voltar
        self.btn_voltar = ctk.CTkButton(master = self.frame_menu_cadastro, text= 'Voltar', width = 150, font=('Roboto', 14), corner_radius= 20, command= lambda: (self.voltar_tela(self.frame_menu_cadastro, self.menu.tela_menu)), fg_color= 'green')                           
        self.btn_voltar.grid(row = 4, column = 0, padx = 10, pady = 10)
        

    def tela_cadastro_veiculo(self):
        self.remove_tela_cadastro()

        # frame cadastro de veículo
        self.frame_cadastro_veiculo = ctk.CTkFrame(self.master, width = 400, height = 500)
        # self.frame_cadastro_veiculo.grid_columnconfigure(0, weight=1)
        self.frame_cadastro_veiculo.grid(row = 0,  column = 0, pady = 30, columnspan = 4)
        # Configuração das colunas para que elas se expandam igualmente
        for i in range(5):
            self.frame_cadastro_veiculo.grid_columnconfigure(i, weight=1)

        self.lbtitle = ctk.CTkLabel(master = self.frame_cadastro_veiculo, text = 'Cadastrar novo veículo', font = ('Roboto', 18))
        self.lbtitle.grid(row = 0,  padx = 0, pady = 10, sticky = 'nswe', columnspan = 4)      

        # Modelo
        self.lbtitle = ctk.CTkLabel(master = self.frame_cadastro_veiculo, text = 'Modelo:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 1, column = 0, padx = 0, pady = 10)   

        self.modelo_veiculo_entry = ctk.CTkEntry(master = self.frame_cadastro_veiculo, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.modelo_veiculo_entry.grid(row = 1, column = 1, padx = 10, pady = 10) 

        # Placa
        self.lbtitle = ctk.CTkLabel(master = self.frame_cadastro_veiculo, text = 'Placa:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 2, column = 0, padx = 0, pady = 10)   

        self.placa_veiculo_entry = ctk.CTkEntry(master = self.frame_cadastro_veiculo, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.placa_veiculo_entry.grid(row = 2, column = 1, padx = 10, pady = 10)   

        # ano
        self.lbtitle = ctk.CTkLabel(master = self.frame_cadastro_veiculo, text = 'Ano:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 3, column = 0, padx = 0, pady = 10)   

        self.ano_veiculo_entry = ctk.CTkEntry(master = self.frame_cadastro_veiculo, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.ano_veiculo_entry.grid(row = 3, column = 1, padx = 10, pady = 10)   


        # cadastrar
        self.btn_cadastrar = ctk.CTkButton(master =self.frame_cadastro_veiculo, text= 'Cadastrar', width = 125, font=('Roboto', 12), corner_radius= 20, fg_color = 'gray', command = lambda: self.cadastrar_veiculo(self.modelo_veiculo_entry, self.placa_veiculo_entry, self.placa_veiculo_entry))                       
        self.btn_cadastrar.grid(row = 4, column = 1, padx = 10, pady = 10)       


        # voltar
        self.btn_voltar = ctk.CTkButton(master =self.frame_cadastro_veiculo, text= 'Voltar', width = 85, font=('Roboto', 12), corner_radius= 20, command = lambda: self.voltar_tela(self.frame_cadastro_veiculo, self.tela_cadastro), fg_color = 'green')                       
        self.btn_voltar.grid(row = 5, column = 1, padx = 10, pady = 10)       


    def cadastrar_veiculo(self, modelo, placa, ano):
        modelo = (modelo.get()).upper()
        placa = (placa.get()).upper()
        ano = (ano.get())

        # Adicionar placa+modelo junto no database
        placa_veiculo =  placa + ' ' + modelo
        placa_veiculo = placa_veiculo.strip()

        if(modelo == '' or placa == ''):
            messagebox.showerror(message='Preencha o modelo e a placa.')
        else:
            self.backend.cadastrar_veiculo_db(modelo, placa, ano, placa_veiculo)


    def tela_cadastro_cliente(self):
        # frame cadastro de cliente
        self.frame_cadastro_cliente = ctk.CTkFrame(self.master, width = 400, height = 500)
        # self.frame_cadastro_cliente.grid_columnconfigure(0, weight=1)
        self.frame_cadastro_cliente.grid(row = 0,  column = 0, pady = 30, columnspan = 4)
        # Configuração das colunas para que elas se expandam igualmente
        for i in range(5):
            self.frame_cadastro_cliente.grid_columnconfigure(i, weight=1)

        self.lbtitle = ctk.CTkLabel(master = self.frame_cadastro_cliente, text = 'Cadastrar novo cliente', font = ('Roboto', 18))
        self.lbtitle.grid(row = 0,  padx = 0, pady = 10, sticky = 'nswe', columnspan = 4)      

        # Nome cliente
        self.lbtitle = ctk.CTkLabel(master = self.frame_cadastro_cliente, text = 'Nome cliente:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 1, column = 0, padx = 0, pady = 10)   

        self.nome_cliente_entry = ctk.CTkEntry(master = self.frame_cadastro_cliente, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.nome_cliente_entry.grid(row = 1, column = 1, padx = 10, pady = 10) 

        # SelectBox
        self.lbtitle = ctk.CTkLabel(master = self.frame_cadastro_cliente, text = 'Tipo:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 2, column = 0, padx = 0, pady = 10)   


        self.cpf_cnpj_option = ctk.CTkComboBox(master=self.frame_cadastro_cliente, values=["CPF", "CNPJ"], width=250, font=('Roboto', 12), corner_radius=12)
        self.cpf_cnpj_option.grid(row = 2, column = 1, padx = 10, pady = 10) 

        # CPF/CNPJ
        self.lbtitle = ctk.CTkLabel(master = self.frame_cadastro_cliente, text = 'CPF/CNPJ:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 3, column = 0, padx = 0, pady = 10)   

        self.cpf_cnpj_entry = ctk.CTkEntry(master = self.frame_cadastro_cliente, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.cpf_cnpj_entry.grid(row = 3, column = 1, padx = 10, pady = 10)   

        # Cidade
        self.lbtitle = ctk.CTkLabel(master = self.frame_cadastro_cliente, text = 'Cidade:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 4, column = 0, padx = 0, pady = 10)   

        self.cidade_cliente_entry = ctk.CTkEntry(master = self.frame_cadastro_cliente, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.cidade_cliente_entry.grid(row = 4, column = 1, padx = 10, pady = 10)   

        # Estado
        self.lbtitle = ctk.CTkLabel(master = self.frame_cadastro_cliente, text = 'UF:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 5, column = 0, padx = 0, pady = 10)   

        self.uf_cliente_entry = ctk.CTkEntry(master = self.frame_cadastro_cliente, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.uf_cliente_entry.grid(row = 5, column = 1, padx = 10, pady = 10)   


        # cadastrar
        self.btn_cadastrar = ctk.CTkButton(master =self.frame_cadastro_cliente, text= 'Cadastrar', width = 125, font=('Roboto', 12), corner_radius= 20, fg_color = 'gray', command= lambda: self.cadastrar_cliente(self.nome_cliente_entry, self.cpf_cnpj_entry, self.cidade_cliente_entry, self.uf_cliente_entry, self.cpf_cnpj_option))                       
        self.btn_cadastrar.grid(row = 6, column = 1, padx = 10, pady = 10)       


        # voltar
        self.btn_voltar = ctk.CTkButton(master =self.frame_cadastro_cliente, text= 'Voltar', width = 85, font=('Roboto', 12), corner_radius= 20, command = lambda: self.voltar_tela(self.frame_cadastro_cliente, self.tela_cadastro), fg_color = 'green')                       
        self.btn_voltar.grid(row = 7, column = 1, padx = 10, pady = 10)              


    def cadastrar_cliente(self, nome, cpf_cnpj, cidade, uf, tipo):
        # Validar nome - CPF/CNPJ
        nome = nome.get().title().strip()
        cpf_cnpj = (cpf_cnpj.get())
        cidade = (cidade.get()).title().strip()
        uf = (uf.get()).upper().strip()
        cpf_cnpj_option = tipo.get().strip()


        if(nome == '' or cpf_cnpj == ''):
            messagebox.showerror(message='Preencha o nome e CPF/CNPJ.')
        else:
            if cpf_cnpj_option == 'CPF':
                cpf_cnpj = self.valida_cpf(cpf_cnpj)  
                print(cpf_cnpj)          
            else: 
                cpf_cnpj = self.valida_cnpj(cpf_cnpj)
                print(cpf_cnpj)   

            if cpf_cnpj is not None:  # Verifica se o CPF/CNPJ é válido
                self.backend.cadastrar_cliente_db(nome, cpf_cnpj_option, cpf_cnpj, cidade, uf)
            else:
                messagebox.showerror(message='CPF/CNPJ inválido.')           # self.backend.cadastrar_cliente_db(nome, cpf_cnpj_option, cpf_cnpj, cidade, uf)
        

    def valida_cpf(self, documento):
        documento = str(documento)
        validador = CPF()
        if validador.validate(documento):
            documento = validador.mask(documento)
            return documento
        else:
            return None


    def valida_cnpj(self, documento):
        documento = str(documento)
        cnpj_validacao = CNPJ()
        if cnpj_validacao.validate(documento):
            documento = cnpj_validacao.mask(documento)
            return documento
        else:
            return None
    

    def tela_cadastro_motorista(self):
        # frame cadastro de cliente
        self.frame_cadastro_motorista = ctk.CTkFrame(self.master, width = 400, height = 500)
        # self.frame_cadastro_cliente.grid_columnconfigure(0, weight=1)
        self.frame_cadastro_motorista.grid(row = 0,  column = 0, pady = 30, columnspan = 4)
        # Configuração das colunas para que elas se expandam igualmente
        for i in range(5):
            self.frame_cadastro_motorista.grid_columnconfigure(i, weight=1)

        self.lbtitle = ctk.CTkLabel(master = self.frame_cadastro_motorista, text = 'Cadastrar novo motorista', font = ('Roboto', 18))
        self.lbtitle.grid(row = 0,  padx = 0, pady = 10, sticky = 'nswe', columnspan = 4)      

        # Nome motorista
        self.lbtitle = ctk.CTkLabel(master = self.frame_cadastro_motorista, text = 'Nome:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 1, column = 0, padx = 0, pady = 10)   

        self.nome_motorista_entry = ctk.CTkEntry(master = self.frame_cadastro_motorista, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.nome_motorista_entry.grid(row = 1, column = 1, padx = 10, pady = 10) 

        # CPF
        self.lbtitle = ctk.CTkLabel(master = self.frame_cadastro_motorista, text = 'CPF:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 2, column = 0, padx = 0, pady = 10)   

        self.cpf_motorista_entry = ctk.CTkEntry(master = self.frame_cadastro_motorista, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.cpf_motorista_entry.grid(row = 2, column = 1, padx = 10, pady = 10)   

        # Data de ingresso
        self.lbtitle = ctk.CTkLabel(master = self.frame_cadastro_motorista, text = 'Data de ingresso:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 3, column = 0, padx = 0, pady = 10)   

        self.data_ingresso_motorista_entry = ctk.CTkEntry(master = self.frame_cadastro_motorista, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.data_ingresso_motorista_entry.grid(row = 3, column = 1, padx = 10, pady = 10)   


        # cadastrar
        self.btn_cadastrar = ctk.CTkButton(master =self.frame_cadastro_motorista, text= 'Cadastrar', width = 125, font=('Roboto', 12), corner_radius= 20, fg_color = 'gray', command = lambda: self.cadastrar_motorista(self.nome_motorista_entry, self.cpf_motorista_entry, self.data_ingresso_motorista_entry))                       
        self.btn_cadastrar.grid(row = 5, column = 1, padx = 10, pady = 10)       


        # voltar
        self.btn_voltar = ctk.CTkButton(master =self.frame_cadastro_motorista, text= 'Voltar', width = 85, font=('Roboto', 12), corner_radius= 20, command = lambda: self.voltar_tela(self.frame_cadastro_motorista, self.tela_cadastro), fg_color = 'green')                       
        self.btn_voltar.grid(row = 6, column = 1, padx = 10, pady = 10)       
        pass


    def cadastrar_motorista(self, nome, cpf, data):
        # Validar nome - CPF/CNPJ
        nome = nome.get().title().strip()
        cpf = (cpf.get())
        data = data.get().strip()

        if(nome == '' or cpf == ''):
            messagebox.showerror(message='Preencha o nome e CPF.')
        else: 
            if self.validar_data(data):
                cpf = self.valida_cpf(cpf)

                if cpf is not None:  # Verifica se o CPF/CNPJ é válido
                    self.backend.cadastrar_motorista_db(nome, cpf, data)
                else:
                    messagebox.showerror(message='CPF inválido.')
            else:
                messagebox.showerror(message='Formato de data incorreto. Ex: dd/mm/yyyy.')
            # print(nome, cpf, data)
        
        
    def validar_data(self, data_texto):
        formato = '%d/%m/%Y'
        try:
            datetime.strptime(data_texto, formato)
            return True
        except ValueError:
            return False


    def voltar_tela(self, frame_atual, frame_anterior):
        frame_atual.grid_remove()
        frame_anterior()  # Assuming you're going back to the menu screen, adjust as needed
        # Remove the previous "Voltar" button if it exists

    
    def remove_tela_cadastro(self):
        self.frame_menu_cadastro.grid_remove()