import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyperclip
import random

window = tk.Tk()
window.title("Password Manager")
window.minsize(380,380)
window.configure(background="white", padx=30, pady=30)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, "end")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    web      = web_entry.get()
    email    = email_entry.get()
    password = password_entry.get()

    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill all fields")

    else:
        is_ok = messagebox.askokcancel(title=f"for {web}", message=f"\nEmail:        {email}"
                                                          f"\nPassword: {password}\n"
                                                          f"\nIs it ok to save ?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{web}\t | \t{email}\t | \t{password} \n")
                messagebox.showinfo("Success", "Password has been saved")
                web_entry.delete(0, "end")
                email_entry.delete(0, "end")
                password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
pic = tk.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=pic)
canvas.grid(row=0, column=0, padx=20, pady=20, columnspan=3)

label_web = tk.Label(text="Website:", bg="white")
label_web.grid(row=1, column=0, sticky="w", padx=10, pady=5)

web_entry = ttk.Entry(width=40)
web_entry.grid(row=1, column=1, columnspan=2, pady=5)

label_email = tk.Label(text="Email/Username:", bg="white")
label_email.grid(row=2, column=0, sticky="w", padx=10, pady=5)

email_entry = ttk.Entry(width=40)
email_entry.insert(0,"")
email_entry.grid(row=2, column=1, columnspan=2, pady=5)

label_password = tk.Label(text="Password:", bg="white")
label_password.grid(row=3, column=0, sticky="w", padx=10, pady=5)

password_entry = ttk.Entry(width=21)
password_entry.grid(row=3, column=1)

genpass = ttk.Button(text="Generate Password",command=generate_password)
genpass.grid(row=3, column=2)

add_button = ttk.Button(text="Add",width=40, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, pady=10)


window.mainloop()


