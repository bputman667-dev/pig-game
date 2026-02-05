import tkinter as tk

def say_hi():
    label.config(text="you clicked the button")

def unclick():
    label.config(text="hello tkinter")

root = tk.Tk()
root.title("my first tkinter project")
root.geometry("400x300")

label = tk.Label(root, text = "hello tkinter")
label.pack()

button = tk.Button(root, text = "click me", command = say_hi)
button.pack()

button_unclick = tk.Button(root, text = "click me to unclick above button", command = unclick)
button_unclick.pack()

root.mainloop()