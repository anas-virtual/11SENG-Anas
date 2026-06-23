import tkinter as tk
import ctypes # For DPI awarness on Windows
try: 
    ctypes.windll.shcore.SetProcessDpiAwarness(1) # This basically just makes the app look better and removes the blurriness and low resolution
except:
    pass
root = tk.Tk()
root.title("Learn Hindi Made Easy!")
root.geometry("400x500") # Set the window size to 400x500 pixels
root.resizable(False, False) # Disable resizing of the window

bg_image = tk.PhotoImage(file="Background SENG (1).png")
bg_label = tk.Label(root, image=bg_image, bd=0)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#Buttons
start_button = tk.Button(root, text="Welcome!", font=("Arial", 11, "bold"), fg="#FF9F3E", bg="white", padx=10, pady=2, cursor="hand2")
start_button.place(x=200, y=265, anchor="center")


root.mainloop()