# Create your first GUI application
# First, we will import Tkinter package and create a window and set its title:

from tkinter import *

from tkinter import ttk

window = Tk()

window.title("Welcome to LikeGeeks app")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='First')

tab_control.add(tab2, text='Second')

lbl1 = Label(tab1, text= 'label1')

lbl1.grid(column=0, row=0)

lbl2 = Label(tab2, text= 'label2')

lbl2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

window.mainloop()

window.mainloop()

# from tkinter import *
#
# main_window = Tk()
# # Labels
# Label(main_window, text="Enter your name").grid(row=0, column=0)
# Label(main_window, text="Enter your age").grid(row=1, column=0)
# # Text input
# My_name = Entry(main_window, width=50, borderwidth=5).grid(row=0, column=2)
# My_age = Entry(main_window, width=50, borderwidth=5).grid(row=1, column=2)
# # My_name.get(row=0, column=2)
# # My_age.get(row=1, column=2)
#
#
# def on_click():
#     print(f"My name is {My_name}, and My age is {My_age}")
#
#
# # Buttons
# Button(main_window, text="Click me", command=on_click()).grid(row=2, column=1)

# main_window.mainloop()
