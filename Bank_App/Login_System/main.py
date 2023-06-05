from tkinter import *
import os
from PIL import ImageTk, Image

# Main Screen
master = Tk()
master.title('Outcast Banking')
master['bg'] = 'black'
master['border'] = 20
# Disable window resizing
master.resizable(False, False)

#Functions

def reg_done():
    name = temp_name.get()
    surname = temp_surname.get()
    email = temp_email.get()
    cell_no = temp_cell_no.get()
    password = temp_password.get()
    confirm_password = temp_confirm_password.get()
    all_acc = os.listdir()

    if name == "" or surname == "" or email == "" or cell_no == "" or password == "" or confirm_password == "":
        notif.config(fg="maroon", bg = "white", text="All fields are required!")
        return
    
    elif(password != confirm_password):
            notif.config(fg="maroon", bg = "white", text="The Passwords do not match!")
            return
    
    else:
         username = name + surname

    
    
    for user_check in all_acc:
        if username == user_check:
            notif.config(fg="maroon", bg = "white", text="This user already exists!")
            return
        else:
             new_file = open(username, "w+")
             new_file.write(name+"\n")
             new_file.write(surname+"\n")
             new_file.write(email+"\n")
             new_file.write(cell_no+"\n")
             new_file.write(password+"\n")
             new_file.write('0')
             new_file.close()
             notif.config(fg="maroon", bg = "white", text="User account created succefully!")
#======================================   
def register():

    #Instantiating Variables
    global temp_name
    global temp_surname
    global temp_email
    global temp_cell_no
    global temp_password
    global temp_confirm_password
    global notif

    #Declaring variables types
    temp_name = StringVar()
    temp_surname = StringVar()
    temp_email = StringVar()
    temp_cell_no = StringVar()
    temp_password = StringVar()
    temp_confirm_password = StringVar()

    #Register screen
    register_screen = Toplevel(master)
    register_screen.title("Register")
    register_screen['bg'] = 'black'

    #Labels
    # Labels
    Label(register_screen, text="Thank for choosing Outcast Banking", font=('Times New Roman', 15, "bold"), background="black", foreground="white").grid(row=0, sticky=N, pady=10)
    Label(register_screen, text="Please enter your details below:", font=('Times New Roman', 12, "bold"),background="black", foreground="white").grid(row=1, column=0, sticky=N, pady=10)

    #Label Fields
    Label(register_screen, text="Name:", font=('Times New Roman', 12, "bold"),background="black", foreground="white").grid(row=2, column=0, sticky=W, pady=10)
    Label(register_screen, text="Surname:", font=('Times New Roman', 12, "bold"),background="black", foreground="white").grid(row=3, column=0, sticky=W, pady=10)
    Label(register_screen, text="Email:", font=('Times New Roman', 12, "bold"),background="black", foreground="white").grid(row=4, column=0, sticky=W, pady=10)
    Label(register_screen, text="Cell No.:", font=('Times New Roman', 12, "bold"),background="black", foreground="white").grid(row=5, column=0, sticky=W, pady=10)
    Label(register_screen, text="Password:", font=('Times New Roman', 12, "bold"),background="black", foreground="white").grid(row=6, column=0, sticky=W, pady=10)
    Label(register_screen, text="Confirm Password:", font=('Times New Roman', 12, "bold"),background="black", foreground="white").grid(row=7, column=0, sticky=W, pady=10)
    notif = Label(register_screen, font=('Times New Roman', 12, "bold"),background="maroon", foreground="white")
    notif.grid(row=8, column=1, sticky=N, pady=10)

    
      
    #Entries
    Entry(register_screen, textvariable=temp_name, font=('Times New Roman', 12, "bold"),background="maroon", foreground="white").grid(row=2, column=1)
    Entry(register_screen, textvariable=temp_surname, font=('Times New Roman', 12, "bold"),background="maroon", foreground="white").grid(row=3, column=1)
    Entry(register_screen, textvariable=temp_email, font=('Times New Roman', 12, "bold"),background="maroon", foreground="white").grid(row=4, column=1)
    Entry(register_screen, textvariable=temp_cell_no, font=('Times New Roman', 12, "bold"),background="maroon", foreground="white").grid(row=5, column=1)
    Entry(register_screen, textvariable=temp_password, font=('Times New Roman', 12, "bold"),background="maroon", foreground="white", show="*").grid(row=6, column=1)
    Entry(register_screen, textvariable=temp_confirm_password, font=('Times New Roman', 12, "bold"),background="maroon", foreground="white", show="*").grid(row=7, column=1)

    #Buttons
    #Confirm Register Button
    Button(register_screen, text="Register", font=('Times New Roman', 12), width=20, background="maroon",foreground="white", command=reg_done).grid(row=8, sticky=W, pady=10)

def account_details():
     #Account Details screen
    account_details_screen = Toplevel(master)
    account_details_screen.title("Account Details")
    account_details_screen['bg'] = 'black'

def deposit():
     #Account Details screen
    deposit_screen = Toplevel(master)
    deposit_screen.title("Deposit Form")
    deposit_screen['bg'] = 'black'

def withdraw():
     #Account Details screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title("Withdraw Form")
    withdraw_screen['bg'] = 'black'

