import random
from tkinter import *
from tkinter import messagebox, ttk
import pyperclip
import string

class PasswordGenerator:
    def __init__(self):
        self.gui = Tk()
        self.gui.title('Password Generator')
        self.gui.geometry('400x500')
        self.gui.resizable(0,0)
        self.gui.configure(bg='#f0f0f0')

        # Variables
        self.string_pass = StringVar(value="12")
        self.include_lower = BooleanVar(value=True)
        self.include_upper = BooleanVar(value=True) 
        self.include_numbers = BooleanVar(value=True)
        self.include_special = BooleanVar(value=True)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.gui, padding="20")
        main_frame.pack(fill=BOTH, expand=True)
        
        # Title
        ttk.Label(main_frame, text="Password Generator", font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        # Length frame
        length_frame = ttk.LabelFrame(main_frame, text="Password Length", padding="10")
        length_frame = ttk.LabelFrame(main_frame, text="Password Length", padding="10")
        length_frame.pack(fill=X, pady=10)
        
        ttk.Entry(length_frame, textvariable=self.string_pass, width=10).pack(side=LEFT, padx=5)
        ttk.Scale(length_frame, from_=8, to=32, variable=self.string_pass, orient=HORIZONTAL, 
                command=lambda x: self.string_pass.set(int(float(x)))).pack(side=LEFT, fill=X, expand=True, padx=5)
        
        # Options frame
        options_frame = ttk.LabelFrame(main_frame, text="Options", padding="10")
        options_frame.pack(fill=X, pady=10)
        
        ttk.Checkbutton(options_frame, text="Lowercase (a-z)", variable=self.include_lower).pack(anchor=W)
        ttk.Checkbutton(options_frame, text="Uppercase (A-Z)", variable=self.include_upper).pack(anchor=W)
        ttk.Checkbutton(options_frame, text="Numbers (0-9)", variable=self.include_numbers).pack(anchor=W)
        ttk.Checkbutton(options_frame, text="Special Characters (@#$%&*)", variable=self.include_special).pack(anchor=W)
        
        # Generate button
        ttk.Button(main_frame, text="Generate Password", command=self.process, style='Accent.TButton').pack(pady=20)
        
        # Result frame
        self.result_var = StringVar()
        result_frame = ttk.LabelFrame(main_frame, text="Generated Password", padding="10")
        result_frame.pack(fill=X, pady=10)
        
        self.result_entry = ttk.Entry(result_frame, textvariable=self.result_var, state='readonly', width=40)
        self.result_entry.pack(side=LEFT, padx=5)
        
        ttk.Button(result_frame, text="Copy", command=self.copy_password).pack(side=LEFT, padx=5)

    def process(self):
        try:
            length = int(self.string_pass.get())
            if length < 8:
                messagebox.showwarning("Warning", "Password length should be at least 8 characters")
                return
                
            char_sets = []
            if self.include_lower.get():
                char_sets.append(string.ascii_lowercase)
            if self.include_upper.get():
                char_sets.append(string.ascii_uppercase)
            if self.include_numbers.get():
                char_sets.append(string.digits)
            if self.include_special.get():
                char_sets.append('@#$%&*')
                
            if not char_sets:
                messagebox.showwarning("Warning", "Please select at least one character set")
                return
                
            all_chars = ''.join(char_sets)
            password = ''.join(random.choice(all_chars) for _ in range(length))
            
            # ensure at least one character from each selected set
            if len(char_sets) > length:
                messagebox.showwarning("Warning", "Password length must be greater than number of required character types")
                return
                
            self.result_var.set(password)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for password length")

    def copy_password(self):
        password = self.result_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")

if __name__ == "__main__":
    app = PasswordGenerator()
    app.gui.mainloop()
