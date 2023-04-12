import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Grid GUI")

# Define the grid size
num_rows = 2
num_cols = 2

# Define the colors for the boxes
colors = ["blue", "green", "red", "yellow"]

# Create the grid of boxes with different colors
for row in range(num_rows):
    for col in range(num_cols):
        # Create a canvas widget as a box
        box = tk.Canvas(root, width=100, height=100, bg=colors[row * num_cols + col])
        # Place the box in the grid with no padding or spacing
        box.grid(row=row, column=col, padx=0, pady=0)

# Start the main event loop
root.mainloop()