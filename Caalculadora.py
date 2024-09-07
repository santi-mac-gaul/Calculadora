from tkinter import *
from tkinter import ttk
import math

def IngresarValores(tecla):
    if tecla >= "0" and tecla <= "9" or tecla == ')' or tecla == '(' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)
    if tecla == '*' or tecla == '/' or tecla =='+' or tecla == '-':
        
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')

        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')

        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')

        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')

        entrada2.set('')
    if tecla == '=':
        try:
            entrada1.set(entrada1.get() + entrada2.get())
            resultado = eval(entrada1.get())
            if resultado > 15:
                resultado = f'{resultado:.3F}'
                entrada2.set(resultado)
            entrada2.set(resultado)
        except(NameError,SyntaxError,ZeroDivisionError):
            return entrada1.set(''),entrada2.set('Syntaxrror')
def RaizCuadrada():
    entrada1.set('')
    try:
        resultado = math.sqrt(float(entrada2.get()))
        if resultado > 10:
                    resultado = f'{resultado:.3E}'
                    entrada2.set(resultado)
        else:
             entrada2.set(resultado)
    except(NameError,SyntaxError,ZeroDivisionError):
         return entrada1.set(''),entrada2.set('SyntaxError')
def Borrar():
    inicio = 0
    final = len(entrada2.get())
    entrada2.set(entrada2.get()[inicio:final -1])
def BorrarTodo():
     entrada1.set('')
     entrada2.set('')

VentanaRaiz = Tk()
VentanaRaiz.title("Calculadora")
VentanaRaiz.geometry("+500+80")
VentanaRaiz.resizable(0,0)