def log_out():
     #Account Details screen
    log_out_screen = Toplevel(master)
    log_out_screen.title("Log-Out")
    log_out_screen['bg'] = 'black'

def login_session():
    all_acc = os.listdir()
    login_username = temp_login_username.get()
    login_password = temp_login_password.get()

    for username in all_acc:
         if username == login_username:
              file = open(username, "r+")
              file_data = file.read()
              file_data = file_data.split("\n")
              password = file_data[4]
              if login_password != password:
                   login_notif.config(fg="maroon", bg = "white", text="Username or Password is incorrect or user account does not exist.")
                   return
              else:
                   login_notif.config(fg="maroon", bg = "white", text="User logged in succefully!")
                   login_screen.destroy()

                   #Account Dashboard Screen
                   acc_dashboard = Toplevel(master)
                   acc_dashboard.title('Dashboard')
                   acc_dashboard['bg'] = "black"
                   # Labels
                   Label(acc_dashboard, text=("Welcome to " + username + "'s Dashboard"), font=('Times New Roman', 15, "bold"), background="maroon", foreground="white").grid(row=0, sticky=N, pady=10)
                   #Buttons
                   Button(acc_dashboard, text="Account Details", font=('Times New Roman', 12), width=20, background="maroon",foreground="white", command=account_details).grid(row=1, column=0, sticky=W, pady=10)
                   Button(acc_dashboard, text="Deposit", font=('Times New Roman', 12), width=20, background="maroon",foreground="white", command=deposit).grid(row=1, column=1, sticky=W, pady=10)
                   Button(acc_dashboard, text="Withdraw", font=('Times New Roman', 12), width=20, background="maroon",foreground="white", command=withdraw).grid(row=2, column=0, sticky=W, pady=10)
                   Button(acc_dashboard, text="Log_out", font=('Times New Roman', 12), width=20, background="maroon",foreground="white", command=log_out).grid(row=2, column=1, sticky=W, pady=10)
              return
         else:
              login_notif.config(fg="maroon", bg = "white", text="Username or Password is incorrect or user account does not exist.")

def login():
    #Instantiating Variables
    # global temp_name
    # global temp_surname
    global temp_login_password
    global temp_login_username
    global login_notif
    global login_screen

    # #Declaring variables types
    # temp_name = StringVar()
    # temp_surname = StringVar()
    temp_login_password = StringVar()
    temp_login_username = StringVar()

    #LogIn screen
    login_screen = Toplevel(master)
    login_screen.title("Login")
    login_screen['bg'] = 'black'

    #Labels
    # Labels
    Label(login_screen, text="Login Into You Account", font=('Times New Roman', 15, "bold"), background="black", foreground="white").grid(row=0, sticky=N, pady=10)
    Label(login_screen, text="Please enter your details below:", font=('Times New Roman', 12, "bold"),background="black", foreground="white").grid(row=1, column=0, sticky=N, pady=10)

    #Label Fields
    Label(login_screen, text="Username:", font=('Times New Roman', 12, "bold"),background="black", foreground="white").grid(row=2, column=0, sticky=W, pady=10)
    Label(login_screen, text="Password:", font=('Times New Roman', 12, "bold"),background="black", foreground="white").grid(row=3, column=0, sticky=W, pady=10)
    login_notif = Label(login_screen, font=('Times New Roman', 12, "bold"),background="maroon", foreground="white")
    login_notif.grid(row=4, column=0, sticky=N, pady=10)
      
    #Entries
    Entry(login_screen, textvariable=temp_login_username, font=('Times New Roman', 12, "bold"),background="maroon", foreground="white").grid(row=2, column=1)
    Entry(login_screen, textvariable=temp_login_password, font=('Times New Roman', 12, "bold"),background="maroon", foreground="white", show="*").grid(row=3, column=1)

    #Buttons
    #Confirm login Button
    Button(login_screen, text="Login", font=('Times New Roman', 12), width=20, background="maroon",foreground="white", command=login_session).grid(row=5, sticky=W, pady=10)
    Button(login_screen, text="Register", font=('Times New Roman', 12), width=20, background="maroon",foreground="white", command=register).grid(row=5, column=1, sticky=W, pady=10)

# Image Import
img = Image.open('./Login_System/6.png')
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

# Labels
Label(master, text="Welcome to Outcast Banking", font=('Times New Roman', 15, "bold"), background="maroon", foreground="white").grid(row=0, column=0, sticky=N, pady=10)

# Image display
image_label = Label(master, image=img, borderwidth=0)
image_label.grid(row=1, column=0, pady=10)

Label(master, text="Best bank for interspecies transactions.", font=('Times New Roman', 12, "bold"),background="maroon", foreground="white").grid(row=2, column=0, sticky=N, pady=10)

#Buttons
Button(master, text="Login", font=('Times New Roman', 12), width=20, background="maroon", foreground="white", command=login).grid(row=3, column=0, sticky=N, pady=0)
Button(master, text="Register", font=('Times New Roman', 12), width=20, background="maroon",foreground="white", command=register).grid(row=4, column=0, sticky=N, pady=10)

# Start the GUI event loop
master.mainloop()

