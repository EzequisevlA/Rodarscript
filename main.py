from tkinter import *
from tkinter import ttk
import pyodbc
import os
import pickle

def config_banco():
    Janela_config_instanc = Toplevel(janela_principal)
    Janela_config_instanc.geometry("330x230")
    Label(Janela_config_instanc, text="Informe a instância").place(x=115, y=15)
    instancia = Entry(Janela_config_instanc).place(x=105, y=40)
    Label(Janela_config_instanc, text="Informe o banco").place(x=115, y=90)
    instancia = Entry(Janela_config_instanc).place(x=105, y=115)
    botao_salvar = Button(Janela_config_instanc, text="Salvar")
    botao_salvar.place(x=125, y=180)
    botao_salvar.config(padx=15, pady=5 )

def config_script():

    


    Janela_config_script = Toplevel(janela_principal)
    Janela_config_script.geometry("430x540")
    Label(Janela_config_script, text="Informe a instância").place(x=170, y=15)
    instancia = Entry(Janela_config_script).place(x=170, y=40)
    Label(Janela_config_script, text="Informe o Script").place(x=170, y=90)
    rodar_script = Text(Janela_config_script)
    def salvar_variavel():
        def salvar_variavel():
            texto = rodar_script.get("1.0", "end")
            with open("Script.txt", "w") as arquivo:
                arquivo.write(texto)
        salvar_variavel()

        def carregar_variavel():
            with open("Script.txt", "r") as arquivo:
                texto = arquivo.read()
            rodar_script.delete("1.0", "end")
            rodar_script.insert("1.0", texto)

            rodar_script.insert("1.0", texto)
        carregar_variavel




       
    rodar_script.place(relx = 0.1, rely = 0.2,relwidth = 0.8,relheight=0.70)
    botao_salvar = Button(Janela_config_script, text="Salvar", command=salvar_variavel)
    botao_salvar.place(x=170, y=495)
    botao_salvar.config(padx=15, pady=5 )

    






janela_principal = Tk()
janela_principal.geometry("430x540")
botao_banco_de_dados = Button(janela_principal,text="Instância", command=config_banco)
botao_banco_de_dados.place(x=15,y=10)
botao_banco_de_dados.config(padx=15, pady=5)
Script = Button(janela_principal,text="Script", command=config_script)
Script.configure(padx=20, pady=5, )
Script.place(x=340,y=10)


janela_principal.mainloop()