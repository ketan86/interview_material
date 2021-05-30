-- Question 4
-- Select all employee's name and bonus whose bonus is < 1000.

-- Table:Employee

-- +-------+--------+-----------+--------+
-- | empId |  name  | supervisor| salary |
-- +-------+--------+-----------+--------+
-- |   1   | John   |  3        | 1000   |
-- |   2   | Dan    |  3        | 2000   |
-- |   3   | Brad   |  null     | 4000   |
-- |   4   | Thomas |  3        | 4000   |
-- +-------+--------+-----------+--------+
-- empId is the primary key column for this table.
-- Table: Bonus

-- +-------+-------+
-- | empId | bonus |
-- +-------+-------+
-- | 2     | 500   |
-- | 4     | 2000  |
-- +-------+-------+
-- empId is the primary key column for this table.
-- Example ouput:

-- +-------+-------+
-- | name  | bonus |
-- +-------+-------+
-- | John  | null  |
-- | Dan   | 500   |
-- | Brad  | null  |
-- +-------+-------+
-- Solution
-- ?? Why NULL Check ? No null value present in bonus column of Bonus table.
SELECT
    e.name, b.bonus
FROM
    Employee as e LEFT OUTER JOIN Bonus as b ON 
    e.empId = b.empId
WHERE 
    b.bonus < 1000 OR
    b.bonus IS NULL

-- Solution 2

Select E.name, B.bonus
From Employee E left join Bonus B
    on E.empId = B.empId
where B.bonus< 1000 or B.Bonus IS NULL