# from tkinter import *
# import os
# from PIL import ImageTk, Image

# # Function to handle button click event
# def login():
#     username = username_entry.get()
#     password = password_entry.get()
    
#     # Perform login logic here

# # Main Screen
# master = Tk()
# master.title('Outcast Banking')

# # Image Import
# img = Image.open('./Login_System/6.png')
# img = img.resize((150, 150))
# img = ImageTk.PhotoImage(img)

# # Labels
# Label(master, text="Welcome to Outcast Banking", font=('Times New Roman', 15)).grid(row=0, column=0, sticky=N, pady=10)
# Label(master, text="Best bank for interspecies transactions.", font=('Times New Roman', 12)).grid(row=1, column=0, sticky=N)

# # Image display
# image_label = Label(master, image=img)
# image_label.grid(row=2, column=0, pady=10)

# # Username label and entry field
# Label(master, text="Username:").grid(row=3, column=0, sticky=W, padx=10)
# username_entry = Entry(master)
# username_entry.grid(row=3, column=0, pady=5, padx=90)

# # Password label and entry field
# Label(master, text="Password:").grid(row=4, column=0, sticky=W, padx=10)
# password_entry = Entry(master, show="*")
# password_entry.grid(row=4, column=0, pady=5, padx=90)

# # Login button
# login_button = Button(master, text="Login", command=login)
# login_button.grid(row=5, column=0, pady=10)

# # Start the GUI event loop
# master.mainloop()

# from tkinter import *
# import os
# from PIL import ImageTk, Image

# # Function to handle button click event
# def login():
#     username = username_entry.get()
#     password = password_entry.get()
    
#     # Perform login logic here

# # Main Screen
# master = Tk()
# master.title('Outcast Banking')

# # Image Import
# img = Image.open('./Login_System/6.png')
# img = img.resize((150, 150))
# img = ImageTk.PhotoImage(img)

# # Labels
# Label(master, text="Welcome to Outcast Banking", font=('Times New Roman', 15)).grid(row=0, column=0, columnspan=2, sticky=N, pady=10)
# Label(master, text="Best bank for interspecies transactions.", font=('Times New Roman', 12)).grid(row=1, column=0, columnspan=2, sticky=N)

# # Image display
# image_label = Label(master, image=img)
# image_label.grid(row=2, column=0, columnspan=2, pady=10)

# # Username label and entry field
# Label(master, text="Username:").grid(row=3, column=0, sticky=E, padx=5, pady=5)
# username_entry = Entry(master)
# username_entry.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# # Password label and entry field
# Label(master, text="Password:").grid(row=4, column=0, sticky=E, padx=5, pady=5)
# password_entry = Entry(master, show="*")
# password_entry.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# # Login button
# login_button = Button(master, text="Login", command=login)
# login_button.grid(row=5, column=0, columnspan=2, pady=10)

# # Configure grid weights to make the widgets responsive
# master.columnconfigure(0, weight=1)
# master.columnconfigure(1, weight=1)
# master.rowconfigure(2, weight=1)

# # Start the GUI event loop
# master.mainloop()

from tkinter import *
import os
from PIL import ImageTk, Image

# Function to handle button click event
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Perform login logic here

# Main Screen
master = Tk()
master.title('Outcast Banking')

# Disable window resizing
master.resizable(False, False)

# Image Import
img = Image.open('./Login_System/6.png')
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

# Labels
Label(master, text="Welcome to Outcast Banking", font=('Times New Roman', 15)).grid(row=0, column=0, columnspan=2, sticky=N, pady=10)
Label(master, text="Best bank for interspecies transactions.", font=('Times New Roman', 12)).grid(row=1, column=0, columnspan=2, sticky=N)

# Image display
image_label = Label(master, image=img)
image_label.grid(row=2, column=0, columnspan=2, pady=10)

# Username label and entry field
Label(master, text="Username:").grid(row=3, column=0, sticky=E, padx=5, pady=5)
username_entry = Entry(master)
username_entry.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Password label and entry field
Label(master, text="Password:").grid(row=4, column=0, sticky=E, padx=5, pady=5)
password_entry = Entry(master, show="*")
password_entry.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Login button
login_button = Button(master, text="Login", command=login)
login_button.grid(row=5, column=0, columnspan=2, pady=10)

# Start the GUI event loop
master.mainloop()