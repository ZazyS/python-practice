import tkinter as tk

window = tk.Tk()
window.title("My first app")
window.geometry("300x200")

label = tk.Label(window, text ="Type your name")
label.pack()
entry = tk.Entry(window)
entry.pack()

def button_clicked():
    name = entry.get()
    label.config(text =f"Hello, {name}!")
    
button = tk.Button(window, text="Click me", command=button_clicked)
button.pack()

window.mainloop()
   