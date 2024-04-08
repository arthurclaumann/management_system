import customtkinter as ctk
from tkinter import * 
from tkinter import messagebox
from ordem_servico import OS
from cadastro import Cadastro 
from PIL import Image

class App_menu():
    def __init__(self, master, backend):
        self.master = master
        self.backend = backend
        # self.utilidades = Utilidades(master= self.master, backend =  self.backend, menu = self)
        self.os = OS(self.master, self, self.backend)
        self.cadastro = Cadastro(self.master, self, self.backend)


    def tela_menu(self):
        ### self.frame_menu
        self.frame_menu = ctk.CTkFrame(self.master, width = 400, height = 500)
        # self.frame_menu.place(x = 400, y = 30)
        self.frame_menu.grid_columnconfigure(0, weight=1)
        self.frame_menu.grid_columnconfigure(1, weight=2)
        self.frame_menu.grid(row = 0,  column = 0, pady = 30, sticky = 'nswe')

      # frame image
        # Criando o título
        self.title = ctk.CTkLabel(self.frame_menu, text = 'Sistema de Gerenciamento\nArca Brasil', font = ('Roboto', 20), justify = 'center' )
        self.title.grid(row = 0, column = 0, padx = 10, pady = 30)

        self.logo_image = ctk.CTkImage(light_image= Image.open('Ativo 22.png'), size = (200,200))
        self.logo = ctk.CTkLabel(self.frame_menu, text='', image=self.logo_image, anchor='center',justify='center')
        self.logo.grid(row = 1, column = 0, pady = 5, padx = 40, sticky = 'nswe', rowspan = 6)


        # frame_menu widgets
        self.lbtitle = ctk.CTkLabel(master = self.frame_menu, text = 'Selecione uma opção:', font = ('Roboto', 18))
        self.lbtitle.grid(row = 0, column = 1, padx = 10, pady = 10) 
        
        # Botão Ordens serviços
        self.btn_os = ctk.CTkButton(master = self.frame_menu, text= 'Ordens de Serviços', width = 300, font=('Roboto', 14), corner_radius= 20, command = self.os.tela_os)                             
        self.btn_os.grid(row = 1, column = 1, padx = 10, pady = 10)

        # Botão financeiro
        self.btn_financeiro = ctk.CTkButton(master = self.frame_menu, text= 'Financeiro', width = 300, font=('Roboto', 14), corner_radius= 20)                             
        self.btn_financeiro.grid(row = 2, column = 1, padx = 10, pady = 10)

        # Botão cadastro
        self.btn_cadastro = ctk.CTkButton(master = self.frame_menu, text= 'Cadastro', width = 300, font=('Roboto', 14), corner_radius= 20, command = self.cadastro.tela_cadastro)                             
        self.btn_cadastro.grid(row = 3, column = 1, padx = 10, pady = 10)

        # Botão apoio
        self.btn_os = ctk.CTkButton(master = self.frame_menu, text= 'Apoio', width = 300, font=('Roboto', 14), corner_radius= 20)                             
        self.btn_os.grid(row = 4, column = 1, padx = 10, pady = 10)

        # Botão parametros
        self.btn_os = ctk.CTkButton(master = self.frame_menu, text= 'Parâmetros', width = 300, font=('Roboto', 14), corner_radius= 20)                             
        self.btn_os.grid(row = 5, column = 1, padx = 10, pady = 10)

    def limpa_menu(self):
        self.frame_menu.grid_remove()        
     