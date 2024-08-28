import tkinter as tk
import os
from tkinter import filedialog, ttk


class Notepad:
    def __init__(self):
        # Create the main window with a title and custom icon
        self.window = tk.Tk()
        self.window.title("Notepad")
        self.window.iconbitmap('Notepad-Icon.ico')

        # Create a Notebook instance to hold all tabs
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(expand=True, fill='both')

        # Display buttons and add the first tab
        self.display_buttons()
        self.add_new_tab()

    def add_new_tab(self, name='Untitled'):
        # Create a new frame for the tab
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=name)

        # Create a text area in the new tab
        text_area = tk.Text(frame)
        text_area.pack(expand=True, fill='both')

        # Store the text area in the tab
        frame.text_area = text_area

    def close_tab(self):
        current_tab = self.notebook.select()
        if current_tab:
            self.notebook.forget(current_tab)

        if not self.notebook.tabs():
            self.window.quit()

    # Clear the Notepad and then open a preexisting file
    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        file_name = os.path.basename(file_path)
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.add_new_tab(name=file_name)
                self.notebook.select(self.notebook.index("end") - 1)
                current_tab = self.notebook.nametowidget(self.notebook.select())
                current_tab.text_area.insert(tk.END, content)

    # Create a file in the specified directory and insert all content to save a copy to your PC
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile="Untitled",
                                                 filetypes=[("Text files", "*.txt")])
        current_tab = self.notebook.nametowidget(self.notebook.select())
        if file_path:
            with open(file_path, 'w') as file:
                content = current_tab.text_area.get(1.0, tk.END)
                file.write(content)

    # Display the buttons to the screen providing functionality
    def display_buttons(self):
        # Create frames and buttons
        button_frame = tk.Frame(self.window)
        button_frame.pack(fill='x')

        new_button = tk.Button(button_frame, text='New', command=self.add_new_tab, background='white', width=5)
        new_button.pack(side='left')

        open_button = tk.Button(button_frame, text='Open', command=self.open_file, background='white', width=5)
        open_button.pack(side='left')

        save_button = tk.Button(button_frame, text='Save', command=self.save_file, background='white', width=5)
        save_button.pack(side='left')

        close_button = tk.Button(button_frame, text='Close', command=self.close_tab, background='white', width=5)
        close_button.pack(side='left')
