#Objetivo: Adicionar os botoes e as funcionalidades de:
    #Potencia
    #Raiz
    #1/x



import tkinter as tk

calculo=str()

def inserir_texto(x):
    global calculo

    calculo=calculo+x
    texto.delete(1.0,"end")
    texto.insert(1.0,calculo)

def avaliar():
    
    global calculo
    a=str(eval(texto.get(1.0,"end")))
    calculo=str()
    inserir_texto(a)

def deletar():
    global calculo

    texto.delete(1.0,"end")
    calculo=str()

def calcular_raiz():
    global calculo
    try:
        resultado = (float(texto.get(1.0, "end")))**0.5
        calculo = str(resultado)
        texto.delete(1.0, "end")
        texto.insert(1.0, calculo)
    except:
        texto.delete(1.0, "end")
        texto.insert(1.0, "Erro")

def calcular_potencia():
    global calculo
    try:
        resultado = eval(texto.get(1.0, "end"))
        resultado = pow(resultado, 2)
        calculo = str(resultado)
        texto.delete(1.0, "end")
        texto.insert(1.0, calculo)
    except:
        texto.delete(1.0, "end")
        texto.insert(1.0, "Erro")

def calcular_inverso():
    global calculo
    try:
        resultado = eval(texto.get(1.0, "end"))
        resultado = 1 / resultado
        calculo = str(resultado)
        texto.delete(1.0, "end")
        texto.insert(1.0, calculo)
    except ZeroDivisionError:
        texto.delete(1.0, "end")
        texto.insert(1.0, "Divisão por zero")
    except:
        texto.delete(1.0, "end")
        texto.insert(1.0, "Erro")



janela=tk.Tk()
janela.geometry("590x570")
texto=tk.Text(janela, height=4, width=26, font=("Arial", 24))
texto.grid(columnspan=6)
botao1=tk.Button(janela,text="1", command=lambda:inserir_texto("1"), width=12,height=4, font=("Arial",12))
botao1.grid(column=1,row=2)
botao2=tk.Button(janela,text="2", command=lambda:inserir_texto("2"), width=12,height=4, font=("Arial",12))
botao2.grid(column=2,row=2)
botao3=tk.Button(janela,text="3", command=lambda:inserir_texto("3"), width=12,height=4, font=("Arial",12))
botao3.grid(column=3,row=2)
botao4=tk.Button(janela,text="4", command=lambda:inserir_texto("4"), width=12,height=4, font=("Arial",12))
botao4.grid(column=1,row=3)
botao5=tk.Button(janela,text="5", command=lambda:inserir_texto("5"), width=12,height=4, font=("Arial",12))
botao5.grid(column=2,row=3)
botao6=tk.Button(janela,text="6", command=lambda:inserir_texto("6"), width=12,height=4, font=("Arial",12))
botao6.grid(column=3,row=3)
botao7=tk.Button(janela,text="7", command=lambda:inserir_texto("7"), width=12,height=4, font=("Arial",12))
botao7.grid(column=1,row=4)
botao8=tk.Button(janela,text="8", command=lambda:inserir_texto("8"), width=12,height=4, font=("Arial",12))
botao8.grid(column=2,row=4)
botao9=tk.Button(janela,text="9", command=lambda:inserir_texto("9"), width=12,height=4, font=("Arial",12))
botao9.grid(column=3,row=4)
botao0=tk.Button(janela,text="0", command=lambda:inserir_texto("0"), width=12,height=4, font=("Arial",12))
botao0.grid(column=2,row=5)

botao_mais=tk.Button(janela,text="+", command=lambda:inserir_texto("+"), width=12,height=4, font=("Arial",12))
botao_mais.grid(column=4,row=2)

botao_menos=tk.Button(janela,text="-", command=lambda:inserir_texto("-"), width=12,height=4, font=("Arial",12))
botao_menos.grid(column=4,row=3)

botao_vezes=tk.Button(janela,text="*", command=lambda:inserir_texto("*"), width=12,height=4, font=("Arial",12))
botao_vezes.grid(column=4,row=4)

botao_dividir=tk.Button(janela,text="/", command=lambda:inserir_texto("/"), width=12,height=4, font=("Arial",12))
botao_dividir.grid(column=4,row=5)

botao_abrepar=tk.Button(janela,text="(", command=lambda:inserir_texto("("), width=12,height=4, font=("Arial",12))
botao_abrepar.grid(column=1,row=5)

botao_fechapar=tk.Button(janela,text=")", command=lambda:inserir_texto(")"), width=12,height=4, font=("Arial",12))
botao_fechapar.grid(column=3,row=5)

botao_apagar=tk.Button(janela,text="C", command=lambda:deletar(), width=12,height=4, font=("Arial",12))
botao_apagar.grid(column=5,row=2)

botao_igual=tk.Button(janela,text="=", command=lambda:avaliar(), width=12,height=4, font=("Arial",12))
botao_igual.grid(column=5,row=3)

botao_raiz = tk.Button(janela, text="√", command=calcular_raiz, width=12, height=4, font=("Arial", 12))
botao_raiz.grid(column=5, row=4)

botao_potencia = tk.Button(janela, text="²", command=calcular_potencia, width=12, height=4, font=("Arial", 12))
botao_potencia.grid(column=5, row=5)

botao_inverso = tk.Button(janela, text="1/x", command=calcular_inverso, width=12, height=4, font=("Arial", 12))
botao_inverso.grid(column=5, row=6)

janela.mainloop()