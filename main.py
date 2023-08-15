import random
import tkinter as tk
from tkinter import messagebox

# password characters lists
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = int(letters_entry.get())
    nr_symbols = int(symbols_entry.get())
    nr_numbers = int(numbers_entry.get())

    # password list
    password = []

    # generate random letters
    for _ in range(nr_letters):
        random_let = random.choice(letters)
        password.append(random_let)

    # generate random symbols
    for _ in range(nr_symbols):
        random_sym = random.choice(symbols)
        password.append(random_sym)

    # generate random numbers
    for _ in range(nr_numbers):
        random_num = random.choice(numbers)
        password.append(random_num)

    # generate random password(letters+symbols+numbers)
    random.shuffle(password)

    # make password list to string
    password_str = "".join(password)

    # display password in the field
    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password_str)
    password_entry.config(state="readonly")

# create main window
window = tk.Tk()
window.title("Password Generator by Fred Wong")

# add labels and input field
letters_label = tk.Label(window, text="How many letters do you want?:")
letters_label.pack()
letters_entry = tk.Entry(window)
letters_entry.pack()

symbols_label = tk.Label(window, text="How many symbols do you want?:")
symbols_label.pack()
symbols_entry = tk.Entry(window)
symbols_entry.pack()

numbers_label = tk.Label(window, text="how many numbers do you want?:")
numbers_label.pack()
numbers_entry = tk.Entry(window)
numbers_entry.pack()

# add generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# add password display field
password_label = tk.Label(window, text="Here is your password:")
password_label.pack()
password_entry = tk.Entry(window, state="readonly")
password_entry.pack()

# run mainloop
window.mainloop()