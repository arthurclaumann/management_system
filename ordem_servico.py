import customtkinter as ctk
from tkinter import * 
from tkinter import messagebox
from CTkTable import *
import datetime
from CTkScrollableDropdown import *

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
        self.btn_fechar_os = ctk.CTkButton(master = self.frame_os, text= 'Fechar ordem de serviço', width = 300, font=('Roboto', 14), corner_radius= 20)                             
        self.btn_fechar_os.grid(row = 7, column = 0, padx = 10, pady = 10)

        # Editar os
        self.btn_editar_os = ctk.CTkButton(master = self.frame_os, text= 'Editar ordem de serviço', width = 300, font=('Roboto', 14), corner_radius= 20)                         
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

        # Botão voltar
        self.btn_voltar_cria_os = ctk.CTkButton(master =self.frame_cria_os, text= 'Voltar', width = 150, font=('Roboto', 12), corner_radius= 20, command = lambda: self.voltar_tela_os(self.frame_cria_os, self.tela_os))                       
        self.btn_voltar_cria_os.grid(row = 10, column = 1, padx = 1, pady = 10)


    def ver_os_aberta(self):
        self.remover_tela_os()


        try:
            os_abertas = self.backend.ver_os_aberta_db()

            ### Criando o frame
            self.frame_os_abertas = ctk.CTkFrame(self.master, width = 450, height = 550)
            self.frame_os_abertas.grid_columnconfigure(0, weight=1)
            self.frame_os_abertas.grid(row = 0,  column = 0, pady = 30)

           # frame scrollable 
            self.scroll_frame = ctk.CTkScrollableFrame(self.frame_os_abertas, width = 725, height = 300)
            self.scroll_frame.grid(row = 1, column = 0, padx= 5, pady =5)

            # Widgets
            # 1. Título
            self.lbtitle = ctk.CTkLabel(master = self.frame_os_abertas, text = 'Ordens de serviço abertas', font = ('Roboto', 14))
            self.lbtitle.grid(row = 0, column = 0, padx = 0, pady = 10)

            # 2. Criando a tabela
            table = CTkTable(master= self.scroll_frame, values=os_abertas, height=30, width=40, column=7)
            table.grid(row=1, column=0, padx=0, pady=20)

            # Opções de seleção
            # Título seleção
            self.lbtitle = ctk.CTkLabel(master = self.frame_os_abertas, text = 'Selecionar:', font = ('Roboto', 14))
            self.lbtitle.grid(row = 3, column = 0, padx = 0, pady = 0)

            # # # Lista de opções com autopreenchimento
            self.var1 = ctk.StringVar()    
            self.selecionar_options_filtro = ctk.CTkComboBox(master = self.frame_os_abertas, variable=self.var1, values=['Ordem de serviço', 'Data', 'Cliente', 'Carro', 'Motorista'], width = 250, font=('Roboto', 12),corner_radius=15, command = lambda value: (self.on_combo1_selected(value, entry_frame=self.selecionar_entry)))
            self.selecionar_options_filtro.grid(row = 4, column = 0, padx = 0, pady = 5)

            self.selecionar_entry = ctk.CTkEntry(master = self.frame_os_abertas, placeholder_text='', width = 240, font=('Roboto', 12),corner_radius=15)
            self.selecionar_entry.grid(row = 5, column = 0, padx = 0, pady = 5)

            CTkScrollableDropdown(self.selecionar_entry, values=[], command=lambda e: self.selecionar_entry.insert(1, e),
                      autocomplete=True) # Using autocomplete         

            
              # Botão buscar
            self.btn_buscar = ctk.CTkButton(master = self.frame_os_abertas, text= 'Buscar', width = 150, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.selecionar_os(self.frame_os_abertas, self.selecionar_options_filtro, self.selecionar_entry,'Aberta', self.ver_os_aberta)), fg_color='gray')                       
            self.btn_buscar.grid(row = 6, column = 0, padx = 5, pady = 5)

        except:
            messagebox.showinfo(message='Ainda não há ordens de serviço abertas.')

        # Botão voltar
        self.btn_voltar = ctk.CTkButton(master = self.frame_os_abertas, text= 'Voltar', width = 150, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.voltar_tela_os(self.frame_os_abertas, self.tela_os)))                       
        self.btn_voltar.grid(row = 10, column = 0, padx = 5, pady = 10)


    def ver_os_fechada(self):
        self.remover_tela_os()

        try:
            os_fechadas = self.backend.ver_os_fechada_db()

            ### Criando o frame
            self.frame_os_fechada = ctk.CTkFrame(self.master, width = 450, height = 550)
            self.frame_os_fechada.grid_columnconfigure(0, weight=1)
            self.frame_os_fechada.grid(row = 0,  column = 0, pady = 30)

           # frame scrollable 
            self.scroll_frame = ctk.CTkScrollableFrame(self.frame_os_fechada, width = 725, height = 300)
            self.scroll_frame.grid(row = 1, column = 0, padx= 5, pady =5)

            # widgets
            # 1. Título
            self.lbtitle = ctk.CTkLabel(master = self.frame_os_fechada, text = 'Ordens de serviço fechadas', font = ('Roboto', 14))
            self.lbtitle.grid(row = 0, column = 0, padx = 0, pady = 10)

            # 2. Criando a tabela
            table = CTkTable(master=  self.scroll_frame, values=os_fechadas, height=30, width=40)
            table.grid(row=1, column=0, padx=0, pady=20)

            # 3. Opções de seleção
            # Título seleção
            self.lbtitle = ctk.CTkLabel(master = self.frame_os_fechada, text = 'Selecionar:', font = ('Roboto', 14))
            self.lbtitle.grid(row = 3, column = 0, padx = 0, pady = 0)

            # Lista de opções com autopreenchimento
            self.var1 = ctk.StringVar()
            self.selecionar_options_filtro = ctk.CTkOptionMenu(master = self.frame_os_fechada, variable = self.var1, values=['Ordem de serviço', 'Data', 'Cliente', 'Carro', 'Motorista'], width = 225, font=('Roboto', 12),corner_radius=15, command = lambda value: (self.on_combo1_selected(value, self.selecionar_entry)))
            self.selecionar_options_filtro.grid(row = 4, column = 0, padx = 0, pady = 5)
            
            self.selecionar_entry = ctk.CTkEntry(master = self.frame_os_fechada, placeholder_text='', width = 200, font=('Roboto', 12),corner_radius=15)
            self.selecionar_entry.grid(row = 5, column = 0, padx = 0, pady = 5)

            self.selecionar_entry = ctk.CTkEntry(master = self.frame_os_fechada, placeholder_text='', width = 200, font=('Roboto', 12),corner_radius=15)

            # Botão buscar
            self.btn_buscar = ctk.CTkButton(master = self.frame_os_fechada, text= 'Buscar', width = 150, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.selecionar_os(self.frame_os_fechada, self.selecionar_options_filtro, self.selecionar_entry, 'Fechada', self.ver_os_fechada)), fg_color='gray')                       
            self.btn_buscar.grid(row = 6, column = 0, padx = 5, pady = 5)

        except:
            messagebox.showinfo(message='Ainda não há ordens de serviço fechadas.')

        # Botão voltar
        self.btn_voltar = ctk.CTkButton(master = self.frame_os_fechada, text= 'Voltar', width = 150, font=('Roboto', 14), corner_radius= 20, command = lambda: (self.voltar_tela_os(self.frame_os_fechada, self.tela_os)))                       
        self.btn_voltar.grid(row = 7, column = 0, padx = 5, pady = 30)


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
        criterio = selecao.get()
        valor = valor.get()

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

    def editar_os(self, num_os):
        pass

    def fechar_os(self, os):
        pass

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
        

    def imprimir_os(self):
        # Será transformado para pdf --- 
        pass


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