import tkinter as tk
from tkinter import filedialog

def detect_particles():
    # Placeholder function for particle detection
    print("Detecting particles...")

def upload_image():
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        print("Selected file:", file_path)
        # Perform further processing with the selected image file

# Create the main window
root = tk.Tk()
root.title("NanoLense")

# Add a title label
title_label = tk.Label(root, text="NanoLense", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Add a button to upload images
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

# Add a button to trigger particle detection
detect_button = tk.Button(root, text="Detect Particles", command=detect_particles)
detect_button.pack(pady=10)

# Center the window on the screen
window_width = 400
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

# Run the application
root.mainloop()
