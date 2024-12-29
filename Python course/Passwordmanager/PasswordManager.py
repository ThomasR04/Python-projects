from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    pass_lettere= [random.choice(letters) for item in range(0,nr_letters)]
    pass_symbols = [random.choice(symbols) for item in range(0, nr_symbols)]
    pass_numbers = [random.choice(numbers) for item in range(0, nr_numbers)]

    pass_list = pass_numbers + pass_symbols + pass_lettere
    random.shuffle(pass_list)
    password = "".join(pass_list)
    Password_Entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    Website = website_entry.get()
    u_name = Username_entry.get()
    passkey = Password_Entry.get()
    if len(Website) == 0 or len(passkey) == 0:
        messagebox.showerror(message="Please enter a username and website")
    else:
        ok =messagebox.askokcancel(title=Website, message= f"These are the details entered \nEmail: {u_name}\n Password: {passkey}\n Website: {Website} ")
        if ok:
          with open("data.txt", "a") as data_file:
            data_file.write(f"{Website}| {u_name}| {passkey}\n")
            messagebox.showinfo(title="Success", message="Details stored successfully!")
            website_entry.delete(0,END)
            Password_Entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=35,pady=35)
canvas = Canvas(width=200, height=200)
pad_Lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=pad_Lock)
canvas.grid(column=1,row=0)
website = Label(text="Website")
Username = Label(text="Email/Username")
Password = Label(text="Password")
website.grid(row=1, column= 0)
Username.grid(row=2, column=0)
Password.grid(row=3, column=0)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1,row=1, columnspan=2)
Username_entry = Entry(width=35)
Username_entry.insert(0, "Thomasrichmond232@gmail.com")
Username_entry.grid(column=1,row=2, columnspan=2)
Password_Entry = Entry(width=31)
Password_Entry.grid(column=1,row=3)
Add = Button(text="Add", width=36, command= save_password)
Add.grid(column=1, row=4, columnspan=2)
generate_password_button = Button(text= "Generate password", width=20, command=password_generator)
generate_password_button.grid(row=3,column=3)


window.mainloop()