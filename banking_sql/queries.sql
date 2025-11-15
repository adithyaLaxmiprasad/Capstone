USE banking_system;

-- 1. List all customers
SELECT * FROM customers;

-- 2. Find a customer by email
SELECT * FROM customers WHERE email = 'john@example.com';

-- 3. Get all accounts for a customer
SELECT * FROM accounts WHERE customer_id = 1;

-- 4. Total balance for all accounts
SELECT SUM(balance) AS total_bank_balance FROM accounts;

-- 5. All transactions for a specific account
SELECT * FROM transactions WHERE account_number = 1 ORDER BY timestamp DESC;

-- 6. Join customer + account details
SELECT c.full_name, a.account_number, a.balance
FROM customers c
JOIN accounts a ON c.customer_id = a.customer_id;

-- 7. Find highest balance account
SELECT * FROM accounts ORDER BY balance DESC LIMIT 1;

-- 8. Count number of savings accounts
SELECT COUNT(*) FROM accounts WHERE account_type = 'Savings';

-- 9. Find accounts created in last 7 days
SELECT * FROM accounts WHERE created_at >= NOW() - INTERVAL 7 DAY;

-- 10. Group total transactions per account
SELECT account_number, COUNT(*) AS txn_count
FROM transactions
GROUP BY account_number;
