import customtkinter as ctk
from tkinter import * 
from tkinter import messagebox
from CTkTable import *

# class Utilidades():
#     def __init__(self, master, menu, backend):
#         self.master = master
#         self.menu = menu
#         self.backend = backend


class OS():
    def __init__(self, master, menu, backend):
        self.master = master
        self.menu = menu
        self.backend = backend

    def tela_os(self):
        self.menu.limpa_menu()
        ### self.frame_os
        self.frame_os = ctk.CTkFrame(self.master, width = 400, height = 500)
        self.frame_os.place(x = 400, y = 30)

        # frame_os widgets
        self.lbtitle = ctk.CTkLabel(master = self.frame_os, text = 'Ordem de Serviço', font = ('Roboto', 14))
        self.lbtitle.grid(row = 0, column = 0, padx = 10, pady = 10)      


        ### Criando as opções das OS
        # Botão os
        self.btn_os = ctk.CTkButton(master = self.frame_os, text= 'Criar ordem de serviço', width = 300, font=('Roboto', 12), corner_radius= 20, command = self.cria_os)                           
        self.btn_os.grid(row = 2, column = 0, padx = 10, pady = 10)

        # Botão os_aberta
        self.btn_os_aberta = ctk.CTkButton(master = self.frame_os, text= 'Ordens de serviço abertas', width = 300, font=('Roboto', 14), corner_radius= 20, command= self.ver_os_aberta)                             
        self.btn_os_aberta.grid(row = 5, column = 0, padx = 10, pady = 10)
     
        # Botão os_fechada
        self.btn_os_fechada = ctk.CTkButton(master = self.frame_os, text= 'Ordens de serviço fechadas', width = 300, font=('Roboto', 14), corner_radius= 20, command = self.ver_os_fechada)                             
        self.btn_os_fechada.grid(row = 7, column = 0, padx = 10, pady = 10)

        # # Botão fechar_os
        # self.btn_fechar_os = ctk.CTkButton(master = self.frame_os, text= 'Fechar OS', width = 200, font=('Roboto', 14), corner_radius= 20, fg_color = 'green')                             
        # self.btn_fechar_os.grid(row = 6, column = 0, padx = 10, pady = 10)


        # Botão relatorio_por_carro
        self.btn_relatorio_carro = ctk.CTkButton(master = self.frame_os, text= 'Relatório por carros', width = 300, font=('Roboto', 14), corner_radius= 20)                         
        self.btn_relatorio_carro.grid(row = 8, column = 0, padx = 10, pady = 10)

        # Botão voltar
        self.btn_voltar = ctk.CTkButton(master = self.frame_os, text= 'Voltar', width = 150, font=('Roboto', 14), corner_radius= 20, command = self.voltar_menu, fg_color='green')                       
        self.btn_voltar.grid(row = 10, column = 0, padx = 5, pady = 10)


    def cria_os(self):
        self.remover_tela_os()

        ### self.frame_cria_os
        self.frame_cria_os = ctk.CTkFrame(self.master, width = 550, height = 600)
        self.frame_cria_os.place(x = 400, y = 30)

        # Número OS
        self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'N. ordem de serviço', font = ('Roboto', 14))
        self.lbtitle.grid(row = 0, column = 0, padx = 0, pady = 10)

        self.numero_os_entry = ctk.CTkEntry(master = self.frame_cria_os, placeholder_text= '', width = 125, font=('Roboto', 12),corner_radius=15)
        self.numero_os_entry.grid(row = 0, column = 1, padx = 0, pady = 10)

        # # Data
        # self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'Data', font = ('Roboto', 14))
        # self.lbtitle.grid(row = 0, column = 2, padx = 0, pady = 10)

        # self.date_os_entry = ctk.CTkEntry(master = self.frame_cria_os, placeholder_text= '', width = 175, font=('Roboto', 12),corner_radius=15)
        # self.date_os_entry.grid(row = 0, column = 3, padx = 1, pady = 10)

        # Cliente
        self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'Cliente', font = ('Roboto', 14))
        self.lbtitle.grid(row = 1, column = 0, padx = 5, pady = 10)

        self.cliente_os_entry = ctk.CTkEntry(master = self.frame_cria_os, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.cliente_os_entry.grid(row = 1, column = 1, padx = 5, pady = 10)


        # Veículo
        self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'Veiculo', font = ('Roboto', 14))
        self.lbtitle.grid(row = 3, column = 0, padx = 5, pady = 5)
        
        self.veiculo_os_entry = ctk.CTkComboBox(master=self.frame_cria_os, justify = 'center',values=["PLD-8032 TOYOTA COROLLA", "EZY 4G48 SPRINTER MARTM5"], width=250, font=('Roboto', 12), corner_radius=12)
        # self.veiculo_os_entry = ctk.CTkEntry(master = self.frame_cria_os, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.veiculo_os_entry.grid(row = 3, column = 1, padx = 5, pady = 5)

        # Motorista --- Criar função para obter motoristas do db
        self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'Motorista', font = ('Roboto', 14))
        self.lbtitle.grid(row = 4, column = 0, padx = 5, pady = 5)

        self.motorista_os_entry = ctk.CTkEntry(master = self.frame_cria_os, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.motorista_os_entry.grid(row = 4, column = 1, padx = 5, pady = 5)

        # Serviço
        self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'Serviço', font = ('Roboto', 14))
        self.lbtitle.grid(row = 5, column = 0, padx = 5, pady = 5)
  
        self.servico_os_entry = ctk.CTkEntry(master = self.frame_cria_os, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.servico_os_entry.grid(row = 5, column = 1, padx = 5, pady = 5)

        # Valor OS
        self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'Valor', font = ('Roboto', 14))
        self.lbtitle.grid(row = 6, column = 0, padx = 5, pady = 5)
  
        self.valor_os_entry = ctk.CTkEntry(master = self.frame_cria_os, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.valor_os_entry.grid(row = 6, column = 1, padx = 5, pady = 5)

        # SITUAÇÂO DA OS - Fechada ou aberta
        self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'Situação:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 7, column = 0, padx = 5, pady = 5)
        
        self.situacao_os_entry = ctk.CTkComboBox(master=self.frame_cria_os, values=["Aberta", "Fechada"], width=250, font=('Roboto', 12), corner_radius=12)
        self.situacao_os_entry.grid(row = 7, column = 1, padx = 5, pady = 5)

        # Botão Registrar
        # irá se comunicar com a base de dados e inserir os dados na base de dados
        self.btn_registrar_os = ctk.CTkButton(master =self.frame_cria_os, text= 'Registrar', width = 150, font=('Roboto', 12), corner_radius= 20, command = lambda: self.registrar_os(
            self.numero_os_entry,
            self.cliente_os_entry,
            self.veiculo_os_entry, 
            self.motorista_os_entry,
            self.servico_os_entry,   
            self.valor_os_entry,   
            self.situacao_os_entry))
                            
        self.btn_registrar_os.grid(row = 9, column = 1, padx = 1, pady = 10)

        # Botão voltar
        self.btn_voltar_cria_os = ctk.CTkButton(master =self.frame_cria_os, text= 'Voltar', width = 150, font=('Roboto', 12), corner_radius= 20, command = lambda: self.voltar_tela_os(self.frame_cria_os))                       
        self.btn_voltar_cria_os.grid(row = 10, column = 1, padx = 1, pady = 10)
        # self.os_num = os_num_entry

    # Criar self.limpa_os
    def voltar_menu(self):
        self.remover_tela_os()
        self.menu.tela_menu()


    def voltar_tela_os(self, frame):
        frame.place_forget()
        self.tela_os()


    def remover_tela_os(self):
        self.frame_os.place_forget()   


    def registrar_os(self, os, cliente, carro, motorista, servico, valor, situacao):
        os = os.get()
        cliente = cliente.get()
        carro = carro.get()
        motorista = motorista.get()
        servico = servico.get()
        valor = valor.get()
        situacao = situacao.get()
        self.backend.cadastrar_os_db(os, cliente, carro, motorista, servico, valor, situacao)
        

    def ver_os_aberta(self):
        self.remover_tela_os()
        try:
            os_abertas = self.backend.ver_os_aberta_db()

            ### self.frame_os_abertas
            self.frame_os_abertas = ctk.CTkFrame(self.master, width = 450, height = 550)
            self.frame_os_abertas.place(x = 275, y = 30)

            self.scroll_frame = ctk.CTkScrollableFrame(self.frame_os_abertas, width = 715, height = 300)
            self.scroll_frame.grid(row = 1, column = 0, padx= 5, pady =5)

            # frame_os_abertas widgets
            self.lbtitle = ctk.CTkLabel(master = self.frame_os_abertas, text = 'Ordens de serviço abertas', font = ('Roboto', 14))
            self.lbtitle.grid(row = 0, column = 0, padx = 0, pady = 10)

            table = CTkTable(master= self.scroll_frame, values=os_abertas, height=30, width=40)
            
            table.grid(row=1, column=0, padx=0, pady=20)

            # Número OS
            self.lbtitle = ctk.CTkLabel(master = self.frame_os_abertas, text = 'Selecionar ordem de serviço:', font = ('Roboto', 14))
            self.lbtitle.grid(row = 3, column = 0, padx = 0, pady = 5)

            self.selecionar_os_entry = ctk.CTkEntry(master = self.frame_os_abertas, placeholder_text= 'N. ordem de serviço', width = 175, font=('Roboto', 12),corner_radius=15)
            self.selecionar_os_entry.grid(row = 4, column = 0, padx = 0, pady = 5)

            # Botão buscar
            self.btn_buscar = ctk.CTkButton(master = self.frame_os_abertas, text= 'Buscar', width = 150, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.selecionar_os(self.frame_os_abertas, self.selecionar_os_entry.get())), fg_color='gray')                       
            self.btn_buscar.grid(row = 5, column = 0, padx = 5, pady = 5)

        except:
            messagebox.showerror(message='Ainda não há ordens de serviço abertas.')

        # Botão voltar
        self.btn_voltar = ctk.CTkButton(master = self.frame_os_abertas, text= 'Voltar', width = 150, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.voltar_tela_os(self.frame_os_abertas)))                       
        self.btn_voltar.grid(row = 10, column = 0, padx = 5, pady = 10)


    def ver_os_fechada(self):
        self.remover_tela_os()

        try:
            os_fechadas = self.backend.ver_os_fechada_db()

            # print(os_abertas)
            ### self.frame_os_fechada
            self.frame_os_fechada = ctk.CTkFrame(self.master, width = 450, height = 550)
            self.frame_os_fechada.place(x = 275, y = 30)
        
            self.scroll_frame = ctk.CTkScrollableFrame(self.frame_os_fechada, width = 715, height = 300)
            self.scroll_frame.grid(row = 1, column = 0, padx= 5, pady =5)

            # frame_os_fechada widgets
            self.lbtitle = ctk.CTkLabel(master = self.frame_os_fechada, text = 'Ordens de serviço fechadas', font = ('Roboto', 14))
            self.lbtitle.grid(row = 0, column = 0, padx = 0, pady = 10)

            table = CTkTable(master=  self.scroll_frame, values=os_fechadas, height=30, width=40)
            
            table.grid(row=1, column=0, padx=0, pady=20)

            # Número OS
            self.lbtitle = ctk.CTkLabel(master = self.frame_os_fechada, text = 'Selecionar ordem de serviço:', font = ('Roboto', 14))
            self.lbtitle.grid(row = 3, column = 0, padx = 0, pady = 5)

            self.selecionar_os_entry = ctk.CTkEntry(master = self.frame_os_fechada, placeholder_text= 'N. ordem de serviço', width = 175, font=('Roboto', 12),corner_radius=15)
            self.selecionar_os_entry.grid(row = 4, column = 0, padx = 0, pady = 5)
            
            # Botão buscar
            self.btn_buscar = ctk.CTkButton(master = self.frame_os_fechada, text= 'Buscar', width = 150, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.selecionar_os(self.frame_os_fechada, self.selecionar_os_entry.get())), fg_color='gray')                       
            self.btn_buscar.grid(row = 5, column = 0, padx = 5, pady = 5)

        except:
            messagebox.showerror(message='Ainda não há ordens de serviço fechadas.')

        # Botão voltar
        self.btn_voltar = ctk.CTkButton(master = self.frame_os_fechada, text= 'Voltar', width = 150, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.voltar_tela_os(self.frame_os_fechada)))                       
        self.btn_voltar.grid(row = 10, column = 0, padx = 5, pady = 30)


    ##### Criar botão para selecionar uma ordem de serviço e então as opções de editar ou imprimir
    ## Criar botão de editar em ver_os_aberta --- 
    ## Criar botão para imprimir ordem de serviço
        

    ## Criar input para selecionar uma ordem de serviço e dois botões (editar, imprimir)
            
    def editar_os(self):
        pass

    def imprimir_os(self):
        # Será transformado para pdf --- 
        pass

    def selecionar_os(self, frame, os):

        # Botão para buscar
        os_info = self.buscar_os(os)

        self.limpa_frame(frame)

        ### self.frame_os_selecionada
        self.frame_os_selecionada = ctk.CTkFrame(self.master, width = 450, height = 550)
        self.frame_os_selecionada.place(x = 275, y = 30)

        # frame_os_selecionada widgets
        self.lbtitle = ctk.CTkLabel(master = self.frame_os_selecionada, text = 'Ordem de serviço', font = ('Roboto', 14))
        self.lbtitle.grid(row = 0, column = 0, padx = 0, pady = 10)

        try:
            table = CTkTable(master=  self.frame_os_selecionada, values= os_info, height=30, width=40)
            
            table.grid(row=1, column=0, padx=0, pady=20)
        except:
            messagebox.showerror(message='Ordem de serviço não encontrada!')

        # Botão voltar
        self.btn_voltar = ctk.CTkButton(master = self.frame_os_selecionada, text= 'Voltar', width = 150, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.voltar_tela_os(self.frame_os_selecionada)))                       
        self.btn_voltar.grid(row = 10, column = 0, padx = 5, pady = 10)     


    def limpa_frame(self, frame):
        frame.place_forget()   


    def buscar_os(self, os):
        os_info = self.backend.buscar_os_db(os)
        return os_info