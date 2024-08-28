import tkinter as tk
from tkinter import filedialog


class Notepad:
    def __init__(self):
        # Create screen and title
        self.window = tk.Tk()
        self.window.title("Untitled | Notepad")

        # Custom icon
        self.window.iconbitmap('Notepad-Icon.ico')

        # Define text area and display buttons above
        self.text_area = tk.Text(self.window)
        self.display_buttons()
        self.text_area.pack(expand=True, fill='both')

    # Clear the Notepad
    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    # Clear the Notepad and then open a preexisting file
    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.new_file()
                self.text_area.insert(tk.END, content)

    # Create a file in the specified directory and insert all content to save a copy to your PC
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile="Untitled", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    # Display the buttons to the screen providing functionality
    def display_buttons(self):
        # Create frames and buttons
        button_frame = tk.Frame(self.window)
        button_frame.pack(fill='x')

        new_button = tk.Button(button_frame, text='New', command=self.new_file, background='white', width=5)
        new_button.pack(side='left')

        open_button = tk.Button(button_frame, text='Open', command=self.open_file, background='white', width=5)
        open_button.pack(side='left')

        save_button = tk.Button(button_frame, text='Save', command=self.save_file, background='white', width=5)
        save_button.pack(side='left')


