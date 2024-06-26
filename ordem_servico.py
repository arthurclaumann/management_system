import customtkinter as ctk
from tkinter import * 
from tkinter import messagebox
from CTkTable import *
import datetime
from CTkScrollableDropdown import *
import os
import win32com.client
from docxtpl import DocxTemplate


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
        self.backend.cria_tabela_os()


    def tela_os(self):
        self.menu.limpa_menu()

        ### self.frame_os
        self.frame_os = ctk.CTkFrame(self.master, width = 400, height = 500)
        self.frame_os.grid_columnconfigure(0, weight=1)
        self.frame_os.grid(row = 0,  column = 0, pady = 30)

        # frame_os widgets
        self.lbtitle = ctk.CTkLabel(master = self.frame_os, text = 'Ordem de Serviço', font = ('Roboto', 14))
        self.lbtitle.grid(row = 0, column = 0, padx = 10, pady = 10)      


        ### Criando as opções das OS
        # Botão os
        self.btn_os = ctk.CTkButton(master = self.frame_os, text= 'Criar ordem de serviço', width = 300, font=('Roboto', 14), corner_radius= 20, command = self.cria_os)                           
        self.btn_os.grid(row = 2, column = 0, padx = 10, pady = 10)

        # Botão os_aberta
        self.btn_os_aberta = ctk.CTkButton(master = self.frame_os, text= 'Ordens de serviço abertas', width = 300, font=('Roboto', 14), corner_radius= 20, command= self.ver_os_aberta)                             
        self.btn_os_aberta.grid(row = 5, column = 0, padx = 10, pady = 10)
     
        # Botão os_fechada
        self.btn_os_fechada = ctk.CTkButton(master = self.frame_os, text= 'Ordens de serviço fechadas', width = 300, font=('Roboto', 14), corner_radius= 20, command = self.ver_os_fechada)                             
        self.btn_os_fechada.grid(row = 6, column = 0, padx = 10, pady = 10)

        # Botão fechar_os
        self.btn_fechar_os = ctk.CTkButton(master = self.frame_os, text= 'Fechar ordem de serviço', width = 300, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.frame_fechar_editar('Fechar')))                            
        self.btn_fechar_os.grid(row = 7, column = 0, padx = 10, pady = 10)

        # Editar os
        self.btn_editar_os = ctk.CTkButton(master = self.frame_os, text= 'Editar ordem de serviço', width = 300, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.frame_fechar_editar('Editar')))                         
        self.btn_editar_os.grid(row = 8, column = 0, padx = 10, pady = 10)

        # Botão relatorio_por_carro
        self.btn_relatorio_carro = ctk.CTkButton(master = self.frame_os, text= 'Relatório por carros', width = 300, font=('Roboto', 14), corner_radius= 20)                         
        self.btn_relatorio_carro.grid(row = 9, column = 0, padx = 10, pady = 10)

        # Botão voltar
        self.btn_voltar = ctk.CTkButton(master = self.frame_os, text= 'Voltar', width = 150, font=('Roboto', 14), corner_radius= 20, command = self.voltar_menu, fg_color='green')                       
        self.btn_voltar.grid(row = 10, column = 0, padx = 5, pady = 10)


    def cria_os(self):
        self.remover_tela_os()

        ### self.frame_cria_os
        self.frame_cria_os = ctk.CTkFrame(self.master, width = 400, height = 500)
        self.frame_cria_os.grid_columnconfigure(0, weight=1)
        self.frame_cria_os.grid(row = 0,  column = 0, pady = 30)
        
        self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'Preencher nova ordem de serviço', font = ('Roboto', 18))
        self.lbtitle.grid(row = 0, column = 0, padx = 0, pady = 10, sticky = 'nswe', columnspan = 2)

        # # Data
        self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'Data', font = ('Roboto', 14))
        self.lbtitle.grid(row = 1, column = 0, padx = 0, pady = 10)

        self.date_os_entry = ctk.CTkEntry(master = self.frame_cria_os, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.date_os_entry.grid(row = 1, column = 1, padx = 5, pady = 10)

        
        # Cliente
        self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'Cliente', font = ('Roboto', 14))
        self.lbtitle.grid(row = 2, column = 0, padx = 5, pady = 10)

        self.cliente_os_entry = ctk.CTkEntry(master = self.frame_cria_os, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.cliente_os_entry.grid(row = 2, column = 1, padx = 5, pady = 10)

        CTkScrollableDropdown(self.cliente_os_entry, values=self.retorna_todos_clientes(), command=lambda e: self.cliente_os_entry.insert(1, e),
                      autocomplete=True) # Using autocomplete

        # Veículo  --- criar registro de veículos e inserir lista de veículos nas opções
        self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'Veiculo', font = ('Roboto', 14))
        self.lbtitle.grid(row = 3, column = 0, padx = 5, pady = 5)
        
        self.veiculo_os_entry = ctk.CTkComboBox(master=self.frame_cria_os, justify = 'center', width=250, font=('Roboto', 12), corner_radius=12)
        self.veiculo_os_entry.grid(row = 3, column = 1, padx = 5, pady = 5)

        CTkScrollableDropdown(self.veiculo_os_entry, values=self.retorna_todos_veiculos(), justify="left", button_color="transparent", autocomplete = True)


        # Motorista --- Criar função para obter motoristas do db
        self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'Motorista', font = ('Roboto', 14))
        self.lbtitle.grid(row = 4, column = 0, padx = 5, pady = 5)

        self.motorista_os_entry = ctk.CTkEntry(master = self.frame_cria_os, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.motorista_os_entry.grid(row = 4, column = 1, padx = 5, pady = 5)

        CTkScrollableDropdown(self.motorista_os_entry, values=self.retorna_todos_motoristas(), command=lambda e: self.motorista_os_entry.insert(1, e),
                      autocomplete=True) # Using autocomplete
        # Serviço
        self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'Serviço', font = ('Roboto', 14))
        self.lbtitle.grid(row = 5, column = 0, padx = 5, pady = 5)
  
        self.servico_os_entry = ctk.CTkEntry(master = self.frame_cria_os, placeholder_text= '', width = 250, font=('Roboto', 12),corner_radius=15)
        self.servico_os_entry.grid(row = 5, column = 1, padx = 5, pady = 5)

        # # SITUAÇÂO DA OS - Fechada ou aberta
        # self.lbtitle = ctk.CTkLabel(master = self.frame_cria_os, text = 'Situação:', font = ('Roboto', 14))
        # self.lbtitle.grid(row = 7, column = 0, padx = 5, pady = 5)
        
        # self.situacao_os_entry = ctk.CTkComboBox(master=self.frame_cria_os, values=["Aberta", "Fechada"], width=250, font=('Roboto', 12), corner_radius=12)
        # self.situacao_os_entry.grid(row = 7, column = 1, padx = 5, pady = 5)

        # Botão Registrar
        # irá se comunicar com a base de dados e inserir os dados na base de dados
        self.btn_registrar_os = ctk.CTkButton(master =self.frame_cria_os, text= 'Registrar', width = 150, font=('Roboto', 12), corner_radius= 20, command = lambda: self.cadastrar_os_aberta(
            self.date_os_entry,   
            self.cliente_os_entry,
            self.veiculo_os_entry, 
            self.motorista_os_entry,
            self.servico_os_entry))
                            
        self.btn_registrar_os.grid(row = 9, column = 1, padx = 1, pady = 10)

        # Botão imprimir ordem de serviço
        self.btn_imprimir_os = ctk.CTkButton(master =self.frame_cria_os, text= 'Imprimir', width = 150, font=('Roboto', 12), corner_radius= 20, command = lambda: self.imprimir_os(
            self.cliente_os_entry.get(),
            self.date_os_entry.get(),   
            self.veiculo_os_entry.get(), 
            self.motorista_os_entry.get(),
            self.servico_os_entry.get()))
                            
        self.btn_imprimir_os.grid(row = 10, column = 1, padx = 1, pady = 10)


        # Botão voltar
        self.btn_voltar_cria_os = ctk.CTkButton(master =self.frame_cria_os, text= 'Voltar', width = 150, font=('Roboto', 12), corner_radius= 20, command = lambda: self.voltar_tela_os(self.frame_cria_os, self.tela_os))                       
        self.btn_voltar_cria_os.grid(row = 11, column = 1, padx = 1, pady = 10)


    def cria_frame_ver_os(self, frame, titulo, filtro, dados_db, frame_anterior, situacao):
        self.remover_tela_os()
        try:
            ### Criando o frame
            frame.grid_columnconfigure(0, weight=1)
            frame.grid(row = 0,  column = 0, pady = 30, columnspan = 10)

           # frame scrollable 
            self.scroll_frame = ctk.CTkScrollableFrame(frame, width = 900, height = 300)
            self.scroll_frame.grid(row = 1, column = 0, padx= 5, pady =5)

            # Widgets
            # 1. Título
            self.lbtitle = ctk.CTkLabel(master = frame, text = titulo, font = ('Roboto', 14))
            self.lbtitle.grid(row = 0, column = 0, padx = 0, pady = 10)

            # 2. Criando a tabela
            table = CTkTable(master= self.scroll_frame, values=dados_db, height=30, width=40, column=11)
            table.grid(row=1, column=0, padx=0, pady=20)
            
        # # Lista de opções com autopreenchimento
            # Título seleção
            self.lbtitle = ctk.CTkLabel(master = frame, text = 'Selecione a opção:', font = ('Roboto', 14))
            self.lbtitle.grid(row = 2, column = 0, padx = 0, pady = 0)
            # # # Lista de opções com autopreenchimento
            self.var1 = ctk.StringVar()         
            self.selecionar_options_filtro = ctk.CTkComboBox(master = frame, variable=self.var1, values = filtro, width = 250, state = 'readonly', font=('Roboto', 12),corner_radius=15, command = lambda value: (self.on_combo1_selected(value, entry_frame = self.selecionar_entry)))
            self.selecionar_options_filtro.grid(row = 3, column = 0, padx = 0, pady = 5)

            self.selecionar_entry = ctk.CTkEntry(master = frame, placeholder_text='', width = 240, font=('Roboto', 12),corner_radius=15)
            self.selecionar_entry.grid(row = 4, column = 0, padx = 0, pady = 5)
    
            CTkScrollableDropdown(self.selecionar_entry, values=[], command=lambda e: self.selecionar_entry.insert(1, e),
                autocomplete=True) # Using autocomplete
                
            # Botão buscar
            self.btn_buscar = ctk.CTkButton(master = frame, text= 'Buscar', width = 150, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.selecionar_os(frame, self.selecionar_options_filtro.get(), self.selecionar_entry.get(), situacao, frame_anterior)), fg_color='gray')                       
            self.btn_buscar.grid(row = 5, column = 0, padx = 5, pady = 5)
        except:
            if situacao == 'Aberta':
                messagebox.showinfo(message='Ainda não há ordens de serviço abertas.')
            elif situacao == 'Fechada':
                messagebox.showinfo(message='Ainda não há ordens de serviço fechadas.')
       
        # Botão voltar
        self.btn_voltar = ctk.CTkButton(master = frame, text= 'Voltar', width = 150, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.voltar_tela_os(frame, self.tela_os)))                       
        self.btn_voltar.grid(row = 10, column = 0, padx = 5, pady = 10)


    def ver_os_aberta(self):
        os_abertas = self.backend.ver_os_aberta_db()
        self.frame_os_aberta = ctk.CTkFrame(self.master, width = 450, height = 550)
        filtro=['Ordem de serviço', 'Data', 'Cliente', 'Carro', 'Motorista']

        self.cria_frame_ver_os( self.frame_os_aberta, 'Ordens de serviço abertas', filtro, os_abertas, self.ver_os_aberta, 'Aberta')


    def ver_os_fechada(self):
        os_fechadas = self.backend.ver_os_fechada_db()
        self.frame_os_fechada = ctk.CTkFrame(self.master, width = 450, height = 550)
        filtro=['Ordem de serviço', 'Data', 'Cliente', 'Carro', 'Motorista']
        self.cria_frame_ver_os(self.frame_os_fechada,'Ordens de serviço fechadas', filtro, os_fechadas, self.ver_os_fechada, 'Fechada')


    def frame_fechar_editar(self, acao):
        self.remover_tela_os()

        try:
            ### Criando o frame
            self.frame_fechar_os = ctk.CTkFrame(self.master, width = 450, height = 550)
            self.frame_fechar_os.grid_columnconfigure(0, weight=1)
            self.frame_fechar_os.grid(row = 0,  column = 0, pady = 30, columnspan = 10)

           # frame scrollable 
            self.scroll_frame = ctk.CTkScrollableFrame(self.frame_fechar_os, width = 900, height = 300)
            self.scroll_frame.grid(row = 1, column = 0, padx= 5, pady =5)

            if acao == 'Fechar':
                ordens_servico = self.backend.ver_os_aberta_db()
                self.lbtitle = ctk.CTkLabel(master = self.frame_fechar_os, text = 'Fechar ordem de serviço', font = ('Roboto', 14))
            elif acao == 'Editar':
                ordens_servico = self.backend.ver_os_fechada_db()
                self.lbtitle = ctk.CTkLabel(master = self.frame_fechar_os, text = 'Editar ordem de serviço', font = ('Roboto', 14))

            # Widgets
            # 1. Título
            self.lbtitle.grid(row = 0, column = 0, padx = 0, pady = 10)

            # 2. Criando a tabela
            table = CTkTable(master= self.scroll_frame, values=ordens_servico, height=30, width=40, column=7)
            table.grid(row=1, column=0, padx=0, pady=20)
            
        # # Lista de opções com autopreenchimento
            # Título seleção
            self.lbtitle = ctk.CTkLabel(master = self.frame_fechar_os, text = 'Digite a ordem de serviço:', font = ('Roboto', 14))
            self.lbtitle.grid(row = 2, column = 0, padx = 0, pady = 0)

            # # # Entrada da ordem de serviço
            self.selecionar_entry = ctk.CTkEntry(master = self.frame_fechar_os, placeholder_text='Num. Ordem de serviço', width = 240, font=('Roboto', 12),corner_radius=15)
            self.selecionar_entry.grid(row = 3, column = 0, padx = 0, pady = 5)
                
            # Botão buscar
            if acao == 'Fechar':
                self.btn_selecionar = ctk.CTkButton(master = self.frame_fechar_os, text= 'Selecionar', width = 150, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.tela_fechar_editar_os(self.frame_fechar_os, self.selecionar_entry, acao = 'Fechar')), fg_color='gray')  
            elif acao == 'Editar':
                self.btn_selecionar = ctk.CTkButton(master = self.frame_fechar_os, text= 'Selecionar', width = 150, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.tela_fechar_editar_os(self.frame_fechar_os, self.selecionar_entry, acao = 'Editar')), fg_color='gray')  

            self.btn_selecionar.grid(row = 5, column = 0, padx = 5, pady = 5)
        except:
            messagebox.showinfo(message='Não foi possível encotrar a ordem de serviço.') 

        # Botão voltar
        self.btn_voltar = ctk.CTkButton(master = self.frame_fechar_os, text= 'Voltar', width = 150, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.voltar_tela_os(self.frame_fechar_os, self.tela_os)))                       
        self.btn_voltar.grid(row = 10, column = 0, padx = 5, pady = 10)
        

    def tela_fechar_editar_os(self, frame, valor, acao):
        if acao == 'Editar':
            resultado_filtro = self.filtro_registros_os('Ordem de serviço', valor.get(), 'Fechada')
            state = 'normal'
        elif acao == 'Fechar':
            resultado_filtro = self.filtro_registros_os('Ordem de serviço', valor.get(), 'Aberta')
            state = 'disabled'


        self.limpa_frame(frame)
            ### Criando o frame
        self.frame_fechando_os = ctk.CTkFrame(self.master, width = 500, height = 600)
        self.frame_fechando_os.grid_columnconfigure(0, weight=1)
        self.frame_fechando_os.grid(row = 0,  column = 0, pady = 30, columnspan = 10)
        
        # 1. Título
        self.lbtitle = ctk.CTkLabel(master = self.frame_fechando_os, text = f'{acao} ordem de serviço', font = ('Roboto', 18), justify = 'center')
        self.lbtitle.grid(row = 0, column = 0, padx = 0, pady = 10, columnspan = 2)

        # ADICIONAR AQUI OS OUTROS ELEMENTOS PARA O PREENCHIMENTO
        # Título seleção
        # N. Ordem de serviço
        self.lbtitle = ctk.CTkLabel(master = self.frame_fechando_os, text = 'Ordem de serviço:', font = ('Roboto', 14), corner_radius=15, justify = 'center')
        self.lbtitle.grid(row = 1, column = 0, padx = 0, pady = 5)

        self.os_entry = ctk.CTkEntry(master = self.frame_fechando_os, placeholder_text=f'{resultado_filtro[0][0]}', width = 240, font=('Roboto', 12),corner_radius=15, justify = 'center', takefocus = 0, height=25)
        self.os_entry.grid(row = 1, column = 1, padx = 0, pady = 5)
        self.os_entry.configure(state = 'disabled')

        # Data
        self.lbtitle = ctk.CTkLabel(master = self.frame_fechando_os, text = 'Data:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 2, column = 0, padx = 0, pady = 5)
        self.data_entry = ctk.CTkEntry(master = self.frame_fechando_os, placeholder_text=f'{resultado_filtro[0][2]}', width = 240, font=('Roboto', 12),corner_radius=15, justify = 'center', takefocus = 0, height=25)
        self.data_entry.grid(row = 2, column = 1, padx = 0, pady = 5)  
        self.data_entry.configure(state = 'disabled')
        
        # Cliente
        self.lbtitle = ctk.CTkLabel(master = self.frame_fechando_os, text = 'Cliente:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 3, column = 0, padx = 0, pady = 5)
        self.cliente_entry = ctk.CTkEntry(master = self.frame_fechando_os, placeholder_text=f'{resultado_filtro[0][3]}', width = 240, font=('Roboto', 12),corner_radius=15, justify = 'center', takefocus = 0, height=25)
        self.cliente_entry.grid(row = 3, column = 1, padx = 0, pady = 5)       
        self.cliente_entry.configure(state = 'disabled')

        # Veículo
        self.lbtitle = ctk.CTkLabel(master = self.frame_fechando_os, text = 'Veículo:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 4, column = 0, padx = 0, pady = 5)
        self.veiculo_entry = ctk.CTkEntry(master = self.frame_fechando_os, placeholder_text=f'{resultado_filtro[0][4]}', width = 240, font=('Roboto', 12),corner_radius=15, justify = 'center', takefocus = 0, height=25)
        self.veiculo_entry.grid(row = 4, column = 1, padx = 0, pady = 5)   
        self.veiculo_entry.configure(state = 'disabled')

        # # Motorista
        self.lbtitle = ctk.CTkLabel(master = self.frame_fechando_os, text = 'Motorista:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 5, column = 0, padx = 0, pady = 5)
        self.motorista_entry = ctk.CTkEntry(master = self.frame_fechando_os, placeholder_text=f'{resultado_filtro[0][5]}', width = 240, font=('Roboto', 12),corner_radius=15, justify = 'center', takefocus = 0, height=25)
        self.motorista_entry.grid(row = 5, column = 1, padx = 0, pady = 5)
        self.motorista_entry.configure(state = 'disabled')

        # # Serviço
        self.lbtitle = ctk.CTkLabel(master = self.frame_fechando_os, text = 'Serviço:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 6, column = 0, padx = 0, pady = 5)
        self.servico_entry = ctk.CTkEntry(master = self.frame_fechando_os, placeholder_text=f'{resultado_filtro[0][6]}', width = 240, font=('Roboto', 12),corner_radius=15, justify = 'center', takefocus = 0, height=25)
        self.servico_entry.grid(row = 6, column = 1, padx = 0, pady = 5)
        self.servico_entry.configure(state = 'disabled')

        # # Receita
        self.lbtitle = ctk.CTkLabel(master = self.frame_fechando_os, text = 'Receita:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 7, column = 0, padx = 0, pady = 5)
        self.receita_entry = ctk.CTkEntry(master = self.frame_fechando_os, placeholder_text = f'{resultado_filtro[0][7]}', width = 240, font=('Roboto', 12),corner_radius=15, justify = 'center', takefocus = 0, height=25)
        self.receita_entry.grid(row = 7, column = 1, padx = 0, pady = 5)

        # # Cod. Receita
        self.lbtitle = ctk.CTkLabel(master = self.frame_fechando_os, text = 'Cod. Receita:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 8, column = 0, padx = 0, pady = 5)
        self.cod_receita_entry = ctk.CTkComboBox(master=self.frame_fechando_os, values=["001 - Fretamento", "002 - Comissão venda", '003 - Comissão Hotel'], width=250, font=('Roboto', 12), corner_radius=12, justify = 'center', height = 20)
        self.cod_receita_entry.grid(row = 8, column = 1, padx = 0, pady = 5)

        # # Despesa
        self.lbtitle = ctk.CTkLabel(master = self.frame_fechando_os, text = 'Despesa:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 9, column = 0, padx = 0, pady = 5) 
        self.despesa_entry = ctk.CTkEntry(master = self.frame_fechando_os, placeholder_text = f'{resultado_filtro[0][9]}', width = 240, font=('Roboto', 12),corner_radius=15, justify = 'center', takefocus = 0, height=25)
        self.despesa_entry.grid(row = 9, column = 1, padx = 0, pady = 5)

        # # Cod. Despesa
        self.lbtitle = ctk.CTkLabel(master = self.frame_fechando_os, text = 'Cod. Despesa:', font = ('Roboto', 14))
        self.lbtitle.grid(row = 10, column = 0, padx = 0, pady = 5)
        self.cod_despesa_entry = ctk.CTkComboBox(master=self.frame_fechando_os, values=["001 - Combustivel", "002 - Alimentação"], width=250, font=('Roboto', 12), corner_radius=12, justify = 'center', height = 20)
        self.cod_despesa_entry.grid(row = 10, column = 1, padx = 0, pady = 5)


        
        if acao == 'Fechar':
            # Botão Finalizar --------
            self.btn_finalizar = ctk.CTkButton(master = self.frame_fechando_os, text= 'Finalizar', width = 150, font=('Roboto', 14), corner_radius= 20, height=20 ,command = lambda: (self.finalizar_os(resultado_filtro[0][0], self.receita_entry, self.cod_receita_entry, self.despesa_entry, self.cod_despesa_entry)))                         
            self.btn_finalizar.grid(row = 11, column = 1, padx = 5, pady = 10)
        elif acao == 'Editar':
            # Botão Finalizar --------
            self.btn_editar = ctk.CTkButton(master = self.frame_fechando_os, text= 'Finalizar', width = 150, font=('Roboto', 14), corner_radius= 20, height=20 ,command = lambda: (self.editar_os(resultado_filtro[0][0], self.receita_entry, self.cod_receita_entry, self.despesa_entry, self.cod_despesa_entry)))                         
            self.btn_editar.grid(row = 11, column = 1, padx = 5, pady = 10)


        # Botão voltar
        self.btn_voltar = ctk.CTkButton(master = self.frame_fechando_os, text= 'Voltar', width = 150, font=('Roboto', 14), corner_radius= 20, height=20 ,command = lambda: (self.voltar_tela_os(self.frame_fechando_os, self.tela_os)))                       
        self.btn_voltar.grid(row = 12, column = 1, padx = 5, pady = 10)


    def finalizar_os(self, num_os, receita, cod_receita, despesa, cod_despesa):
        num_os = int(num_os)
        receita = float(receita.get())
        cod_receita = int(cod_receita.get()[0:3].strip())
        despesa = float(despesa.get())
        cod_despesa = int(cod_despesa.get()[0:3].strip())

        if(receita == "" or cod_receita =="" or despesa =="" or cod_despesa ==''):
            messagebox.showerror(title ='', message='Preencha todos os dados!')
        else:
            self.backend.finalizar_os_db(num_os, receita, cod_receita, despesa, cod_despesa)


    def selecionar_os(self, frame, criterio, valor, situacao, frame_anterior):
        # Botão para buscar
        self.limpa_frame(frame)
        resultado_filtro = self.filtro_registros_os(criterio, valor, situacao)


        ### self.frame_os_selecionada
        self.frame_os_selecionada = ctk.CTkFrame(self.master, width = 450, height = 550)
        self.frame_os_selecionada.grid_columnconfigure(0, weight=1)
        self.frame_os_selecionada.grid(row = 0,  column = 0, pady = 30)


        # frame_os_selecionada widgets
        self.lbtitle = ctk.CTkLabel(master = self.frame_os_selecionada, text = 'Ordem de serviço', font = ('Roboto', 18))
        self.lbtitle.grid(row = 0, column = 0, padx = 0, pady = 10)

        try:
            table = CTkTable(master=  self.frame_os_selecionada, values= resultado_filtro, height=30, width=40)
            
            table.grid(row=1, column=0, padx=0, pady=20)
        except:
            messagebox.showerror(message='Ordem de serviço não encontrada!')

        # Botão voltar
        self.btn_voltar = ctk.CTkButton(master = self.frame_os_selecionada, text= 'Voltar', width = 150, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.voltar_tela_os(self.frame_os_selecionada, frame_anterior)))                       
        self.btn_voltar.grid(row = 10, column = 0, padx = 5, pady = 10)     


    def filtro_registros_os(self, selecao, valor, situacao):
        criterio = selecao
        valor = valor

        # Mapeia o critério selecionado para a coluna correspondente no banco de dados
        mapeamento_colunas = {
        'Ordem de serviço': 'os',
        'Data': 'data',
        'Cliente': 'cliente',
        'Carro': 'carro',
        'Motorista': 'motorista'}

        if criterio in mapeamento_colunas:
            coluna = mapeamento_colunas[criterio]
        else:
            messagebox.showerror(message='Critério inválido.')
        
        # Faz a busca SQL no banco de dados
        resultado_busca = self.backend.filtro_db_os(coluna, valor, situacao)

        return resultado_busca


    def editar_os(self, num_os, receita, cod_receita, despesa, cod_despesa):
        num_os = int(num_os)
        receita = float(receita.get())
        cod_receita = int(cod_receita.get()[0:3].strip())
        despesa = float(despesa.get())
        cod_despesa = int(cod_despesa.get()[0:3].strip())

        if(receita == "" or cod_receita =="" or despesa =="" or cod_despesa ==''):
            messagebox.showerror(title ='', message='Preencha todos os dados!')
        else:
            self.backend.editar_os_db(num_os, receita, cod_receita, despesa, cod_despesa)    
        


    def voltar_menu(self):
        self.remover_tela_os()
        self.menu.tela_menu()
        # Remove the previous "Voltar" button if it exists
        if hasattr(self, "btn_voltar"):
            self.btn_voltar.destroy()


    def voltar_tela_os(self, frame_atual, frame_anterior):
        frame_atual.grid_remove()
        frame_anterior()  # Assuming you're going back to the menu screen, adjust as needed
        # Remove the previous "Voltar" button if it exists


    def remover_tela_os(self):
        self.frame_os.grid_remove()   


    def cadastrar_os_aberta(self, data, cliente, carro, motorista, servico):
        data = self.validar_formato_data(data.get())
        cliente = self.formata_texto(cliente.get())
        carro = carro.get()
        motorista = self.formata_texto(motorista.get())
        servico = self.formata_texto(servico.get())

        if(cliente =="" or carro =="" or motorista =="" or servico ==''):
            messagebox.showerror(title ='', message='Preencha todos os dados!')
        else:
            self.backend.cadastrar_os_aberta_db(data, cliente, carro, motorista, servico)

    ## Criar botão para imprimir ordem de serviço
        

    def imprimir_os(self, cliente, data, carro, motorista, servico):
        # Será transformado para pdf --- 
        num_os = self.backend.retorna_ultima_os_db()

        doc = DocxTemplate('template.docx')

        context = {'num_os': num_os,
                'nome_cliente': cliente,
                'data_emissao': data,
                'carro': carro,
                'motorista': motorista,
                'servico': servico
                }

        doc.render(context)

        doc.save('template_atualizado.docx')

        doc_path = 'template_atualizado.docx'
        
     # Verifica se o arquivo .docx existe
        if os.path.exists(doc_path):
            # Inicia o Microsoft Word
            word = win32com.client.Dispatch("Word.Application")
            # Abre o documento
            doc = word.Documents.Open(doc_path)
            # Imprime o documento
            doc.PrintOut()
            # Fecha o documento
            doc.Close()
            # Fecha o Microsoft Word
            word.Quit()
        else:
            messagebox.showerror("Erro", "O arquivo da ordem de serviço não foi encontrado.")



    def limpa_frame(self, frame):
        frame.grid_remove()   


    def validar_formato_data(self, data):
        try:
            datetime.datetime.strptime(data, '%d/%m/%Y')
            return data
        except ValueError:
            messagebox.showerror(message='Formato de data inválido. Use DD/MM/AAAA.')
            return False

    def formata_texto(self, texto):
        return texto.title().strip()
    
    def retorna_todos_veiculos(self):
        veiculos = self.backend.retorna_veiculos()
        veiculos = [veiculo[0] for veiculo in veiculos]
        return veiculos
    
       
    def retorna_todos_motoristas(self):
        motoristas = self.backend.retorna_motoristas()
        motoristas = [motorista[0] for motorista in motoristas]
        return motoristas

        
    def retorna_todos_clientes(self):
        clientes = self.backend.retorna_clientes()
        clientes = [cliente[0] for cliente in clientes]
        return clientes
        
 
    def retorna_dados_busca(self, tipo):
        if tipo == 'Cliente':
            autopreenchimento = self.retorna_todos_clientes()
        elif tipo == 'Carro':
            autopreenchimento = self.retorna_todos_veiculos()
        elif tipo == 'Motorista':
            autopreenchimento = self.retorna_todos_motoristas()
        elif tipo == 'Ordem de serviço' or tipo == 'Data' or tipo == '':
            autopreenchimento = []
         
        return autopreenchimento

        
    def on_combo1_selected(self, value, entry_frame):
        values = self.retorna_dados_busca(value)
        # Clear the entry before populating it with new values
        CTkScrollableDropdown(entry_frame, values=values, command=lambda e: entry_frame.insert(1, e),
    autocomplete=True) # Using autocomplete  