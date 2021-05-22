import tkinter
import tkinter.messagebox as messagebox
import random
import pyperclip


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def GeneratePassword():
    print("password generated")
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    
    password_entry.delete(0, len(password_entry.get()))
    password_entry.insert(0, password)
    
    pyperclip.copy(password)
    messagebox.showinfo(title= "yayee!", message="Password Generated and Copied to Clipboard")
    
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def SavePassword():    
    #get all the text in the entries
    website_name = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    
    
    #return if some info are missing
    if len(website_name) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title= "Uh oh!", message= "You have not entered the required info!")
        return
    
    
    msg = messagebox.askokcancel(title= website_name, message= f"These are the details entered: \n Email:{email} \n Password: {password} \n Is it ok to save?")
    
    #save the message if return true (ok), otherwise false (cancel)
    if msg == False:
        print("password not saved")
        return
    
    print("password saved")
    #writes the information in the text file
    with open('password.txt','a') as file:
        file.write(f"{website_name} | {email} | {password} \n")
    file.close
    
    #delete the information on the entries
    website_entry.delete(0, len(website_name))
    email_username_entry.delete(0, len(email))
    password_entry.delete(0, len(password))
    
    #refocu the cursor back to the website entry
    website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("PW Manager")
window.config(padx=50, pady= 50)

canvas = tkinter.Canvas(width= 200, height= 200)
lock_img = tkinter.PhotoImage(file= 'logo.png')
canvas.create_image(100, 100, image= lock_img)
canvas.grid(row=0, column= 1)

#website input
website_label = tkinter.Label(text= "Website:")
website_label.grid(row=1, column=0)

website_entry = tkinter.Entry(width= 55)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus() #Puts the cursor in here at start
# website_entry.insert(0, "sample")

#email/username input
email_username_label = tkinter.Label(text= "Email/Username:")
email_username_label.grid(row=2, column= 0)

email_username_entry = tkinter.Entry(width = 55)
email_username_entry.grid(row=2, column= 1, columnspan=2)
email_username_entry.insert(0, "sample@email.com")

#password input
password_label = tkinter.Label(text= "Password:")
password_label.grid(row=3, column= 0)

password_entry = tkinter.Entry(width= 35)
password_entry.grid(row=3, column=1)

#generate password button
generate_pw_button = tkinter.Button(text= 'Generate Password', command= GeneratePassword)
generate_pw_button.grid(row=3, column=2)

#add button
add_button = tkinter.Button(text= 'Add', width= 46, command= SavePassword)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()