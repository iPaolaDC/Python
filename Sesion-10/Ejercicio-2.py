import tkinter as tk

ventana = tk.Tk()
ventana.geometry('300x300')

label = tk.Label(ventana, text="Comida del dia:")
label.grid(column=0, row=1, sticky=tk.W)

listbox = tk.Listbox(ventana)
listbox.grid(column=1, row=2, sticky=tk.W)

lista = ['Spaguetti', 'Arepas', 'Carne', 'Arroz']

for item in lista:
    listbox.insert(tk.END, item)

ventana.mainloop()
