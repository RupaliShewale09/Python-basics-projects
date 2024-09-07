#-----------------------------------------  PASSWORD GENERATOR --------------------------------------
# to create GUI-based application using Python, allowing users to specify the length and complexity of the password

import tkinter as tk
import random
import string

# Function to generate the password
def generate_password():
    length = password_length.get()
    characters = ""
    
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if numbers_var.get():
        characters += string.digits
    if special_var.get():
        characters += string.punctuation

    if characters:
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        check_password_strength(password)
    else:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Select options")

# Function to copy password
def copy_password():
    copied_password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(copied_password)
    copied_label.config(text=f"Copied: {copied_password}")

# Function to check password strength
def check_password_strength(password):
    if len(password) < 7:
        strength_label.config(text="Weak", fg="red", bg="white")
    elif len(password) <= 14:
        strength_label.config(text="Medium", fg="orange", bg="white")
    else:
        strength_label.config(text="Strong", fg="green", bg="white")
        
def update_length_label(value):
    # Update the label with the current slider value
    length_label.config(text=f"Password Length: {value}")
    
def reattempt_password():
    # Uncheck all checkboxes
    lowercase_var.set(False)
    uppercase_var.set(False)
    numbers_var.set(False)
    special_var.set(False)
    generate_password()

# Main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("550x550")
root.configure(bg='white', highlightthickness=30, highlightcolor="turquoise")


# Title Label
title_label = tk.Label(root, text="PASSWORD GENERATOR", font=("Cambria", 20,"bold"), bg='white')
title_label.pack(pady=10)
title_label.place_configure(x='70',y='40')

# Password Entry Field
password_entry = tk.Entry(root, font=("Cambria", 16),fg='black',width=25, highlightthickness=4)
password_entry.pack(pady=10)
password_entry.place_configure(x='40',y='100')

# Strength Label
strength_label = tk.Label(root, text="", font=("Cambria", 14), bg="white")
strength_label.pack(pady=5)
strength_label.place_configure(x='40',y='140')

# Copy Button
copy_button = tk.Button(root, text=" Copy ",font=("Cambria",13), command=copy_password, bg='turquoise',width=7,relief='ridge')
#copy_button.pack(ipadx=50, ipady=10)
copy_button.place_configure(x='400',y='100')

# Label to display copied password
copied_label = tk.Label(root, text="", font=("Cambria", 12), bg="white", fg="black")
copied_label.pack(pady=10)

# Generate Button
generate_button = tk.Button(root, text="Generate", command=generate_password, font=('Cambria',15 , 'bold'), bg='turquoise', width=20, relief='ridge')
generate_button.pack(pady=10)
generate_button.place_configure(x='130',y='410')


reattempt_button = tk.Button(root, text=' ⟳ ', command=reattempt_password, font=('Cambria',12, 'bold'), bg='white', relief='ridge')
reattempt_button.place_configure(x='360',y='100')  

# Password Length Slider

length_label = tk.Label(root, text="Password Length: 8",font=("Cambria",13), bg='white',fg='black')
length_label.pack(pady=10)
length_label.place_configure(x='40',y='180')


password_length = tk.IntVar(value=8)
slider = tk.Scale(root, from_=5, to_=20, orient='horizontal', variable=password_length, length=400, width=20, sliderlength=30, bg='white', troughcolor='white',command=update_length_label)
slider.pack(pady=10)
slider.place_configure(x='40',y='210')

# Checkboxes for options
lowercase_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_var = tk.BooleanVar()

lowcase = tk.Checkbutton(root, text="Lowercase", variable=lowercase_var, bg='white', font=("Cambria",14) )
lowcase.place_configure(x='40',y='300')
uppcase = tk.Checkbutton(root, text="Uppercase", variable=uppercase_var, bg='white', font=("Cambria",14))
uppcase.place_configure(x='250',y='300')
numbers = tk.Checkbutton(root, text="Numbers", variable=numbers_var, bg='white', font=("Cambria",14))
numbers.place_configure(x='40',y='350')
characters = tk.Checkbutton(root, text="Special Characters", variable=special_var, bg='white', font=("Cambria",14))
characters.place_configure(x='250',y='350')


root.mainloop()