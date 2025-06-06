import tkinter as tk
from tkinter import messagebox
import os
import utilities  

class LoginGUI:
    def __init__(self, master):

        #Window setup
        self.master = master
        self.master.title("Login System")
        self.master.geometry("300x250")
        self.mode = "login"

        #Widgets setup
        self.username_label = tk.Label(master, text="Username:")
        self.username_entry = tk.Entry(master)

        self.password_label = tk.Label(master, text="Password:")
        self.password_entry = tk.Entry(master, show="*")

        self.submit_btn = tk.Button(master, text="Login", command=self.process)
        self.toggle_btn = tk.Button(master, text="Create Account Instead", command=self.toggle_mode)

        #Layout setup
        self.username_label.pack(pady=5)
        self.username_entry.pack(pady=5)
        self.password_label.pack(pady=5)
        self.password_entry.pack(pady=5)
        self.submit_btn.pack(pady=10)
        self.toggle_btn.pack()

    def toggle_mode(self):
        if self.mode == "login":
            self.mode = "create"
            self.submit_btn.config(text="Create Account")
            self.toggle_btn.config(text="Back to Login")
        else:
            self.mode = "login"
            self.submit_btn.config(text="Login")
            self.toggle_btn.config(text="Create Account Instead")

    def process(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showwarning("Missing Info", "Username and password cannot be empty.")
            return

        file = username + ".txt" #user's passwords will be stored as text files, named by the user's name

        #exception handling used for certain cases
        if self.mode == "create":
            if os.path.exists(file):
                messagebox.showwarning("Oops", "Account already exists.")
                return

            try:
                hashed = utilities.hashing(password).hexdigest() #used SHA256 hashing to store password (more secure than encryption as it generates new bundle of characters for each hashing, making it impossible to restore original data)
                utilities.create_file(file, hashed)
                messagebox.showinfo("Success", "Account created successfully!")
                self.toggle_mode()
                self.clear_entries()
            except FileExistsError:
                messagebox.showerror("Error", "Couldn't create file. Try again.")

        elif self.mode == "login":
            if not os.path.exists(file):
                messagebox.showerror("Login Failed", "Username not found.")
                return

            try:
                stored_hash = utilities.read_file(file)
                input_hash = utilities.hashing(password).hexdigest()

                if stored_hash == input_hash:
                    messagebox.showinfo("Login Success", f"Welcome back, {username}!")
                    self.clear_entries()
                else:
                    messagebox.showerror("Login Failed", "Incorrect password.")
            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong:\n{e}")

    #restart after each successful entry(login or creation)
    def clear_entries(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginGUI(root)
    root.mainloop()
