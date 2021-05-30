-- Question 14
-- Table: Person

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | PersonId    | int     |
-- | FirstName   | varchar |
-- | LastName    | varchar |
-- +-------------+---------+
-- PersonId is the primary key column for this table.
-- Table: Address

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | AddressId   | int     |
-- | PersonId    | int     |
-- | City        | varchar |
-- | State       | varchar |
-- +-------------+---------+
-- AddressId is the primary key column for this table.


-- Write a SQL query for a report that provides the following information for each person in the Person table,
-- regardless if there is an address for each of those people:

-- FirstName, LastName, City, State

-- Runtime: 366 ms, faster than 26.11% 
-- Solution
SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person as P
    LEFT OUTER JOIN Address as a
    ON p.PersonId = a.PersonId