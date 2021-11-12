# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *

# import filedialog module


from tkinter import filedialog

import tkinter as tk

from regex import plot_

from simulator import simulator
from functools import partial
import subprocess


# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("800x650")

# Set window background color
window.config(background="white")

# raiz.configure(bg = 'beige')

# Create a File Explorer label
label_file_explorer = Label(window, text="...", width=50, height=1)



logs = Text(window, height=10, width=80)

# logs['state'] = 'disabled'


filename = ''

def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\JoseK21\\Desktop\\hls", title="Select a File", filetypes=(("Text files", "*.py*"), ("all files", "*.*")))

    
    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename, bg = 'white')

# def browseFiles():
#     filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))

#     # Change label contents
#     label_file_explorer.configure(text="File Opened: " + filename, bg = 'white')

l = []
def print_selection(variable):

    print('variable: ', variable)

    if(variable in l):
        index__ = l.index(variable)

        l.pop(index__)
    else:
        l.append(variable)

    print('----------->', l)

def openNewWindow(vars):
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow,  text ="This is a new window").grid(row=1, column=1)

    global l
    action_with_arg = partial(simulator, l, 200)

    Button(newWindow, text="Run", command= action_with_arg).grid(row=3, column=1)

    c = 1
    for variable in vars:
        c = c + 1

        var1 = tk.IntVar()

        action_with_arg = partial(print_selection, variable)

        c1 = tk.Checkbutton(newWindow, text=variable, variable=var1, onvalue=1, offvalue=0, command= action_with_arg)
        c1.grid(row=2, column=c)


def execute():
    global filename
    print(filename)

    p = subprocess.Popen('python {}'.format(filename), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    c = 0
    for line in p.stdout.readlines():
        c = c + 1
        logs.insert(tk.END, line.decode("utf-8") + "\n")
    retval = p.wait()

    vars = plot_(filename.replace(".py", ".vcd"))

    openNewWindow(vars)



button_explore = Button(window, text="Choose Files", command=browseFiles)
button_explore.configure(bg = 'white')

spinner = Spinbox( window, activebackground="red" )

log_label = Label(window, text = "Logs")

loading_label = Label(window, text = "Loading..")
loading_label.configure(bg = 'white')

log_label.configure(bg = 'white')

button_exit = Button(window, text="Run", command=execute)

# T.insert(tk.END, "Just a text Widget\nin two lines\n")

button_explore.grid(row=1, column=1, padx=10, pady=50)

label_file_explorer.grid(row=1, column=2)

button_exit.grid(row=1, column=4)

loading_label.grid(row=2, column=2)

log_label.grid(row=3, column=1)

logs.grid(row=4, column=2)

# Let the window wait for any events
window.mainloop()
