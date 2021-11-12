# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *

# import filedialog module


from tkinter import filedialog, scrolledtext, messagebox

import tkinter as tk

from numpy import integer

from regex import plot_

from simulator import simulator
from functools import partial
import subprocess

# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
# window.geometry("800x650")

# Set window background color
window.config(background="white", padx=30)
window.resizable(width=False, height=False)
filename = ''

l = []

loading_label = Label(window, text = "", bg = 'white')

def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\JoseK21\\Desktop\\hls", title="Select a File", filetypes=(("Text files", "*.py*"), ("all files", "*.*")))

    
    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename, bg = 'white')

def print_selection(variable):
    if(variable in l):
        index__ = l.index(variable)

        l.pop(index__)
    else:
        l.append(variable)

def openNewWindow(vars, franco):
    global l
    c = 1
    for variable in vars:
        c = c + 1

        var1 = tk.IntVar()

        action_with_arg = partial(print_selection, variable)

        c1 = tk.Checkbutton(f, text=variable, variable=var1, onvalue=1, offvalue=0, command= action_with_arg)
        c1.grid(row=1, column=c)

    action_with_arg = partial(simulator, l, int(franco))
    Button(f, text="Run Simulation", command= action_with_arg).grid(row=1, column=c+1, padx=10)

import time

def execute():
    global filename
    import os.path
    extension = os.path.splitext(filename)[1]

    if extension == '.py':
        p = subprocess.Popen('python {}'.format(filename), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        c = 0
        
        logs['state'] = 'normal'
        for line in p.stdout.readlines():
            c = c + 1
            logs.insert(tk.END, line.decode("utf-8") + "\n")
        retval = p.wait()
        
        logs['state'] = 'disable'

        filename2 = os.path.basename(filename)
        print(filename2)
        vars, franco = plot_( "./"+ filename2.replace(".py", ".vcd"))

        if(franco == "-1"):
            messagebox.showinfo(message="Error> file .vcd doesn't exits | myHDL logic is wrong ", title="Error")
        else:
            openNewWindow(vars, franco)   
    else:
        messagebox.showinfo(message="Error> Wrong extension | Should be.py", title="Error")

label_file_explorer = Label(window, text="...", width=50, height=1)

logs = scrolledtext.ScrolledText(window, height=20, width=80)

button_explore = Button(window, text="Choose File (.py)", command=browseFiles)
button_explore.configure(bg = 'white')

spinner = Spinbox( window, activebackground="red" )

log_label = Label(window, text = "Logs", anchor="e", bg = 'white')

button_exit = Button(window, text="Run", command= execute, bg='#3c9e41')

button_explore.grid(row=1, column=1, pady=50)

label_file_explorer.grid(row=1, column=2)

button_exit.grid(row=1, column=3)

loading_label.grid(row=2, column=2)

log_label.grid(row=3, column=1)

logs.grid(row=4, column=1, columnspan=3)

logs['state'] = 'disable'

f = Frame(window, bg="white", height=200, width=650, pady=30)
f.grid(row=5, column=1, columnspan=3)

window.mainloop()
