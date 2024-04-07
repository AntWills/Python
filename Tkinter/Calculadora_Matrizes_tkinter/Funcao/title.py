import tkinter as tk
from tkinter import *

def printTitle(frame):
    title = Frame(frame)
    title.configure(borderwidth=2, relief='solid')
    title.pack(padx=10, pady=10)

    label_title = tk.Label(title, text='Matriz', font=('Arial', 40))
    label_title.pack(padx=10,pady=10)
    