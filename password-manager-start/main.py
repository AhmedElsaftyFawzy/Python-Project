from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_number + password_symbol

    shuffle(password_list)

    password = "".join(password_list)

    pass_entery.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_entry.get()
    user = user_entery.get()
    password = pass_entery.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title= "Ooops",message="Don't Leave Any Field Empty")
    else:
    
        is_ok = messagebox.askokcancel(title=website, message=f"This The Detail That You Entered: \nUser: {user}\nPassword: {password} \nIs It Ok To Save ??")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {user} | {password}\n")

            web_entry.delete(0, END)
            pass_entery.delete(0, END)    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

app_image = PhotoImage(file="logo.png")
canvas = Canvas(width= 200 , height=200)
canvas.create_image(100, 100, image=app_image)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

web_entry = Entry(width=42)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

user_entery = Entry(width=42)
user_entery.grid(column=1, row=2, columnspan=2)
user_entery.insert(0, "ahmed@gmail.com")

pass_entery = Entry(width=24)
pass_entery.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="ADD" ,width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()