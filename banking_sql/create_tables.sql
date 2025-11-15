-- ===================================
-- DATABASE CREATION
-- ===================================
CREATE DATABASE IF NOT EXISTS banking_system;
USE banking_system;


-- ===================================
-- TABLE 1: customers
-- ===================================
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- ===================================
-- TABLE 2: accounts
-- ===================================
CREATE TABLE accounts (
    account_number INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    account_type ENUM('Savings','Current') DEFAULT 'Savings',
    balance DECIMAL(10,2) DEFAULT 0,
    interest_rate DECIMAL(5,2) DEFAULT 3.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);


-- ===================================
-- TABLE 3: transactions
-- ===================================
CREATE TABLE transactions (
    txn_id INT AUTO_INCREMENT PRIMARY KEY,
    account_number INT NOT NULL,
    txn_type ENUM('DEPOSIT','WITHDRAW') NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (account_number) REFERENCES accounts(account_number)
);
