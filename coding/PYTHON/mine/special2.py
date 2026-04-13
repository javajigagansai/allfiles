import tkinter as tk
import random
def move_no_button(event=None):
    x = random.randint(0, 1300)
    y = random.randint(0, 1300)
    no_button.place(x=x, y=y)
def show_yes_message():
    message_label.config(text="I love you too!")
root = tk.Tk()
root.title("Do you love me ?")
root.geometry("1800x1800")
question_label = tk.Label(root, text="Do you love me?", font=("Arial", 16))
question_label.pack(pady=99)
yes_button = tk.Button(root, text="Yes", font=("Arial", 14), command=show_yes_message)
yes_button.pack(side=tk.LEFT, padx=500)
no_button = tk.Button(root, text="No", font=("Arial", 14))
no_button.place(x=100, y=150)
no_button.bind("<Button-1>", move_no_button)
message_label = tk.Label(root, text="", font=("Arial", 14))
message_label.pack(pady=200)
root.mainloop()