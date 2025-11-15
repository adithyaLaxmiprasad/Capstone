USE banking_system;

-- Insert customers
INSERT INTO customers (full_name, email, phone) VALUES
('Adithya L', 'adithya@mail.com', '9900123456'),
('John Doe', 'john@example.com', '9876543210'),
('Jane Smith', 'jane@example.com', '9123456789');


-- Insert accounts
INSERT INTO accounts (customer_id, account_type, balance, interest_rate) VALUES
(1, 'Savings', 5000, 3.00),
(2, 'Current', 12000, 0.00),
(3, 'Savings', 8000, 3.00);


-- Insert transactions
INSERT INTO transactions (account_number, txn_type, amount) VALUES
(1, 'DEPOSIT', 500),
(1, 'WITHDRAW', 200),
(2, 'DEPOSIT', 1000),
(3, 'WITHDRAW', 500);
