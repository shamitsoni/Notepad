import tkinter as tk
from tkinter import filedialog


# Clear the Notepad
def new_file():
    text_area.delete(1.0, tk.END)


# Clear the Notepad and open a preexisting file
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            new_file()
            text_area.insert(tk.END, content)


# Create a file in the specified directory and insert all content to save a copy to your PC
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)


root = tk.Tk()
root.title("Untitled")

button_frame = tk.Frame(root)
button_frame.pack(fill='x')

new_button = tk.Button(button_frame, text="New", command=new_file)
new_button.pack(side='left')

open_button = tk.Button(button_frame, text="Open", command=open_file)
open_button.pack(side='left')

save_button = tk.Button(button_frame, text="Save", command=save_file)
save_button.pack(side='left')

text_area = tk.Text(root)
text_area.pack(expand=True, fill='both')

root.mainloop()
