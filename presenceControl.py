from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
import os
from datetime import datetime
import csv
#import numpy as np
#import pandas as pd


#Dicionario Utilizado
# Obtendo local dos arquivos
pastaApp = os.path.dirname(__file__)

#Lista que será usada para armazenar a presença.
#dadosUpdate = []

#Recolhendo nomes a partir do ID
listaN = []
listaS = []
with open(pastaApp+"//dados.csv", "r") as file:
    rd = csv.DictReader(file)
    for linha in rd:
        #print("{0} - {1}".format(linha['Nome'], linha['ID']))
        PessoaNome = (linha['ID'], linha['Nome'])
        PessoaSenha = (linha['ID'], linha['Senha'])
        listaN.append(PessoaNome)
        listaS.append(PessoaSenha)
        dadosDictN = dict(listaN)
        dadosDictS = dict(listaS)
    #print(dadosDict)

#Função para validar os dados
def valida(senha, ID):

    if senha == dadosDictS[ID]:
        return True
    else:
        return False
'''
def salvaDados(valor):
    dadosUpdate.append(valor)
    tabela = pd.DataFrame(list, columns= ["ID", "Nome", "Data", "Horário"])
    tabela.to_excel("ControleDePresenca.xlsx")
'''
def cadastraPresenca(tv):
    ID = userID.get()
    senha = userPass.get()
    Nome = dadosDictN[ID]
    Data = datetime.today().strftime('%Y-%m-%d')
    Hora = datetime.today().strftime('%H-%M')

    valor = [ID, Nome, Data, Hora]
    
    #print(ID + ',' + senha)
    if valida(senha, ID) == True:
        tv.insert("","end",values=valor)
        userID.delete(0,END)
        userPass.delete(0, END)
        exec(open(pastaApp+"//progressBar.py").read(), {'varBarra':varBarra})
        tv.update()
        messagebox.showinfo(title='Controle de Presença', message=msg_loginEfetuado)
        #salvaDados(valor)
    else:
        messagebox.showerror(title='Controle de Presença', message=msg_error)
app = tk.Tk()

imgWorkspace=PhotoImage(file=pastaApp+"//workBitch21.gif")
work_gif=Label(app, image=imgWorkspace, background='#43a173')
work_gif.place(x=250, y=60)


imgLogo=PhotoImage(file=pastaApp+"//logoP2.png")
logo=Label(app, image=imgLogo, background='#43a173')
logo.place(x=10, y=10, width=100, height=45)

app.tk.call('wm', 'iconphoto', app._w, tk.PhotoImage(file=pastaApp+"//logoP.png"))

garamInfo = tkFont.Font(family='Garamond', size=10, weight=tkFont.NORMAL)
garamTitle = tkFont.Font(family='Garamond', size=22, weight=tkFont.BOLD)

app.title("ESF Viçosa - Controle de Presença")
app.geometry("600x450")
app.resizable(0, 0)
app.configure(background="#43A173")

msg_loginEfetuado = "Presença cadastrada com sucesso!"
msg_error = "Falha ao tentar cadastrar presença, confira as informações inseridas. Em caso de dúvidas contatar a Diretoria de Qualidade!"

barraDeMenus = Menu(app)

menuArquivo = Menu(barraDeMenus, tearoff=0)
menuArquivo.add_command(label="Opção 1")
menuArquivo.add_command(label="Opção 2")
menuArquivo.add_command(label="Opção 3")
barraDeMenus.add_cascade(label="Arquivo",menu=menuArquivo)

menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label="Opção 1")
menuSobre.add_command(label="Opção 2")
barraDeMenus.add_cascade(label="Sobre",menu=menuSobre)

app.config(menu=barraDeMenus)

legend = Label(app, text="Olá sem fronteiras!", background="#43a173", font=garamTitle)
legend.place(x=100, y=10, width=400, height=80)

#Criando treeview

tv=ttk.Treeview(app, columns=('C_id', 'C_name', 'C_date', 'C_hour'), show='headings')
tv.column('C_id', minwidth=0, width=40)
tv.column('C_name', minwidth=0, width=280)
tv.column('C_date', minwidth=0, width=90)
tv.column('C_hour', minwidth=0, width=90)

tv.heading('C_id', text= 'ID', anchor='w')
tv.heading('C_name', text= 'Nome', anchor='w')
tv.heading('C_date', text= 'Data', anchor='w')
tv.heading('C_hour', text= 'Horário', anchor='w')

tv.place(x=50, y=250, width=500, height=150)

# Definindo entrada do usuário
vUser=StringVar()
vsenha=StringVar()

legend = Label(app, text="ID de Usuário:", background="#43a173", font=garamInfo)
#legend.place(x=220, y=85, width=100, height=15)
legend.place(x=50, y=85, width=100, height=15)
userID = Entry(app, textvariable=vUser)
#userID.place(x=220, y=103, width=160, height=20)
userID.place(x=50, y=103, width=160, height=20)

legend = Label(app, text="Senha:", background="#43a173", font=garamInfo)
#legend.place(x=220, y=128, width=50, height=15)
legend.place(x=50, y=128, width=50, height=15)
userPass = Entry(app, textvariable=vsenha, show="*")
#userPass.place(x=220, y=146, width=160, height=20)
userPass.place(x=50, y=146, width=160, height=20)

btn_verifSenha=Button(app, text="Confirmar Presença", command=lambda:cadastraPresenca(tv))
#btn_verifSenha.place(x=220, y=179, width=160, height=25)
btn_verifSenha.place(x=50, y=179, width=160, height=25)

varBarra=DoubleVar()
varBarra.set(0)

app.mainloop()


