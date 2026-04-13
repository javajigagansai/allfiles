import tkinter as tk
import random

# Function to move the "No" button to a random location inside the frame after it's clicked
def move_no_button(event=None):
    x = random.randint(10, 250)  # Adjust the range to keep it within the frame
    y = random.randint(10, 100)
    no_button.place(x=x, y=y)

# Function to show a message when "Yes" is clicked
def show_yes_message():
    message_label.config(text="I love you too!")

# Create the main window
root = tk.Tk()
root.title("Do you love me?")
root.geometry("400x300")

# Create a frame with a border to contain the question and buttons
border_frame = tk.Frame(root, highlightbackground="black", highlightthickness=2, padx=20, pady=20)
border_frame.pack(pady=30)

# Create a label with the question inside the frame
question_label = tk.Label(border_frame, text="Do you love me?", font=("Arial", 16))
question_label.pack(pady=20)

# Create the "Yes" button inside the frame
yes_button = tk.Button(border_frame, text="Yes", font=("Arial", 12), command=show_yes_message)
yes_button.pack(side=tk.LEFT, padx=50)

# Create the "No" button, which moves when clicked
no_button = tk.Button(border_frame, text="No", font=("Arial", 12))
no_button.place(x=150, y=80)  # Initial position inside the frame
no_button.bind("<Button-1>", move_no_button)

# Create a label for the result message outside the frame
message_label = tk.Label(root, text="", font=("Arial", 14))
message_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
