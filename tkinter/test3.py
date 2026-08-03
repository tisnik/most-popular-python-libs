import tkinter as tk  
from tkinter import ttk  
 
root = tk.Tk()  
root.title("Manually Styled Native App")  
style = ttk.Style()  
 
# Step 1: Set system font (e.g., Ubuntu 10pt)  
system_font = ("Ubuntu", 10)  
style.configure(".", font=system_font)  
 
# Step 2: Set system colors (example for Ubuntu/Yaru)  
bg_color = "#f5f5f5"  # Window background  
text_color = "#2e3440"  # Text color  
accent_color = "#7cafc2"  # Button accent  
 
style.configure(".", background=bg_color, foreground=text_color)  
 
# Step 3: Style specific widgets  
style.configure("TButton",  
                padding=8,  
                background=accent_color,  
                foreground="white",  
                relief="flat",  
                borderwidth=0)  
 
style.configure("TLabel", padding=4)  
style.configure("TEntry", padding=6, relief="solid", borderwidth=1)  
 
# Add widgets to test  
ttk.Label(root, text="Manually Styled!").pack(pady=10)  
ttk.Button(root, text="Custom Button").pack(pady=5)  
ttk.Entry(root).pack(pady=5)  
 
root.mainloop()  
