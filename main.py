from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[choice(letters) for _ in range(randint(8, 10))]
    password_symbols=[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    my_password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    my_password = my_password_entry.get()

    if len(website) == 0 or len(my_password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {my_password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {my_password}\n")
                web_entry.delete(0, END)
                my_password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
web_entry=Entry(width=35)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)

email_label=Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry=Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

my_password_label=Label(text="Password:")
my_password_label.grid(column=0, row=3)
my_password_entry=Entry(width=20)
email_entry.insert(0, "example@gmail.com")
my_password_entry.grid(column=1, row=3)
generate_password_btn=Button(text="Generate For Me", command=generate_password)
generate_password_btn.grid(column=2, row=3)

add_button=Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()