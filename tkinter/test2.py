import tkinter as tk  
from tkinter import ttk  
 
root = tk.Tk()  
root.title("System Theme Demo")  
style = ttk.Style()  

print("System themes:", style.theme_names())
 
 # Make buttons match GTK's rounded style
style.configure("TButton",
                padding=6,
                relief="flat",
                background="#4a90d9",  # GTK blue accent
                foreground="white")

# Hover effect for buttons
style.map("TButton",
          background=[("active", "#357abd")])  # Darker blue on hover

# Use the system's GTK theme (if available)  
#style.theme_use("classic")  # Replace with your theme (e.g., 'adwaita', 'breeze')  
 
# Configure fonts to match system (e.g., Ubuntu uses 'Ubuntu 10')  
style.configure(".", font=("Ubuntu", 10))  # Applies to all widgets  
 
# Add widgets  
ttk.Label(root, text="System Theme Applied!").pack(pady=10)  
ttk.Button(root, text="System-Stlyed Button").pack(pady=5)  
 
root.mainloop()  