mainframe = ttk.Frame(VentanaRaiz)
mainframe.grid(column =  0, row = 0, sticky= (W,N,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.columnconfigure(1,weight=1)
mainframe.columnconfigure(2,weight=1)
mainframe.columnconfigure(3,weight=1)
mainframe.rowconfigure(0,weight=1)
mainframe.rowconfigure(1,weight=1)
mainframe.rowconfigure(2,weight=1)
mainframe.rowconfigure(3,weight=1)
mainframe.rowconfigure(4,weight=1)
mainframe.rowconfigure(5,weight=1)
mainframe.rowconfigure(6,weight=1)
mainframe.rowconfigure(7,weight=1)
#estilos frame
estilosframe = ttk.Style()
estilosframe.theme_use('clam')
estilosframe.configure('mainframe.TFrame', background = '#DBDBDB' )
#estilos label
estiloslabel1 = ttk.Style()
estiloslabel1.configure('Label1.TLabel', font= 'arial 15', anchor = "e")

entrada1 = StringVar()
labelEntrada1 = ttk.Label(mainframe, textvariable= entrada1, style = 'Label1.TLabel')
labelEntrada1.grid(column= 0, row=0, columnspan= 4, sticky= (W,N,E,S))

estiloslabel2 = ttk.Style()
estiloslabel2.configure('Label2.TLabel', font= 'arial 40', anchor = "e")

entrada2 = StringVar()
labelEntrada2 = ttk.Label(mainframe,textvariable=entrada2, style='Label2.TLabel')
labelEntrada2.grid(column=0,row=1, columnspan=4, sticky= (W,N,E,S))

estilos_botonesnumericos = ttk.Style()
estilos_botonesnumericos.configure('BotonesNumericos.TButton', font = "arial 22", width = 5, background = '#FFFFFF', relief = 'flat' )

estilosBotones_borrar = ttk.Style()
estilosBotones_borrar.configure('BotonesBorrar.TButton',font = "arial 22", width = 5, background = '#CECECE', relief = 'flat' )

estilosBotones_restantes = ttk.Style()
estilosBotones_restantes.configure('BotonesRestantes.TButton', font = "arial 22", width = 5, background = '#CECECE', relief = 'flat')
#numeros
boton0 = ttk.Button(mainframe, text = 0, style='BotonesNumericos.TButton', command = lambda: IngresarValores("0"))
boton1 = ttk.Button(mainframe, text = 1, style='BotonesNumericos.TButton', command = lambda: IngresarValores("1"))
boton2 = ttk.Button(mainframe, text = 2, style='BotonesNumericos.TButton', command = lambda: IngresarValores("2"))
boton3 = ttk.Button(mainframe, text = 3, style='BotonesNumericos.TButton', command = lambda: IngresarValores("3"))
boton4 = ttk.Button(mainframe, text = 4, style='BotonesNumericos.TButton', command = lambda: IngresarValores("4"))
boton5 = ttk.Button(mainframe, text = 5, style='BotonesNumericos.TButton', command = lambda: IngresarValores("5"))
boton6 = ttk.Button(mainframe, text = 6, style='BotonesNumericos.TButton', command = lambda: IngresarValores("6"))
boton7 = ttk.Button(mainframe, text = 7, style='BotonesNumericos.TButton', command = lambda: IngresarValores("7"))
boton8 = ttk.Button(mainframe, text = 8, style='BotonesNumericos.TButton', command = lambda: IngresarValores("8"))
boton9 = ttk.Button(mainframe, text = 9, style='BotonesNumericos.TButton', command = lambda: IngresarValores("9"))
#signos
boton_borrar = ttk.Button(mainframe, text = '<', style= 'BotonesBorrar.TButton', command= lambda: Borrar())
boton_borrarTodo = ttk.Button(mainframe, text = 'C', style= 'BotonesBorrar.TButton',command= lambda: BorrarTodo())
boton_parentesis1 = ttk.Button(mainframe, text = '(', style= 'BotonesRestantes.TButton', command = lambda: IngresarValores('('))
boton_parentesis2 = ttk.Button(mainframe, text = ')', style= 'BotonesRestantes.TButton', command = lambda: IngresarValores(')'))
boton_punto = ttk.Button(mainframe, text = '.', style= 'BotonesRestantes.TButton')
#operaciones
boton_division = ttk.Button(mainframe, text = '/', style= 'BotonesRestantes.TButton', command = lambda: IngresarValores('/'))
boton_multiplicacion = ttk.Button(mainframe, text = 'x', style= 'BotonesRestantes.TButton', command = lambda: IngresarValores('*'))
boton_resta = ttk.Button(mainframe, text = '-', style= 'BotonesRestantes.TButton', command = lambda: IngresarValores('-'))
boton_suma = ttk.Button(mainframe, text = '+', style= 'BotonesRestantes.TButton', command = lambda: IngresarValores('+'))
#funcion
boton_raiz = ttk.Button(mainframe, text = '√', style= 'BotonesRestantes.TButton', command=lambda:RaizCuadrada())
boton_igual = ttk.Button(mainframe, text= '=', style= 'BotonesRestantes.TButton',command = lambda: IngresarValores('='))
#fila 2'row'
boton_parentesis1.grid(column= 0,row=2, sticky= (W,N,E,S))
boton_parentesis2.grid(column = 1, row=2, sticky= (W,N,E,S))
boton_borrar.grid(column=2,row=2, sticky= (W,N,E,S))
boton_borrarTodo.grid(column=3,row=2, sticky= (W,N,E,S))
#fila 3
boton7.grid(column = 0,row=3, sticky= (W,N,E,S))
boton8.grid(column=1,row=3, sticky= (W,N,E,S))
boton9.grid(column=2,row=3, sticky= (W,N,E,S))
boton_multiplicacion.grid(column=3,row=3, sticky= (W,N,E,S))
#fila 4
boton4.grid(column=0,row=4, sticky= (W,N,E,S))
boton5.grid(column=1,row=4, sticky= (W,N,E,S))
boton6.grid(column=2,row=4, sticky= (W,N,E,S))
boton_division.grid(column=3,row=4, sticky= (W,N,E,S))
#fila 5
boton1.grid(column=0,row=5, sticky= (W,N,E,S))
boton2.grid(column=1,row=5, sticky= (W,N,E,S))
boton3.grid(column=2,row=5, sticky= (W,N,E,S))
boton_suma.grid(column=3,row=5, sticky= (W,N,E,S))
#fila 6
boton0.grid(column=0,row=6,columnspan=2, sticky= (W,N,E,S))
boton_punto.grid(column=2,row=6, sticky= (W,N,E,S))
boton_resta.grid(column=3,row=6, sticky= (W,N,E,S))
#fila7
boton_igual.grid(column=0 ,row=7,columnspan=2, sticky= (W,N,E,S))
boton_raiz.grid(column=2,row=7,columnspan=2, sticky= (W,N,E,S))

for child in mainframe.winfo_children():
    child.grid_configure(ipadx=10,padx=1,pady=1)

VentanaRaiz.mainloop()