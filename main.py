import customtkinter as ctk
from tkinter import * 
from tkinter import messagebox
from database import Backend
from login import Login
# from menu_app import App_menu


class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.tema()
        self.configuracoes_janela_inicial()

        self.backend = Backend()  # para instanciar o Backend
        # Criar nova classe de login e cadastro, modularizar e então instanciar aqui
        
        self.login_screen = Login(self, self.backend) # pode ser necessário passar como argumento a função para limpar a tela e entrar no menu
        self.login_screen.tela_login()
        # self.menu = App_menu(self, self.backend, self.login_screen)

        # self.menu.tela_menu()
        self.backend.cria_tabela()
        self.backend.cria_tabela_os()

    def tema(self):
        # definindo a aparência e cor do tema
        ctk.set_appearance_mode('System')
        ctk.set_default_color_theme('dark-blue')

    def configuracoes_janela_inicial(self):
    # Criando e configurando a janela
        self.geometry("1080x600")
        self.resizable(False, False) # para evitar que altere o tamanho e os objetos internos percam seu tamanho


if __name__ == '__main__':
    app = Application()
    app.mainloop()
    