USE banking_system;

-- Procedure: deposit amount into account
DELIMITER $$

CREATE PROCEDURE deposit_amount(
    IN acc INT,
    IN amt DECIMAL(10,2)
)
BEGIN
    UPDATE accounts
    SET balance = balance + amt
    WHERE account_number = acc;

    INSERT INTO transactions (account_number, txn_type, amount)
    VALUES (acc, 'DEPOSIT', amt);
END $$

DELIMITER ;


-- Procedure: withdraw with validation
DELIMITER $$

CREATE PROCEDURE withdraw_amount(
    IN acc INT,
    IN amt DECIMAL(10,2)
)
BEGIN
    DECLARE current_balance DECIMAL(10,2);

    SELECT balance INTO current_balance FROM accounts WHERE account_number = acc;

    IF current_balance < amt THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Insufficient balance';
    ELSE
        UPDATE accounts
        SET balance = balance - amt
        WHERE account_number = acc;

        INSERT INTO transactions (account_number, txn_type, amount)
        VALUES (acc, 'WITHDRAW', amt);
    END IF;
END $$

DELIMITER ;
