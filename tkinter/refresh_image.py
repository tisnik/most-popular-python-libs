import tkinter as tk

def refresh_image():
    # Load and display the image
    with open("test.png", "rb") as fin:
        image_data = fin.read()
    image = tk.PhotoImage(data=image_data)
    label.config(image=image)
    label.image = image

    # Schedule the next refresh
    root.after(1000, refresh_image)  # Refresh the image every 1 second

# Create the tkinter window
root = tk.Tk()

# Create a label to display the image
label = tk.Label(root)
label.pack()

# Schedule the initial refresh of the image
refresh_image()

# Add other interactive widgets to the window
button = tk.Button(root, text="Click Me")
button.pack()

# Start the tkinter main loop
root.mainloop()

