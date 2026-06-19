import tkinter as tk

def greet_user():
    username =name_entry.get()
    
    welcome_label.config(text=f"Namaste, {username}!")


root = tk.Tk()
root.title("Learn Hindi Made Easy!")
root.geometry("500x450") # Set the window size to 500x450 pixels

name_entry = tk.Entry(root)
name_entry.pack(pady=10)
submit_btn = tk.Button(root, text="Submit", command=greet_user)
submit_btn.pack(pady=5)

welcome_label = tk.Label(root, text="")
welcome_label.pack(pady=10)
root.mainloop()