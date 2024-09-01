#---------------------------- SIMPLE CALCULATOR APPLICATION ---------------------------------
# GUI based simple calculator which perform basic arithmetic operations with various features


import tkinter as tk
from tkinter import font

#Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("385x600")
root.configure(bg='gray2')

#fonts
button_font = font.Font(family='Cambria', size=22)
display_font = font.Font(family='Cambria', size=30)
label_font = font.Font(family='Cambria', size=27)

#Title
title_label = tk.Label(root, text="My Calculator", font=label_font, fg='violet', bg='gray2')
title_label.grid(row=0, column=0, columnspan=4, pady=15)

#Entry display
entry = tk.Entry(root, width=17, font=display_font, borderwidth=5, fg='HotPink2', bg='gray12', justify='right')
entry.grid(row=1, column=0, columnspan=4, pady=10, ipady=20)
entry.insert(0, "0")

#Functions
def button_click(number):          
    current = entry.get()
    if current == "0":
        current = ""
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_clear():
    entry.delete(0, tk.END)
    entry.insert(0, "0")

def button_backspace():
    current = entry.get()
    if len(current) > 1:
        entry.delete(len(current)-1, tk.END)
    else:
        entry.delete(0, tk.END)
        entry.insert(0, "0")

#Number Style
button_style = {
    'font': button_font,
    'bg': 'gray12',
    'fg': 'Violet',
    'borderwidth': 3,
    'relief': 'sunken',
    'highlightthickness': 0
}

operator_style = {
    'font': button_font,
    'bg': 'HotPink2',
    'fg': 'gray2',
    'borderwidth': 3,
    'relief': 'sunken',
    'highlightthickness': 0
}

#Create buttons
buttons = [
    (' C ', 2, 0, button_clear), ('', 2, 1, button_backspace), ('( )', 2, 2, lambda: button_click('( )')), ('+', 2, 3, lambda: button_click('+')),
    ('7', 3, 0, lambda: button_click(7)), ('8', 3, 1, lambda: button_click(8)), ('9', 3, 2, lambda: button_click(9)), ('-', 3, 3, lambda: button_click('-')),
    ('4', 4, 0, lambda: button_click(4)), ('5', 4, 1, lambda: button_click(5)), ('6', 4, 2, lambda: button_click(6)), ('*', 4, 3, lambda: button_click('*')),
    ('1', 5, 0, lambda: button_click(1)), ('2', 5, 1, lambda: button_click(2)), ('3', 5, 2, lambda: button_click(3)), ('/', 5, 3, lambda: button_click('/')),
    ('0', 6, 0, lambda: button_click(0)), ('.', 6, 1, lambda: button_click('.')), ('%', 6, 2, lambda: button_click('%')), ('=', 6, 3, button_equal)
    
]

# Place buttons on the grid
for (text, row, col, command) in buttons:
    style = button_style if text not in '+-*/=' else operator_style
    button = tk.Button(root, text=text, command=command, **style)
    button.grid(row=row, column=col, sticky="news", padx=4, pady=5, ipadx=7, ipady=5)

# Run the application
root.mainloop()
