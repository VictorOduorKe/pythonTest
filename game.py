import tkinter as tk
import random
import os

# Generate a random three-digit number
nump = random.randint(100, 999)

# Function to check the user's guess
def check_guess():
    user_input = entry.get()

    # Validate input
    if not user_input.isdigit() or len(user_input) != 3:
        result_label.config(text="Please enter a valid three-digit number!", fg="red")
        return

    guess = int(user_input)
    num_str = str(nump)
    guess_str = str(guess)
    correct_digits = sum(1 for i in range(3) if num_str[i] == guess_str[i])

    if correct_digits == 3:
        result_label.config(text="🎉 Congratulations! You guessed it right!", fg="green")
    else:
        result_label.config(text=f"{correct_digits} digits were correct. Try again!", fg="orange")

        # Shutdown system after wrong guess (WARNING: Will shut down the PC)
        os.system("shutdown /s /t 10")

# Function to cancel shutdown if needed
def cancel_shutdown():
    os.system("shutdown /a")
    result_label.config(text="Shutdown Canceled!", fg="blue")

# GUI setup
root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("400x300")

# UI Elements
tk.Label(root, text="Enter a three-digit number:", font=("Arial", 14)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 16), justify="center")
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Guess", command=check_guess, font=("Arial", 14), bg="lightblue")
check_button.pack(pady=10)

cancel_button = tk.Button(root, text="Cancel Shutdown", command=cancel_shutdown, font=("Arial", 14), bg="lightcoral")
cancel_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
