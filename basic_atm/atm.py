import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM")
        self.balance = 1000
        self.pin = "1234"
        self.history = []

        self.main_screen()

    def main_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to the ATM", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self.root, text="Login", command=self.login_screen).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=10)

    def login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter PIN", font=("Helvetica", 14)).pack(pady=20)
        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.pack(pady=10)
        tk.Button(self.root, text="Submit", command=self.check_pin).pack(pady=10)

    def check_pin(self):
        if self.pin_entry.get() == self.pin:
            self.menu_screen()
        else:
            messagebox.showerror("Error", "Incorrect PIN")
            self.pin_entry.delete(0, tk.END)

    def menu_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="ATM Menu", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self.root, text="View Balance", command=self.view_balance).pack(pady=10)
        tk.Button(self.root, text="Transaction History", command=self.view_history).pack(pady=10)
        tk.Button(self.root, text="Change PIN", command=self.change_pin_screen).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.main_screen).pack(pady=10)

    def view_balance(self):
        messagebox.showinfo("Balance", f"Your balance is: ${self.balance}")

    def view_history(self):
        history_str = "\n".join(self.history) if self.history else "No transactions yet."
        messagebox.showinfo("Transaction History", history_str)

    def change_pin_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter New PIN", font=("Helvetica", 14)).pack(pady=20)
        self.new_pin_entry = tk.Entry(self.root, show="*")
        self.new_pin_entry.pack(pady=10)
        tk.Button(self.root, text="Submit", command=self.change_pin).pack(pady=10)

    def change_pin(self):
        if new_pin := self.new_pin_entry.get():
            self.pin = new_pin
            messagebox.showinfo("Success", "PIN changed successfully")
            self.menu_screen()
        else:
            messagebox.showerror("Error", "PIN cannot be empty")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
