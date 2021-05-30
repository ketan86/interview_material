-- Question 11
-- Write a SQL query to find all duplicate emails in a table named Person.

-- +----+---------+
-- | Id | Email   |
-- +----+---------+
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- +----+---------+
-- For example, your query should return the following for the above table:

-- +---------+
-- | Email   |
-- +---------+
-- | a@b.com |
-- +---------+


-- Solution - Using Group By
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1

-- Solution 2 - Using Self Join
SELECT DISTINCT p1.Email
FROM Person as p1
    INNER JOIN Person as p2
    ON p1.Email = p2.Email
        AND p1.Id != p2.Id

-- Solution 3

Select Email
from
    (Select Email, count(Email)
    from person
    group by Email
    having count(Email)>1) a