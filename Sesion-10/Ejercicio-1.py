import tkinter
import tkinter as tk

ventana = tk.Tk()
ventana.geometry('200x150')


def inicio():
    valor_label.config(text="{}".format(lista_items.get()))


# Funcion que reinicia
def reset():
    lista_items.set(None)
    valor_label.config(text='')


# Creamos la lista de opciones
lista = ['Manzanas', 'Pera', 'Uvas', 'Bananas']
# En esta varible se guardan las opciones

lista_items = tkinter.StringVar(value=lista)

# Creamos las opciones con Radiobutton
radio1 = tk.Radiobutton(ventana, text=lista[0], variable=lista_items, value=lista[0], command=inicio)
radio1.grid(column=0, row=0, sticky="W")
radio2 = tk.Radiobutton(ventana, text=lista[1], variable=lista_items, value=lista[1], command=inicio)
radio2.grid(column=0, row=1, sticky="W")
radio3 = tk.Radiobutton(ventana, text=lista[2], variable=lista_items, value=lista[2], command=inicio)
radio3.grid(column=0, row=2, sticky="W")
radio4 = tk.Radiobutton(ventana, text=lista[3], variable=lista_items, value=lista[3], command=inicio)
radio4.grid(column=0, row=3, sticky="W")

# La etiqueta que muestra la opcion
valor_label = tk.Label(ventana)
valor_label.grid(column=1, row=4, sticky="E", padx=40)

# boton de reset
boton_reset = tk.Button(ventana, text="Reinicio", command=reset)
boton_reset.grid(column=0, row=6, sticky="W")

ventana.mainloop()
