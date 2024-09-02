import tkinter as tk
from tkinter import messagebox, font

# Store previous BMI calculations
previous_bmi = []

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())
        
        if weight <= 0 or height_cm <= 0:
            messagebox.showerror("Input Error", "Weight and height must be positive values.")
            return

        height_m = height_cm / 100  # Convert height to meters
        bmi = weight / (height_m ** 2)
        category = categorize_bmi(bmi)
        
        # Store the current BMI in the previous_bmi list
        previous_bmi.append(f"BMI: {bmi:.2f} ({category})")
        update_previous_bmi_list()

        label_result.config(text=f"Your BMI is {bmi:.2f}, which is considered {category}.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def update_previous_bmi_list():
    previous_bmi_text = "\n".join(previous_bmi[-5:])  # Show last 5 entries
    label_previous.config(text=previous_bmi_text)

# Set up the main window
root = tk.Tk()
root.title("BMI Calculator")

# Set font
app_font = font.Font(family="Helvetica", size=12, weight="bold")

# Create and place the weight label and entry field
label_weight = tk.Label(root, text="Enter your weight in kilograms:", font=app_font)
label_weight.pack(pady=5)

entry_weight = tk.Entry(root, font=app_font)
entry_weight.pack(pady=5)

# Create and place the height label and entry field
label_height = tk.Label(root, text="Enter your height in centimeters:", font=app_font)
label_height.pack(pady=5)

entry_height = tk.Entry(root, font=app_font)
entry_height.pack(pady=5)

# Create and place the calculate button
button_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="#4CAF50", fg="white", font=app_font)
button_calculate.pack(pady=10)

# Create and place the result label
label_result = tk.Label(root, text="", font=app_font)
label_result.pack(pady=10)

# Create and place the previous BMI label
label_previous_header = tk.Label(root, text="Previous BMI Calculations:", font=app_font)
label_previous_header.pack(pady=10)

label_previous = tk.Label(root, text="", font=app_font, justify="left")
label_previous.pack(pady=5)

# Run the application
root.mainloop()
