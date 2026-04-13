import tkinter as tk
from tkinter import messagebox


# Simple rules-based loan prediction
def predict_loan_amount():
    try:
        # Get the Inter Merit Score from the user
        inter_merit_score = int(merit_entry.get())

        # Check for valid merit score (0-100)
        if inter_merit_score < 0 or inter_merit_score > 100:
            messagebox.showerror("Invalid Merit Score", "Please enter a merit score between 0 and 100.")
            return

        # Rules for loan amount based on merit score
        if inter_merit_score >= 90:
            loan_amount = 1000000  # 1,000,000 INR for top scorers
            education_level = "Medical or Postgraduate"
        elif inter_merit_score >= 80:
            loan_amount = 800000  # 800,000 INR for good scorers
            education_level = "Undergraduate or Postgraduate"
        elif inter_merit_score >= 70:
            loan_amount = 600000  # 600,000 INR for average scorers
            education_level = "Undergraduate"
        elif inter_merit_score >= 60:
            loan_amount = 400000  # 400,000 INR for decent scorers
            education_level = "Intermediate or Arts"
        else:
            loan_amount = 200000  # 200,000 INR for lower scorers
            education_level = "Arts or Intermediate"

        # Display the results
        result_text = f"Based on your Inter Merit Score of {inter_merit_score}:\n"
        result_text += f"Suggested Education Level: {education_level}\n"
        result_text += f"Suggested Loan Amount: ₹{loan_amount}"

        result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for Merit Score.")


# Setting up the Tkinter window
root = tk.Tk()
root.title("Education Loan Prediction System")

# Title label
title_label = tk.Label(root, text="Education Loan Prediction System", font=("Arial", 16))
title_label.pack(pady=10)

# Merit score entry
merit_label = tk.Label(root, text="Enter Your Inter Merit Score (0-100):")
merit_label.pack(pady=5)
merit_entry = tk.Entry(root)
merit_entry.pack(pady=5)

# Predict button
predict_button = tk.Button(root, text="Predict Loan Amount", command=predict_loan_amount)
predict_button.pack(pady=20)

# Label to display results
result_label = tk.Label(root, text="Your loan amount and education level will appear here.", font=("Arial", 12),
                        justify="left")
result_label.pack(pady=10)

# Run the application
root.mainloop()
