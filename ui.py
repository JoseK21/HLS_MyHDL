# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog

# Function for opening the
# file explorer window


def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename, bg = 'white')

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename, bg = 'white')


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

button_explore = Button(window, text="Choose Files", command=browseFiles)
button_explore.configure(bg = 'white')

button_exit = Button(window, text="Run", command=exit)

spinner = Spinbox( window, activebackground="red" )

log_label = Label(window, text = "Logs")

loading_label = Label(window, text = "Loading..")
loading_label.configure(bg = 'white')

log_label.configure(bg = 'white')

logs = Text(window, height=10, width=80)

# T.insert(tk.END, "Just a text Widget\nin two lines\n")

button_explore.grid(row=1, column=1, padx=10, pady=50)

label_file_explorer.grid(row=1, column=2)

button_exit.grid(row=1, column=4)

loading_label.grid(row=2, column=2)

log_label.grid(row=3, column=1)

logs.grid(row=4, column=2)

# Let the window wait for any events
window.mainloop()
