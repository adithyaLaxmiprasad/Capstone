import tkinter as tk
from tkinter import ttk, messagebox

# Import your backend modules
from banking_app.backend.accounts import BankAccount, SavingsAccount
from banking_app.backend.customer import CustomerManager
from banking_app.backend.transactions import TransactionManager


# -----------------------------
# Glue Layer: BankSystem
# -----------------------------
class BankSystem:
    """
    Small 'service' class that ties together:
    - CustomerManager  (list of customers)
    - TransactionManager (history dict, undo stack, pending queue)
    - Accounts registry (dict: account_number -> BankAccount/SavingsAccount)
    """
    def __init__(self):
        self.customers = CustomerManager()
        self.txn_mgr = TransactionManager()
        self.accounts = {}  # dict: account_number -> BankAccount/SavingsAccount
        self._acc_counter = 5000

    def _next_acc_number(self):
        self._acc_counter += 1
        return self._acc_counter

    def create_account(self, name, email, phone, initial_deposit=0.0,
                       is_savings=True, interest_rate=0.03):
        """
        Creates a customer + account. Returns (customer_id, account_number).
        Raises ValueError for invalid inputs.
        """
        if not name or not email or not phone:
            raise ValueError("All fields (name, email, phone) are required.")
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")

        # Create customer (list DS under the hood)
        customer = self.customers.add_customer(name, email, phone)

        # Create account instance
        acc_num = self._next_acc_number()
        if is_savings:
            account = SavingsAccount(acc_num, customer.name, balance=0.0, interest_rate=interest_rate)
        else:
            account = BankAccount(acc_num, customer.name, balance=0.0)

        # Initial deposit (if any)
        if initial_deposit > 0:
            account.deposit(initial_deposit)
            self.txn_mgr.record_transaction(acc_num, "DEPOSIT", initial_deposit)

        # Store in registry (dict DS)
        self.accounts[acc_num] = account
        return customer.customer_id, acc_num

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError("Account not found.")
        account.deposit(amount)
        self.txn_mgr.record_transaction(account_number, "DEPOSIT", amount)
        return account.balance

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError("Account not found.")
        account.withdraw(amount)
        self.txn_mgr.record_transaction(account_number, "WITHDRAW", amount)
        return account.balance

    def get_balance(self, account_number):
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError("Account not found.")
        return account.balance

    def get_history(self, account_number):
        return self.txn_mgr.get_history(account_number)


