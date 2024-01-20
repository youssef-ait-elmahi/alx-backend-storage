-- Create the SafeDiv function .
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10, 2)
BEGIN
    IF b <> 0 THEN
        RETURN a / b;
    ELSE
        RETURN 0;
    END IF;
END //
DELIMITER ;