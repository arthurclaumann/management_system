import customtkinter as ctk
from tkinter import * 
from tkinter import messagebox
from menu_app import App_menu
from PIL import Image

class Login():
    def __init__(self, master, backend):
        self.master = master
        self.backend = backend
        self.menu = App_menu(self.master, self.backend)
        self.backend.cria_tabela()


    def tela_login(self):


        self.frame_login = ctk.CTkFrame(self.master)
        # self.frame_login.place(x = 400, y = 30)
        self.frame_login.grid_columnconfigure(0, weight=1)
        self.frame_login.grid_columnconfigure(1, weight=2) 
        self.frame_login.grid(row = 0,  column = 0, pady = 30, padx = 40, sticky='nswe')


        # frame image
        # Criando o título
        self.title = ctk.CTkLabel(self.frame_login, text = 'Sistema de Gerenciamento\nArca Brasil', font = ('Roboto', 20), justify = 'center' )
        self.title.grid(row = 0, column = 0, padx = 5, pady = 30)

        self.logo_image = ctk.CTkImage(light_image= Image.open('Ativo 22.png'), size = (200,200))
        self.logo = ctk.CTkLabel(self.frame_login, text='', image=self.logo_image, anchor='center',justify='center')
        self.logo.grid(row = 1, column = 0, pady = 5, padx = 40, sticky = 'nswe', rowspan = 5)


        # frame_login widgets
        self.lbtitle = ctk.CTkLabel(master = self.frame_login, text = 'Faça seu Login', font = ('Roboto', 18))
        self.lbtitle.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = 'we')

        # Usuario
        self.username_entry = ctk.CTkEntry(master = self.frame_login, placeholder_text= 'Nome de usuário', width = 300, font=('Roboto', 14),corner_radius=15, justify = 'center')
        self.username_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
    
        # Senha
        self.pwd_entry = ctk.CTkEntry(master = self.frame_login, placeholder_text= 'Senha', show = '*', width = 300, font=('Roboto', 14),corner_radius=20, justify = 'center')
        self.pwd_entry.grid(row = 2, column = 1, padx = 10, pady = 10)
    
        # # Ver senha
        # self.ver_senha = ctk.CTkCheckBox(master = self.frame_login, text = 'Mostrar senha' , font=('Roboto', 12), corner_radius=15)
        # self.ver_senha.grid(row = 3, column = 1, padx = 10, pady = 10)

        # Botão login
        self.btn_login = ctk.CTkButton(master = self.frame_login, text= 'Fazer login', width = 300, font=('Roboto', 14), corner_radius= 20, command=lambda: self.backend.verifica_login(self.username_entry.get(),self.pwd_entry.get(), self.limpa_entry_login, self.remover_tela_login, self.menu.tela_menu))
        self.btn_login.grid(row = 4, column = 1, padx = 10, pady = 10)
                               

        self.span = ctk.CTkLabel(master = self.frame_login, text = 'Não tem conta? Registre-se', font=('Roboto', 14))
        self.span.grid(row = 5, column = 1, padx = 10, pady = 10)

        self.btn_cadastro = ctk.CTkButton(master = self.frame_login, text = 'Fazer cadastro', font=('Roboto', 14), fg_color = 'green', command = self.tela_de_cadastro, corner_radius=20)
        self.btn_cadastro.grid(row = 6, column = 1, padx = 10, pady = 10)
    
    def tela_de_cadastro(self):
        # Remover o formulário de login
        self.remover_tela_login()

        ### frame formulário cadastro
        self.frame_cadastro = ctk.CTkFrame(self.master, width = 400, height = 500)
        self.frame_cadastro.grid_columnconfigure(0, weight=1)
        self.frame_cadastro.grid(row = 0,  column = 1, pady = 30)
        # self.frame_cadastro.place(x = 350, y = 30)


        # frame_cadastro widgets
        self.lbtitle = ctk.CTkLabel(master = self.frame_cadastro, text = 'Faça seu cadastro', font = ('Roboto', 18))
        self.lbtitle.grid(row = 0, column = 1, padx = 10, pady = 5)

        # Criando widgets de cadastro
        # Usuario
        self.username_cadastro_entry = ctk.CTkEntry(master = self.frame_cadastro, placeholder_text= 'Nome de usuário', width = 300, font=('Roboto', 14),corner_radius=15, justify = 'center')
        self.username_cadastro_entry.grid(row = 1, column = 0, padx = 10, pady = 5)
    
        # Senha
        self.pwd_cadastro_entry = ctk.CTkEntry(master = self.frame_cadastro, placeholder_text= 'Senha', show = '*', width = 300, font=('Roboto', 14),corner_radius=20, justify = 'center')
        self.pwd_cadastro_entry.grid(row = 2, column = 0, padx = 10, pady = 5)

        # confirma senha
        self.confirma_senha_cadastro_entry = ctk.CTkEntry(master = self.frame_cadastro, placeholder_text= 'Confirme a senha', show = '*', width = 300, font=('Roboto', 14),corner_radius=15, justify = 'center')
        self.confirma_senha_cadastro_entry.grid(row = 3, column = 0, padx = 10, pady = 5)

        # Ver senha
        self.ver_senha = ctk.CTkCheckBox(master = self.frame_cadastro, text = 'Mostrar senha' , font=('Roboto', 12), corner_radius=15, checkbox_height=15, checkbox_width=15)
        self.ver_senha.grid(row = 4, column = 0, pady = 5)

        self.btn_cadastrar_user = ctk.CTkButton(master = self.frame_cadastro, corner_radius=15, text = 'Cadastrar', font=('Roboto', 14), fg_color = 'green', command=lambda: self.backend.cadastrar_usuario(
                                                self.username_cadastro_entry.get(),
                                                self.pwd_cadastro_entry.get(),
                                                self.confirma_senha_cadastro_entry.get(),
                                                self.limpa_entry_cadastro))
        self.btn_cadastrar_user.grid(row = 5, column = 0, padx = 10, pady = 5)
        

        self.btn_login_back = ctk.CTkButton(master = self.frame_cadastro, text = 'Voltar', font=('Roboto', 14), fg_color = '#444', hover='#333',command = self.tela_login, corner_radius=15) 
        self.btn_login_back.grid(row = 6, column = 0, padx = 10, pady =10)


    def limpa_entry_cadastro(self):
        self.username_cadastro_entry.delete(0, END)
        self.pwd_cadastro_entry.delete(0, END)
        self.confirma_senha_cadastro_entry.delete(0, END)

    def limpa_entry_login(self):
        self.username_entry.delete(0, END)
        self.pwd_entry.delete(0, END)

    def remover_tela_login(self):
        self.frame_login.grid_remove()        

    