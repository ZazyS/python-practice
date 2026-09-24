import tkinter as tk
import random

conditions = ["burned", "frostbitten", "decaying", "waterlogged", "petrified"]
places = ["jawline", "left eye", "throat", "knuckles", "collarbone"]
extras = ["with visible bone", "still bleeding", "healing badly", "infested", "stitched shut"]

window = tk.Tk()
window.title("SFX Concept Generator")
window.geometry("400x200")

label = tk.Label(window, text="Press the button for a concept", wraplength=350)
label.pack(pady=20)

def generate():
    condition = random.choice(conditions)
    place = random.choice(places)
    extra = random.choice(extras)
    label.config(text=f"{condition} {place}, {extra}")
    
button = tk.Button(window, text="Generate", command=generate)
button.pack()

window.mainloop()