#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

# import filedialog module
from tkinter import filedialog

# Crea una clase Python para definir el interfaz de usuario de
# la aplicación. Cuando se cree un objeto del tipo 'Aplicacion'
# se ejecutará automáticamente el método __init__() qué 
# construye y muestra la ventana con todos sus widgets: 

# Function for opening the
# file explorer window
def browseFiles(label_file_explorer):
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)

class Aplicacion():
    def __init__(self):
        raiz = Tk()
        raiz.geometry('800x650')
        raiz.configure(bg = 'beige')
        raiz.title('Aplicación')

        # Create a File Explorer label
        label_file_explorer = Label(raiz,
                                    text = "File Explorer using Tkinter",
                                    width = 100, height = 4,
                                    fg = "blue")
        
            
        button_explore = Button(raiz,
                                text = "Browse Files",
                                command = browseFiles(label_file_explorer))

        ttk.Button(raiz, text='Salir', 
                   command=raiz.destroy).pack(side=BOTTOM)
        raiz.mainloop()

# Define la función main() que es en realidad la que indica 
# el comienzo del programa. Dentro de ella se crea el objeto 
# aplicación 'mi_app' basado en la clase 'Aplicación':

def main():
    mi_app = Aplicacion()
    return 0

# Mediante el atributo __name__ tenemos acceso al nombre de un
# un módulo. Python utiliza este atributo cuando se ejecuta
# un programa para conocer si el módulo es ejecutado de forma
# independiente (en ese caso __name__ = '__main__') o es 
# importado:

if __name__ == '__main__':
    main()