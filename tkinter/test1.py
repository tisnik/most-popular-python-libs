from ttkthemes import ThemedTk
from tkinter import ttk

# Create a themed window with Yaru theme
root = ThemedTk(theme="arc")
root.title("Native Linux Tkinter App")

# Add widgets to test styling
ttk.Label(root, text="Hello, Native Linux!").pack(pady=10)
ttk.Button(root, text="Click Me").pack(pady=5)
ttk.Entry(root).pack(pady=5)
ttk.Combobox(root, values=["Option 1", "Option 2"]).pack(pady=5)

root.mainloop()
