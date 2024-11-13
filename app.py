import tkinter as tk
from tkinter import ttk

# Inicializando
window_login = tk.Tk()
window_login.title('Login Window')

# Sign in

'''
Sign in

1. Title
2. Input Lines
3. Buttons for access or sign up
'''

# 1. Title
label_title_window_login = tk.Label(window_login, text='Sign In')
label_title_window_login.grid(row=0,column=1)

# 2. Input Lines
label_email = tk.Label(window_login, text='Email:').grid(row=1)
label_password = tk.Label(window_login, text='Password: ').grid(row=2)

# Locate Input Lines
entry_email = tk.Entry(label_email)
entry_email.grid(row=1, column=1)

entry_password = tk.Entry(label_password, show='*')
entry_password.grid(row=2, column=1)

# Get Values for Input Lines
def get_login():
    
    email_value = entry_email.get()
    password_value = entry_password.get()

    return email_value, password_value

# 3. Button for Sing In and Sing Up

# Sing In
button_singin = tk.Button(window_login, text='Sing In', command=get_login)
button_singin.grid(row=3, column=0)

# Sing Up
button_singup = tk.Button(window_login, text='Sing Up')
button_singup.grid(row=3, column=1)

# Mantendo a janela 
window_login.mainloop()