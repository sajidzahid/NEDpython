import tkinter as tk

# Function to update expression in the entry field
def btn_click(item):
    current = entry_var.get()
    entry_var.set(current + str(item))

# Function to clear the entry field
def btn_clear():
    entry_var.set("")

# Function to delete the last character
def btn_backspace():
    current = entry_var.get()
    entry_var.set(current[:-1])

# Function to evaluate the expression
def btn_equal():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x550")
root.resizable(False, False)

# Entry widget to display expressions
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 20), bd=10, relief=tk.GROOVE, justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create buttons and add them to the grid
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=10, height=2, command=btn_equal, bg="lightblue")
    else:
        btn = tk.Button(root, text=text, width=10, height=2, command=lambda t=text: btn_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Additional buttons (Clear & Backspace)
btn_clear = tk.Button(root, text="C", width=10, height=2, command=btn_clear, bg="lightcoral")
btn_clear.grid(row=5, column=0, padx=5, pady=5)

btn_backspace = tk.Button(root, text="←", width=10, height=2, command=btn_backspace, bg="lightgrey")
btn_backspace.grid(row=5, column=1, padx=5, pady=5)

# Run the application
root.mainloop()


