from tkinter import *

janela = Tk()

class Application():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        # criando o Loop
        janela.mainloop()

    def tela(self):
        self.janela.title("Cadastro de Clientes")
        self.janela.configure(background= '#708090')
        self.janela.geometry("900x600")
        self.janela.resizable(True, True)
        self.janela.maxsize(width=900, height=600)
        self.janela.minsize(width=500, height=300)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.janela, bd=4, bg= '#759fe6', highlightbackground= '#B0C4DE', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.66)
        #self.frame_1.place(x=50, y=50, width=100, height=100)
        #self.frame_1.pack(side="top")

        self.frame_2 = Frame(self.janela, bd=4, bg='#759fe6', highlightbackground= '#B0C4DE', highlightthickness=2)

        self.frame_2.place(relx=0.02, rely=0.7, relwidth=0.96, relheight=0.29)
    #botoes
    def criando_botoes(self):
        #Nome
        self.bt_nome = Label(self.frame_1, text='Nome:', bg= '#759fe6', font = ('verdana', 8, 'bold'))
        self.bt_nome.place(relx=0.01, rely=0.002, relwidth=0.05, relheight=0.05)

        self.bt_nome = Entry(self.frame_1)
        self.bt_nome.place(relx=0.01, rely=0.06, relwidth=0.40, relheight=0.07)

        #Telefone
        self.bt_tel = Label(self.frame_1, text='Telefone:', bg= '#759fe6', font = ('verdana', 8, 'bold'))
        self.bt_tel.place(relx=0.385, rely=0.002, relwidth=0.15, relheight=0.05)

        self.bt_tel = Entry(self.frame_1)
        self.bt_tel.place(relx=0.425, rely=0.06, relwidth=0.15, relheight=0.07)

        #email
        self.bt_email = Label(self.frame_1, text='Email:', bg= '#759fe6', font = ('verdana', 8, 'bold'))
        self.bt_email.place(relx=0.59, rely=0.002, relwidth=0.05, relheight=0.05)

        self.bt_email = Entry(self.frame_1)
        self.bt_email.place(relx=0.59, rely=0.06, relwidth=0.40, relheight=0.07)



        #bairro
        self.bt_bairro = Label(self.frame_1, text='Bairro:', bg= '#759fe6', font = ('verdana', 8, 'bold'))
        self.bt_bairro.place(relx=0.012, rely=0.14, relwidth=0.05, relheight=0.05)

        self.bt_bairro = Entry(self.frame_1)
        self.bt_bairro.place(relx=0.01, rely=0.19, relwidth=0.275, relheight=0.07)

        #rua
        self.bt_rua = Label(self.frame_1, text='Rua:', bg= '#759fe6', font = ('verdana', 8, 'bold'))
        self.bt_rua.place(relx=0.292, rely=0.14, relwidth=0.05, relheight=0.05)

        self.bt_rua = Entry(self.frame_1)
        self.bt_rua.place(relx=0.30, rely=0.19, relwidth=0.375, relheight=0.07)

        #numero
        self.bt_num = Label(self.frame_1, text= 'Nº:', bg= '#759fe6', font = ('verdana', 8, 'bold'))
        self.bt_num.place(relx=0.677, rely=0.14, relwidth=0.05, relheight=0.05)

        self.bt_num = Entry(self.frame_1)
        self.bt_num.place(relx=0.690, rely=0.19, relwidth=0.14, relheight=0.07)

        #cep
        self.bt_cep = Label(self.frame_1, text='CEP:', bg= '#759fe6', font = ('verdana', 8, 'bold'))
        self.bt_cep.place(relx=0.84, rely=0.14, relwidth=0.05, relheight=0.05)

        self.bt_cep = Entry(self.frame_1)
        self.bt_cep.place(relx=0.85, rely=0.19, relwidth=0.14, relheight=0.07)

        #Nome do Tec
        self.bt_tec = Label(self.frame_1, text='Nome do Técnico:', bg= '#759fe6', font = ('verdana', 8, 'bold'))
        self.bt_tec.place(relx=0.01, rely=0.28, relwidth=0.14, relheight=0.05)

        self.bt_tec = Entry(self.frame_1)
        self.bt_tec.place(relx=0.01, rely=0.33, relwidth=0.40, relheight=0.07)

        #Responsavel pela visita Técnica?
        self.bt_rep = Label(self.frame_1, text='Quem é o responsável pela visita tec?', bg= '#759fe6',
                            font = ('verdana', 8, 'bold'))
        self.bt_rep.place(relx=0.586, rely=0.28, relwidth=0.30, relheight=0.05)

        self.bt_rep = Entry(self.frame_1)
        self.bt_rep.place(relx=0.59, rely=0.33, relwidth=0.40, relheight=0.07)

        #Quais foram os defeitos encontrados no local:
        self.bt_def = Label(self.frame_1, text= 'Quais foram os defeitos encontrados no local:', bg= '#759fe6',
                            font = ('verdana', 8, 'bold'))
        self.bt_def.place(relx=0.01, rely=0.41, relwidth=0.35, relheight=0.05)

        self.bt_def = Entry(self.frame_1)
        self.bt_def.place(relx=0.01, rely=0.46, relwidth=0.40, relheight=0.07)

        #Função dele no local?
        self.bt_fun = Label(self.frame_1, text='Função dele no local?', bg= '#759fe6', font = ('verdana', 8, 'bold'))
        self.bt_fun.place(relx=0.59, rely=0.54, relwidth=0.165, relheight=0.05)

        self.bt_fun = Entry(self.frame_1)
        self.bt_fun.place(relx=0.59, rely=0.59, relwidth=0.40, relheight=0.07)


        #Quais foram os defeitos encontrados no local
        self.bt_feito = Label(self.frame_1, text='O que foi feito:', bg= '#759fe6', font = ('verdana', 8, 'bold'))
        self.bt_feito.place(relx=0.01, rely=0.54, relwidth=0.115, relheight=0.05)

        self.bt_feito = Entry(self.frame_1)
        self.bt_feito.place(relx=0.01, rely=0.59, relwidth=0.40, relheight=0.07)

        #Algum material foi trocado?
        self.bt_material = Label(self.frame_1, text='Algum material foi trocado?', bg= '#759fe6',
                                 font = ('verdana', 8, 'bold'))
        self.bt_material.place(relx=0.59, rely=0.41, relwidth=0.212, relheight=0.05)

        self.bt_material = Entry(self.frame_1)
        self.bt_material.place(relx=0.59, rely=0.46, relwidth=0.40, relheight=0.07)


        #Os equipamentos revisados estão funcionando?
        self.bt_equipamento = Label(self.frame_1, text='Os equipamentos revisados estão funcionando?', bg= '#759fe6',
                                    font = ('verdana', 8, 'bold'))
        self.bt_equipamento.place(relx=0.01, rely=0.67, relwidth=0.37, relheight=0.05)

        self.bt_equipamento = Entry(self.frame_1)
        self.bt_equipamento.place(relx=0.01, rely=0.72, relwidth=0.40, relheight=0.07)

        #Quais materiais foram trocados?
        self.bt_troca = Label(self.frame_1, text='Quais materiais foram trocados?', bg= '#759fe6',
                              font = ('verdana', 8, 'bold'))
        self.bt_troca.place(relx=0.59, rely=0.67, relwidth=0.25, relheight=0.05)

        self.bt_troca = Entry(self.frame_1)
        self.bt_troca.place(relx=0.59, rely=0.72, relwidth=0.40, relheight=0.07)

        #Algum valor deste serviço será cobrado?
        self.bt_valor = Label(self.frame_1, text='Algum valor deste serviço será cobrado?',  bg= '#759fe6',
                              font = ('verdana', 8, 'bold'))
        self.bt_valor.place(relx=0.01, rely=0.80, relwidth=0.32, relheight=0.05)

        self.bt_valor = Entry(self.frame_1)
        self.bt_valor.place(relx=0.01, rely=0.85, relwidth=0.40, relheight=0.07)

        #Alguns desses materiais tem garantia?
        self.bt_garantia = Label(self.frame_1, text='Alguns desses materiais tem garantia?',  bg= '#759fe6',
                              font = ('verdana', 8, 'bold'))
        self.bt_garantia.place(relx=0.59, rely=0.80, relwidth=0.30, relheight=0.05)

        self.bt_troca = Entry(self.frame_1)
        self.bt_troca.place(relx=0.59, rely=0.85, relwidth=0.40, relheight=0.07)



        #criar pdf
        self.bt_pdf = Button(self.frame_1, text='Criar PDF', bd=4, bg = '#708090',fg = 'white'
                                , font = ('verdana', 8, 'bold'))
        self.bt_pdf.place(relx=0.425, rely=0.93, relwidth=0.15, relheight=0.07)

        #observações
        self.bt_observações = Label(self.frame_2,text='Observações:', bg = '#759fe6', font = ('verdana', 8, 'bold'))
        self.bt_observações.place(relx=0.001, rely=0.002, relwidth=0.13, relheight=0.10)

        self.bt_observações = Entry(self.frame_2)
        self.bt_observações.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.84)


Application()
