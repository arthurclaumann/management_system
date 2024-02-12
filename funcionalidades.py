import customtkinter as ctk
from tkinter import * 
from tkinter import messagebox

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
        self.frame_os.place(x = 350, y = 30)

        # frame_os widgets
        self.lbtitle = ctk.CTkLabel(master = self.frame_os, text = 'Ordem de Serviço', font = ('Roboto', 14))
        self.lbtitle.grid(row = 0, column = 0, padx = 10, pady = 10)      


        ### Criando as opções das OS
        # Botão os
        self.btn_os = ctk.CTkButton(master = self.frame_os, text= 'Criar ordem de serviço', width = 300, font=('Roboto', 12), corner_radius= 20, fg_color = 'green', command = self.cria_os)                             
        self.btn_os.grid(row = 2, column = 0, padx = 10, pady = 10)

        # # Botão voucher_despesa
        # self.btn_voucher_despesa = ctk.CTkButton(master = self.frame_os, text= 'Voucher/Despesa', width = 200, font=('Roboto', 14), corner_radius= 20, fg_color = 'green')                             
        # self.btn_voucher_despesa.grid(row = 3, column = 0, padx = 10, pady = 10)

        # # Botão vouchers_emitidos
        # self.btn_voucher_emitido = ctk.CTkButton(master = self.frame_os, text= 'Vouchers emitidos', width = 200, font=('Roboto', 14), corner_radius= 20, fg_color = 'green')                             
        # self.btn_voucher_emitido.grid(row = 4, column = 0, padx = 10, pady = 10)

        # Botão os_aberta
        self.btn_os_aberta = ctk.CTkButton(master = self.frame_os, text= 'Ordens de serviço abertas', width = 300, font=('Roboto', 14), corner_radius= 20, fg_color = 'green')                             
        self.btn_os_aberta.grid(row = 5, column = 0, padx = 10, pady = 10)
     
        # Botão os_fechada
        self.btn_os_fechada = ctk.CTkButton(master = self.frame_os, text= 'Ordens de serviço fechadas', width = 300, font=('Roboto', 14), corner_radius= 20, fg_color = 'green')                             
        self.btn_os_fechada.grid(row = 7, column = 0, padx = 10, pady = 10)

        # # Botão fechar_os
        # self.btn_fechar_os = ctk.CTkButton(master = self.frame_os, text= 'Fechar OS', width = 200, font=('Roboto', 14), corner_radius= 20, fg_color = 'green')                             
        # self.btn_fechar_os.grid(row = 6, column = 0, padx = 10, pady = 10)


        # Botão relatorio_por_carro
        self.btn_relatorio_carro = ctk.CTkButton(master = self.frame_os, text= 'Relatório por carros', width = 300, font=('Roboto', 14), corner_radius= 20, fg_color = 'green')                             
        self.btn_relatorio_carro.grid(row = 8, column = 0, padx = 10, pady = 10)

        # Botão voltar
        self.btn_voltar = ctk.CTkButton(master = self.frame_os, text= 'Voltar', width = 150, font=('Roboto', 14), corner_radius= 20, command = self.voltar_menu)                       
        self.btn_voltar.grid(row = 10, column = 0, padx = 5, pady = 10)


    def cria_os(self):
        self.remover_tela_os()

        ### self.frame_cria_os
        self.frame_cria_os = ctk.CTkFrame(self.master, width = 550, height = 600)
        self.frame_cria_os.place(x = 250, y = 30)

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

        self.veiculo_os_entry = ctk.CTkEntry(master = self.frame_cria_os, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.veiculo_os_entry.grid(row = 3, column = 1, padx = 5, pady = 5)

        # Motorista
        self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'Motorista', font = ('Roboto', 14))
        self.lbtitle.grid(row = 4, column = 0, padx = 5, pady = 5)

        self.motorista_os_entry = ctk.CTkEntry(master = self.frame_cria_os, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.motorista_os_entry.grid(row = 4, column = 1, padx = 5, pady = 5)

        # Serviço
        self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'Serviço', font = ('Roboto', 14))
        self.lbtitle.grid(row = 5, column = 0, padx = 5, pady = 5)
  
        self.servico_os_entry = ctk.CTkEntry(master = self.frame_cria_os, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.servico_os_entry.grid(row = 5, column = 1, padx = 5, pady = 5)

        # VALOR DA OS
        # SITUAÇÂO DA OS - Fechada ou aberta

        # Botão Registrar
        # irá se comunicar com a base de dados e inserir os dados na base de dados
        self.btn_registrar_os = ctk.CTkButton(master =self.frame_cria_os, text= 'Registrar', width = 150, font=('Roboto', 12), corner_radius= 20, command = lambda: self.backend.cadastrar_os(self.numero_os_entry,))                       
        self.btn_registrar_os.grid(row = 8, column = 1, padx = 5, pady = 10)

        # Botão voltar
        self.btn_voltar_cria_os = ctk.CTkButton(master =self.frame_cria_os, text= 'Voltar', width = 150, font=('Roboto', 12), corner_radius= 20, command = lambda: self.voltar_tela_os(self.frame_cria_os))                       
        self.btn_voltar_cria_os.grid(row = 8, column = 2, padx = 5, pady = 10)
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


    def registrar_os(self):
        pass
