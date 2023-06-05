import tkinter as tk
import tkinter.font as font
from tkinter import *



window = tk.Tk()
window.title("Practise Positioning")
window.geometry("480x500")
window['bg']='black'

my_h1 = font.Font(
    family='Times New Roman',
    size=15,
    weight="bold",
    )

myfont = font.Font(
    family='Times New Roman',
    size=10,
    weight="bold",
    )

greeting = tk.Label(
    text = "Welcome to the Notascam Transfer",
    foreground="#2E9EE5",
    background="black",
    width=25,
    height=10,
    font=my_h1 
)

greeting.config(anchor=CENTER)
greeting.place(
    x=0, y=0
)
greeting.pack()


btn_view_balance = (tk.Button(
    text="View Balance",
    wraplength=50,
    width=30,
    height=5,
    font=myfont, 
    background="#2E9EE5"
)).place(
    x=10, y=200
)

btn_withdraw = (tk.Button(
    text="Withdraw",
    wraplength=60,
    width=30,
    height=5,
    font=myfont,
    background="#2E9EE5"
)).place(
    x=10, y=300
)

btn_deposit = (tk.Button(
    text="Deposit",
    wraplength=50,
    width=30,
    height=5,
    font=myfont,
    background="#2E9EE5"
)).place(
    x=250, y=200
)

btn_financial_calculator = (tk.Button(
    text="Financial Calculator",
    wraplength=60,
    width=30,
    height=5,
    font=myfont,
    background="#2E9EE5"
)).place(
    x=250, y=300
)

window.mainloop()