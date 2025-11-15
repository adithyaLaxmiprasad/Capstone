USE banking_system;

-- View 1: Customer + Account Summary
CREATE OR REPLACE VIEW customer_account_summary AS
SELECT
    c.customer_id,
    c.full_name,
    a.account_number,
    a.account_type,
    a.balance
FROM customers c
JOIN accounts a ON c.customer_id = a.customer_id;


-- View 2: Recent Transactions
CREATE OR REPLACE VIEW last_10_transactions AS
SELECT
    txn_id,
    account_number,
    txn_type,
    amount,
    timestamp
FROM transactions
ORDER BY timestamp DESC
LIMIT 10;


SELECT * FROM last_10_transactions;


SELECT * FROM accounts WHERE account_number = 1001;
SELECT * FROM transactions WHERE account_number = 1001 ORDER BY txn_id DESC LIMIT 1;
