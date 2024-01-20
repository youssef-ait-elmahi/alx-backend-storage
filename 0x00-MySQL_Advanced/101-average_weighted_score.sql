-- Create a procedure that computes the average weighted score for all users.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    DECLARE @id INT;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO @id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        CALL ComputeAverageWeightedScoreForUser(@id);
    END LOOP;

    CLOSE cur;
END //
DELIMITER ;