# -----------------------------
# Tkinter GUI
# -----------------------------
class BankingApp(tk.Tk):
    def __init__(self, bank_system: BankSystem):
        super().__init__()
        self.title("Simple Banking App (Option A)")
        self.geometry("720x480")
        self.resizable(False, False)

        self.bank = bank_system

        # Root container to hold frames
        container = ttk.Frame(self, padding=16)
        container.pack(fill="both", expand=True)

        # Navigation: keep a dict of frames
        self.frames = {}

        # Create all frames here (we will implement CreateAccount fully; others are stubs for now)
        for F in (HomeFrame, CreateAccountFrame, DepositFrame, WithdrawFrame, BalanceFrame, HistoryFrame):
            frame = F(parent=container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show Home at start
        self.show_frame("HomeFrame")

    def show_frame(self, frame_name: str):
        frame = self.frames[frame_name]
        frame.tkraise()


# -----------------------------
# Home Frame (menu)
# -----------------------------
class HomeFrame(ttk.Frame):
    def __init__(self, parent, controller: BankingApp):
        super().__init__(parent)
        self.controller = controller

        title = ttk.Label(self, text="Banking Dashboard", font=("Segoe UI", 20, "bold"))
        subtitle = ttk.Label(self, text="Choose an action", font=("Segoe UI", 12))

        title.pack(pady=(10, 4))
        subtitle.pack(pady=(0, 16))

        # Child frame to hold buttons (we'll use grid ONLY inside this frame)
        btns_frame = ttk.Frame(self)
        btns_frame.pack(pady=12, fill="x")

        # IMPORTANT: make buttons children of btns_frame (not self)
        btn_create = ttk.Button(btns_frame, text="Create Account",
                                command=lambda: controller.show_frame("CreateAccountFrame"))
        btn_deposit = ttk.Button(btns_frame, text="Deposit",
                                 command=lambda: controller.show_frame("DepositFrame"))
        btn_withdraw = ttk.Button(btns_frame, text="Withdraw",
                                  command=lambda: controller.show_frame("WithdrawFrame"))
        btn_balance = ttk.Button(btns_frame, text="View Balance",
                                 command=lambda: controller.show_frame("BalanceFrame"))
        btn_history = ttk.Button(btns_frame, text="Transaction History",
                                 command=lambda: controller.show_frame("HistoryFrame"))

        # Use grid inside btns_frame only
        for i, widget in enumerate([btn_create, btn_deposit, btn_withdraw, btn_balance, btn_history]):
            widget.grid(row=i, column=0, padx=6, pady=6, sticky="ew")

        btns_frame.columnconfigure(0, weight=1)


# -----------------------------
# Create Account Frame (fully working)
# -----------------------------
class CreateAccountFrame(ttk.Frame):
    def __init__(self, parent, controller: BankingApp):
        super().__init__(parent)
        self.controller = controller

        title = ttk.Label(self, text="Create New Account", font=("Segoe UI", 16, "bold"))
        title.pack(pady=(10, 10))

        form = ttk.Frame(self)
        form.pack(pady=6)

        # Inputs
        ttk.Label(form, text="Full Name:").grid(row=0, column=0, sticky="e", padx=6, pady=6)
        ttk.Label(form, text="Email:").grid(row=1, column=0, sticky="e", padx=6, pady=6)
        ttk.Label(form, text="Phone:").grid(row=2, column=0, sticky="e", padx=6, pady=6)
        ttk.Label(form, text="Initial Deposit:").grid(row=3, column=0, sticky="e", padx=6, pady=6)

        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.deposit_var = tk.StringVar(value="0")

        name_entry = ttk.Entry(form, textvariable=self.name_var, width=32)
        email_entry = ttk.Entry(form, textvariable=self.email_var, width=32)
        phone_entry = ttk.Entry(form, textvariable=self.phone_var, width=32)
        deposit_entry = ttk.Entry(form, textvariable=self.deposit_var, width=32)

        name_entry.grid(row=0, column=1, padx=6, pady=6)
        email_entry.grid(row=1, column=1, padx=6, pady=6)
        phone_entry.grid(row=2, column=1, padx=6, pady=6)
        deposit_entry.grid(row=3, column=1, padx=6, pady=6)

        # Account type (Savings vs Basic)
        self.is_savings_var = tk.BooleanVar(value=True)
        savings_chk = ttk.Checkbutton(form, text="Savings Account (3% interest)", variable=self.is_savings_var)
        savings_chk.grid(row=4, column=1, sticky="w", padx=6, pady=(6, 10))

        # Buttons
        btns = ttk.Frame(self)
        btns.pack(pady=8)
        create_btn = ttk.Button(btns, text="Create Account", command=self.create_account)
        back_btn = ttk.Button(btns, text="Back", command=lambda: controller.show_frame("HomeFrame"))
        create_btn.grid(row=0, column=0, padx=8)
        back_btn.grid(row=0, column=1, padx=8)

        # Message label
        self.msg = ttk.Label(self, text="", foreground="green")
        self.msg.pack(pady=6)

    def create_account(self):
        name = self.name_var.get().strip()
        email = self.email_var.get().strip()
        phone = self.phone_var.get().strip()
        deposit_str = self.deposit_var.get().strip() or "0"

        try:
            initial_deposit = float(deposit_str)
        except ValueError:
            messagebox.showerror("Invalid Input", "Initial deposit must be a number.")
            return

        try:
            _, acc_num = self.controller.bank.create_account(
                name=name,
                email=email,
                phone=phone,
                initial_deposit=initial_deposit,
                is_savings=self.is_savings_var.get(),
                interest_rate=0.03
            )
            self.msg.config(text=f"Account created successfully! Account No: {acc_num}", foreground="green")
            # Clear fields
            self.name_var.set(""); self.email_var.set(""); self.phone_var.set(""); self.deposit_var.set("0")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


# -----------------------------
# Other screens (stubs for now)
# We'll implement them in next steps.
# -----------------------------
class DepositFrame(ttk.Frame):
    def __init__(self, parent, controller: BankingApp):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Deposit Money", font=("Segoe UI", 16, "bold")).pack(pady=12)

        form = ttk.Frame(self)
        form.pack(pady=10)

        ttk.Label(form, text="Account Number:").grid(row=0, column=0, padx=6, pady=6, sticky="e")
        ttk.Label(form, text="Amount:").grid(row=1, column=0, padx=6, pady=6, sticky="e")

        self.acc_var = tk.StringVar()
        self.amount_var = tk.StringVar()

        acc_entry = ttk.Entry(form, textvariable=self.acc_var, width=28)
        amt_entry = ttk.Entry(form, textvariable=self.amount_var, width=28)

        acc_entry.grid(row=0, column=1, padx=6, pady=6)
        amt_entry.grid(row=1, column=1, padx=6, pady=6)

        btns = ttk.Frame(self)
        btns.pack(pady=8)

        ttk.Button(btns, text="Deposit", command=self.make_deposit).grid(row=0, column=0, padx=6)
        ttk.Button(btns, text="Back", command=lambda: controller.show_frame("HomeFrame")).grid(row=0, column=1, padx=6)

        self.msg = ttk.Label(self, text="", foreground="green")
        self.msg.pack(pady=6)

    def make_deposit(self):
        acc_str = self.acc_var.get().strip()
        amt_str = self.amount_var.get().strip()

        try:
            acc_num = int(acc_str)
            amount = float(amt_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid account number or amount.")
            return

        try:
            new_balance = self.controller.bank.deposit(acc_num, amount)
            self.msg.config(text=f"Deposit successful! New Balance: ₹{new_balance}", foreground="green")
            self.acc_var.set("")
            self.amount_var.set("")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


#done depostie frame


class WithdrawFrame(ttk.Frame):
    def __init__(self, parent, controller: BankingApp):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Withdraw Money", font=("Segoe UI", 16, "bold")).pack(pady=12)

        form = ttk.Frame(self)
        form.pack(pady=10)

        ttk.Label(form, text="Account Number:").grid(row=0, column=0, padx=6, pady=6, sticky="e")
        ttk.Label(form, text="Amount:").grid(row=1, column=0, padx=6, pady=6, sticky="e")

        self.acc_var = tk.StringVar()
        self.amount_var = tk.StringVar()

        acc_entry = ttk.Entry(form, textvariable=self.acc_var, width=28)
        amt_entry = ttk.Entry(form, textvariable=self.amount_var, width=28)

        acc_entry.grid(row=0, column=1, padx=6, pady=6)
        amt_entry.grid(row=1, column=1, padx=6, pady=6)

        btns = ttk.Frame(self)
        btns.pack(pady=8)

        ttk.Button(btns, text="Withdraw", command=self.make_withdraw).grid(row=0, column=0, padx=6)
        ttk.Button(btns, text="Back", command=lambda: controller.show_frame("HomeFrame")).grid(row=0, column=1, padx=6)

        self.msg = ttk.Label(self, text="", foreground="green")
        self.msg.pack(pady=6)

    def make_withdraw(self):
        acc_str = self.acc_var.get().strip()
        amt_str = self.amount_var.get().strip()

        try:
            acc_num = int(acc_str)
            amount = float(amt_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid account number or amount.")
            return

        try:
            new_balance = self.controller.bank.withdraw(acc_num, amount)
            self.msg.config(text=f"Withdrawal successful! New Balance: ₹{new_balance}", foreground="green")
            self.acc_var.set("")
            self.amount_var.set("")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

#withdrawal frame

class BalanceFrame(ttk.Frame):
    def __init__(self, parent, controller: BankingApp):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Check Account Balance", font=("Segoe UI", 16, "bold")).pack(pady=12)

        form = ttk.Frame(self)
        form.pack(pady=10)

        ttk.Label(form, text="Account Number:").grid(row=0, column=0, padx=6, pady=6, sticky="e")

        self.acc_var = tk.StringVar()
        acc_entry = ttk.Entry(form, textvariable=self.acc_var, width=28)
        acc_entry.grid(row=0, column=1, padx=6, pady=6)

        btns = ttk.Frame(self)
        btns.pack(pady=8)

        ttk.Button(btns, text="Check Balance", command=self.check_balance).grid(row=0, column=0, padx=6)
        ttk.Button(btns, text="Back", command=lambda: controller.show_frame("HomeFrame")).grid(row=0, column=1, padx=6)

        # label to show result
        self.result_msg = ttk.Label(self, text="", font=("Segoe UI", 12))
        self.result_msg.pack(pady=10)

    def check_balance(self):
        acc_str = self.acc_var.get().strip()

        try:
            acc_num = int(acc_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid account number.")
            return

        try:
            balance = self.controller.bank.get_balance(acc_num)
            self.result_msg.config(
                text=f"Balance for Account {acc_num}: ₹{balance}",
                foreground="green"
            )
        except ValueError as e:
            messagebox.showerror("Error", str(e))
#Balance frame done
class HistoryFrame(ttk.Frame):
    def __init__(self, parent, controller: BankingApp):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Transaction History", font=("Segoe UI", 16, "bold")).pack(pady=12)

        form = ttk.Frame(self)
        form.pack(pady=10)

        ttk.Label(form, text="Account Number:").grid(row=0, column=0, padx=6, pady=6, sticky="e")

        self.acc_var = tk.StringVar()
        acc_entry = ttk.Entry(form, textvariable=self.acc_var, width=28)
        acc_entry.grid(row=0, column=1, padx=6, pady=6)

        ttk.Button(
            self,
            text="Show History",
            command=self.show_history
        ).pack(pady=8)

        # Scrollable history list
        self.text_box = tk.Text(self, height=12, width=70, state="disabled")
        self.text_box.pack(pady=10)

        ttk.Button(
            self,
            text="Back",
            command=lambda: controller.show_frame("HomeFrame")
        ).pack(pady=6)

    def show_history(self):
        acc_str = self.acc_var.get().strip()

        try:
            acc_num = int(acc_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid account number.")
            return

        history = self.controller.bank.get_history(acc_num)

        if not history:
            messagebox.showinfo("No Records", "No transaction history for this account.")
            return

        # Update text box
        self.text_box.config(state="normal")
        self.text_box.delete(1.0, tk.END)

        for txn in history:
            self.text_box.insert(tk.END, str(txn) + "\n")

        self.text_box.config(state="disabled")

# -----------------------------
# Entrypoint
# -----------------------------
if __name__ == "__main__":
    app = BankingApp(bank_system=BankSystem())
    app.mainloop()
