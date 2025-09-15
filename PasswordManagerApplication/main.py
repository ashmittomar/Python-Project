from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # For now, just insert a dummy password (you can expand this later)
    password_entry.delete(0, END)
    password_entry.insert(0, "myStrongPassword123")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        print("Please don’t leave fields empty!")
    else:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        print("Saved successfully!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=0, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=1, column=0)

password_label = Label(text="Password:")
password_label.grid(row=2, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=0, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=1, column=1, columnspan=2)
email_entry.insert(0, "example@email.com")

password_entry = Entry(width=21)
password_entry.grid(row=2, column=1)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=3, column=1, columnspan=2)

window.mainloop()
