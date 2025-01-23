import tkinter as tk
from tkinter import messagebox

class ATM:
    def setup(self, root):
        self.balance = 69696969  # Initial balance
        self.history = []  # Transaction history
        self.pin = "1234"  # Set your PIN here

        self.root = root
        self.root.title("ATM")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=400, height=600, bg="white")  # Set background color to white
        self.canvas.pack(fill="both", expand=True)

        self.widgets = []  # List to keep track of widgets
        self.show_initial_welcome_screen()

    def show_initial_welcome_screen(self):
        self.clear_screen()

        # Initial welcome screen widgets
        self.initial_welcome_label = tk.Label(self.root, text="Welcome to Ashu's Bank", font=("Arial", 16), bg="white")
        self.initial_welcome_label.pack(pady=10, anchor="center")
        self.widgets.append(self.initial_welcome_label)

        self.continue_button = tk.Button(self.root, text="Continue", font=("Arial", 14), command=self.show_welcome_screen,
                                         activebackground="lightblue", activeforeground="black")
        self.continue_button.pack(pady=5, anchor="center")
        self.widgets.append(self.continue_button)

    def show_welcome_screen(self):
        self.clear_screen()

        # Welcome screen widgets
        self.create_label("Welcome to the ATM", 16)

        self.pin_label = tk.Label(self.root, text="Enter PIN", font=("Arial", 14), bg="white")
        self.pin_label.pack(pady=10, anchor="center")
        self.widgets.append(self.pin_label)

        self.pin_entry = tk.Entry(self.root, font=("Arial", 14), show="*")
        self.pin_entry.pack(pady=10, anchor="center")
        self.pin_entry.bind("<Return>", self.check_pin)
        self.widgets.append(self.pin_entry)

        self.pin_button = tk.Button(self.root, text="Submit", font=("Arial", 14), command=self.check_pin,
                                    activebackground="lightblue", activeforeground="black")
        self.pin_button.pack(pady=5, anchor="center")
        self.widgets.append(self.pin_button)

    def check_pin(self, event=None):
        entered_pin = self.pin_entry.get()
        if entered_pin == self.pin:
            self.show_main_screen()
        else:
            messagebox.showerror("Error", "Incorrect PIN")

    def show_main_screen(self):
        self.clear_screen()

        # Main screen widgets
        self.create_label("ATM Machine", 16)
        self.label = tk.Label(self.root, text="ATM Machine", font=("Arial", 16), bg=self.canvas["bg"])
        self.label.pack(pady=10, anchor="center")
        self.widgets.append(self.label)

        self.balance_label = tk.Label(self.root, text=f"Balance: ${self.balance}", font=("Arial", 14), bg="white")
        self.balance_label.pack(pady=10, anchor="center")
        self.widgets.append(self.balance_label)

        self.deposit_button = tk.Button(self.root, text="Deposit", font=("Arial", 14), command=self.show_deposit_screen,
                                        activebackground="lightblue", activeforeground="black")
        self.deposit_button.pack(pady=5, anchor="center")
        self.widgets.append(self.deposit_button)

        self.withdraw_button = tk.Button(self.root, text="Withdraw", font=("Arial", 14), command=self.show_withdraw_screen,
                                         activebackground="lightblue", activeforeground="black")
        self.withdraw_button.pack(pady=5, anchor="center")
        self.widgets.append(self.withdraw_button)

        self.transfer_button = tk.Button(self.root, text="Transfer", font=("Arial", 14), command=self.show_transfer_screen,
                                         activebackground="lightblue", activeforeground="black")
        self.transfer_button.pack(pady=5, anchor="center")
        self.widgets.append(self.transfer_button)

        self.history_button = tk.Button(self.root, text="Transaction History", font=("Arial", 14), command=self.show_history,
                                        activebackground="lightblue", activeforeground="black")
        self.history_button.pack(pady=5, anchor="center")
        self.widgets.append(self.history_button)

        self.inquiry_button = tk.Button(self.root, text="Bank Inquiry", font=("Arial", 14), command=self.show_inquiry,
                                        activebackground="lightblue", activeforeground="black")
        self.inquiry_button.pack(pady=5, anchor="center")
        self.widgets.append(self.inquiry_button)

        self.change_pin_button = tk.Button(self.root, text="Change PIN", font=("Arial", 14), command=self.show_change_pin_screen,
                                           activebackground="lightblue", activeforeground="black")
        self.change_pin_button.pack(pady=5, anchor="center")
        self.widgets.append(self.change_pin_button)

        self.logout_button = tk.Button(self.root, text="Logout", font=("Arial", 14), command=self.show_welcome_screen,
                                       activebackground="lightblue", activeforeground="black")
        self.logout_button.pack(pady=5, anchor="center")
        self.widgets.append(self.logout_button)

    def show_deposit_screen(self):
        self.clear_screen()

        # Deposit screen widgets
        self.label = tk.Label(self.root, text="Deposit Funds", font=("Arial", 16), bg=self.canvas["bg"])
        self.create_label("Deposit Funds", 16)

        self.amount_label = tk.Label(self.root, text="Enter amount", font=("Arial", 14), bg="white")
        self.amount_label.pack(pady=10, anchor="center")
        self.widgets.append(self.amount_label)

        self.amount_entry = tk.Entry(self.root, font=("Arial", 14))
        self.amount_entry.pack(pady=10, anchor="center")
        self.amount_entry.bind("<Return>", self.deposit)
        self.widgets.append(self.amount_entry)

        self.deposit_button = tk.Button(self.root, text="Deposit", font=("Arial", 14), command=self.deposit,
                                        activebackground="lightblue", activeforeground="black")
        self.deposit_button.pack(pady=5, anchor="center")
        self.widgets.append(self.deposit_button)

        self.back_button = tk.Button(self.root, text="Back", font=("Arial", 14), command=self.show_main_screen,
                                     activebackground="lightblue", activeforeground="black")
        self.back_button.pack(pady=5, anchor="center")
        self.widgets.append(self.back_button)

    def show_withdraw_screen(self):
        self.clear_screen()

        # Withdraw screen widgets
        self.label = tk.Label(self.root, text="Withdraw Funds", font=("Arial", 16), bg=self.canvas["bg"])
        self.label.pack(pady=10, anchor="center")
        self.create_label("Withdraw Funds", 16)
        self.amount_label = tk.Label(self.root, text="Enter amount", font=("Arial", 14), bg=self.canvas["bg"])
        self.amount_label.pack(pady=10, anchor="center")
        self.widgets.append(self.amount_label)

        self.amount_entry = tk.Entry(self.root, font=("Arial", 14))
        self.amount_entry.pack(pady=10, anchor="center")
        self.amount_entry.bind("<Return>", self.withdraw)
        self.widgets.append(self.amount_entry)

        self.withdraw_button = tk.Button(self.root, text="Withdraw", font=("Arial", 14), command=self.withdraw,
                                         activebackground="lightblue", activeforeground="black")
        self.withdraw_button.pack(pady=5, anchor="center")
        self.widgets.append(self.withdraw_button)

        self.back_button = tk.Button(self.root, text="Back", font=("Arial", 14), command=self.show_main_screen,
                                     activebackground="lightblue", activeforeground="black")
        self.back_button.pack(pady=5, anchor="center")
        self.widgets.append(self.back_button)

    def show_transfer_screen(self):
        self.clear_screen()

        # Transfer screen widgets
        self.label = tk.Label(self.root, text="Transfer Funds", font=("Arial", 16), bg=self.canvas["bg"])
        self.label.pack(pady=10, anchor="center")
        self.widgets.append(self.label)

        self.amount_label = tk.Label(self.root, text="Enter amount", font=("Arial", 14), bg=self.canvas["bg"])
        self.amount_label.pack(pady=10, anchor="center")
        self.widgets.append(self.amount_label)

        self.amount_entry = tk.Entry(self.root, font=("Arial", 14))
        self.amount_entry.pack(pady=10, anchor="center")
        self.amount_entry.bind("<Return>", self.transfer)
        self.widgets.append(self.amount_entry)

        self.account_label = tk.Label(self.root, text="Enter account number", font=("Arial", 14), bg="white")
        self.account_label.pack(pady=10, anchor="center")
        self.widgets.append(self.account_label)

        self.account_entry = tk.Entry(self.root, font=("Arial", 14))
        self.account_entry.pack(pady=10, anchor="center")
        self.account_entry.bind("<Return>", self.transfer)
        self.widgets.append(self.account_entry)

        self.transfer_button = tk.Button(self.root, text="Transfer", font=("Arial", 14), command=self.transfer,
                                         activebackground="lightblue", activeforeground="black")
        self.transfer_button.pack(pady=5, anchor="center")
        self.widgets.append(self.transfer_button)

        self.back_button = tk.Button(self.root, text="Back", font=("Arial", 14), command=self.show_main_screen,
                                     activebackground="lightblue", activeforeground="black")
        self.back_button.pack(pady=5, anchor="center")
        self.widgets.append(self.back_button)

    def show_inquiry(self):
        messagebox.showinfo("Bank Inquiry", f"Your current balance is ${self.balance}")

    def show_change_pin_screen(self):
        self.clear_screen()

        # Change PIN screen widgets
        self.label = tk.Label(self.root, text="Change PIN", font=("Arial", 16), bg=self.canvas["bg"])
        self.label.pack(pady=10, anchor="center")
        self.widgets.append(self.label)

        self.old_pin_label = tk.Label(self.root, text="Enter old PIN", font=("Arial", 14), bg="white")
        self.old_pin_label.pack(pady=10, anchor="center")
        self.widgets.append(self.old_pin_label)

        self.old_pin_entry = tk.Entry(self.root, font=("Arial", 14), show="*")
        self.old_pin_entry.pack(pady=10, anchor="center")
        self.widgets.append(self.old_pin_entry)

        self.new_pin_label = tk.Label(self.root, text="Enter new PIN", font=("Arial", 14), bg="white")
        self.new_pin_label.pack(pady=10, anchor="center")
        self.widgets.append(self.new_pin_label)

        self.new_pin_entry = tk.Entry(self.root, font=("Arial", 14), show="*")
        self.new_pin_entry.pack(pady=10, anchor="center")
        self.widgets.append(self.new_pin_entry)

        self.change_pin_button = tk.Button(self.root, text="Change PIN", font=("Arial", 14), command=self.change_pin,
                                           activebackground="lightblue", activeforeground="black")
        self.change_pin_button.pack(pady=5, anchor="center")
        self.widgets.append(self.change_pin_button)

        self.back_button = tk.Button(self.root, text="Back", font=("Arial", 14), command=self.show_main_screen,
                                     activebackground="lightblue", activeforeground="black")
        self.back_button.pack(pady=5, anchor="center")
        self.widgets.append(self.back_button)

    def change_pin(self):
        old_pin = self.old_pin_entry.get()
        new_pin = self.new_pin_entry.get()
        if old_pin == self.pin:
            self.pin = new_pin
            messagebox.showinfo("Success", "PIN changed successfully")
            self.show_main_screen()
        else:
            messagebox.showerror("Error", "Incorrect old PIN")

    def deposit(self):
        amount = self.get_amount()
        if amount is not None:
            self.balance += amount
            self.history.append(f"Deposited: ${amount}")
            self.update_balance()
            messagebox.showinfo("Success", f"Deposited ${amount}")
            self.show_main_screen()

    def withdraw(self):
        amount = self.get_amount()
        if amount is not None:
            if amount > self.balance:
                messagebox.showerror("Error", "Insufficient funds")
            else:
                self.balance -= amount
                self.history.append(f"Withdrew: ${amount}")
                self.update_balance()
                messagebox.showinfo("Success", f"Withdrew ${amount}")
                self.show_main_screen()

    def transfer(self):
        amount = self.get_amount()
        account_number = self.account_entry.get()
        if amount is not None and account_number:
            if amount > self.balance:
                messagebox.showerror("Error", "Insufficient funds")
            else:
                self.balance -= amount
                self.history.append(f"Transferred: ${amount} to account {account_number}")
                self.update_balance()
                messagebox.showinfo("Success", f"Transferred ${amount} to account {account_number}")
                self.show_main_screen()
        else:
            messagebox.showerror("Error", "Invalid amount or account number")

    def show_history(self):
        if self.history:
            history_str = "\n".join(self.history)
            messagebox.showinfo("Transaction History", history_str)
        else:
            messagebox.showinfo("Transaction History", "No transactions yet")

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance}")

    def get_amount(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
            return None

    def clear_screen(self):
        for widget in self.widgets:
            widget.pack_forget()
        self.widgets.clear()
        for widget in self.widgets:
            widget.pack_forget()
    def create_label(self, text, font_size):
        label = tk.Label(self.root, text=text, font=("Arial", font_size), bg=self.canvas["bg"])
        label.pack(pady=10, anchor="center")
        self.widgets.append(label)
if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM()
    atm.setup(root)
    root.mainloop()
