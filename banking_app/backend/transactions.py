from collections import deque
from datetime import datetime


class Transaction:
    def __init__(self, account_number, txn_type, amount):
        self.account_number = account_number
        self.txn_type = txn_type  # "DEPOSIT" or "WITHDRAW"
        self.amount = amount
        self.timestamp = datetime.now()

    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.txn_type} ₹{self.amount} (Acc: {self.account_number})"


class TransactionManager:
    """Handles STACK and QUEUE for transactions"""

    def __init__(self):
        self.transaction_history = {}     # dict: acc_num -> list of transactions
        self.undo_stack = []             # STACK for undo
        self.pending_queue = deque()     # QUEUE for pending transactions

    def record_transaction(self, account_number, txn_type, amount):
        transaction = Transaction(account_number, txn_type, amount)

        # Save in history dict
        if account_number not in self.transaction_history:
            self.transaction_history[account_number] = []
        self.transaction_history[account_number].append(transaction)

        # Push to undo stack
        self.undo_stack.append(transaction)

        return transaction

    def get_history(self, account_number):
        return self.transaction_history.get(account_number, [])

    # -------------------------
    # STACK: Undo last transaction
    # -------------------------
    def undo_last(self):
        if not self.undo_stack:
            return None
        return self.undo_stack.pop()

    # -------------------------
    # QUEUE: Pending Transactions (Simulation)
    # -------------------------
    def add_pending(self, account_number, txn_type, amount):
        self.pending_queue.append(Transaction(account_number, txn_type, amount))

    def process_next_pending(self):
        if not self.pending_queue:
            return None
        return self.pending_queue.popleft()
