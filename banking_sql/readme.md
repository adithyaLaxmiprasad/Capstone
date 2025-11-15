# Banking SQL Module (MySQL)

This folder contains SQL scripts for the Banking System database used in the Capstone project.

## Files Included

1. **create_tables.sql**
   - Creates `customers`, `accounts`, and `transactions` tables.
   - Includes primary keys, foreign keys, and constraints.

2. **insert_sample_data.sql**
   - Inserts sample records for testing the database.

3. **queries.sql**
   - Contains commonly used SQL queries.
   - Covers SELECT, JOIN, GROUP BY, ORDER BY, and filtering.

4. **views.sql**
   - Defines SQL views:
     - `customer_account_summary`
     - `last_10_transactions`

5. **stored_procedures.sql**
   - Stored procedures:
     - `deposit_amount`
     - `withdraw_amount` (with validation)

## How to Run

1. Open MySQL Workbench
2. Create schema:
