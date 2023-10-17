-- lists all records score >= 10
-- Records should be ordered by score (top first)
--The database name will be passed as an argument of the mysql command
SELECT 'score', 'name' FROM 'second_table' WHERE 'score' >= 10 ORDER BY 'score' DESC;
