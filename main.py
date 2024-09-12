import tkinter as tk
import random
import time

# Function to simulate the dice roll with animation
def roll_dice():
    result_label.config(text="🎲", font=("Helvetica", 80, "bold"), fg="#888")
    result_label.update()  # Update UI immediately before starting animation
    
    # Dice roll animation (simulating the dice roll by showing random numbers)
    for _ in range(15):  # Animate 15 times for the roll
        result = random.randint(1, 6)
        result_label.config(text=f"{result}", font=("Helvetica", 80, "bold"), fg="#555")
        result_label.update()
        time.sleep(0.1)  # Short delay for animation

    # Display final result with cheer-up effect
    final_result = random.randint(1, 6)
    result_label.config(text=f"{final_result}", font=("Helvetica", 100, "bold"), fg="green")
    
    # Call cheer up animation (like a bounce effect)
    window.after(100, cheer_up_animation, final_result, 0)

    # Add result to history
    roll_history.append(final_result)
    update_history()

# Function for the cheer-up animation
def cheer_up_animation(final_result, count):
    colors = ["green", "orange", "blue", "purple", "red"]
    sizes = [100, 110, 105, 120, 100]
    if count < 5:  # Animate 5 times
        result_label.config(font=("Helvetica", sizes[count], "bold"), fg=colors[count])
        result_label.update()
        window.after(150, cheer_up_animation, final_result, count + 1)

# Function to reset the game
def reset_game():
    result_label.config(text="🎲", font=("Helvetica", 80, "bold"), fg="#888")
    history_label.config(text="")
    roll_history.clear()

# Update the roll history
def update_history():
    history_label.config(text=" | ".join(map(str, roll_history[-5:])), font=("Helvetica", 12), fg="#555")

# Create the tkinter window
window = tk.Tk()
window.title("Animated Dice Simulator")
window.geometry("500x400")
window.resizable(False, False)
window.config(bg="#f0f0f0")

# Dice face initial appearance
result_label = tk.Label(window, text="🎲", font=("Helvetica", 80, "bold"), bg="#f0f0f0", fg="#888")
result_label.pack(pady=30)

# History of rolls
roll_history = []
history_label = tk.Label(window, text="", font=("Helvetica", 12), bg="#f0f0f0", fg="#555")
history_label.pack()

# Roll button
roll_button = tk.Button(window, text="Roll Dice", command=roll_dice, font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white", width=15, height=2, borderwidth=2, relief="groove")
roll_button.pack(pady=10)

# Reset button
reset_button = tk.Button(window, text="Reset", command=reset_game, font=("Helvetica", 12), bg="#FF6347", fg="white", width=10, height=1, borderwidth=2, relief="groove")
reset_button.pack(pady=10)

# Decorative bottom frame
bottom_frame = tk.Frame(window, bg="#3E4149", height=30)
bottom_frame.pack(side="bottom", fill="x")

# Decorative title at the bottom
tk.Label(bottom_frame, text="Dice Simulator", font=("Helvetica", 12, "bold"), fg="white", bg="#3E4149").pack(pady=5)

# Run the tkinter event loop
window.mainloop()
