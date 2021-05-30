-- Question 32 Write a SQL query to delete all duplicate email entries in a
-- table named Person, keeping only unique emails based on its smallest Id.

-- +----+------------------+
-- | Id | Email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- | 3  | john@example.com |
-- +----+------------------+
-- Id is the primary key column for this table.

-- For example, after running your query, the above Person table should have the
-- following rows:

-- +----+------------------+
-- | Id | Email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- +----+------------------+

-- Solution


-- +----+------------------+
-- | Id | Email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- | 3  | john@example.com |
-- +----+------------------+

-- Idea is to find all the duplicate rows (after first id due to smallest
-- id constraint). When doing self join, joins will happen for smallest id
-- matching the smallest id in second table and all the emails where id
-- is greater than current id, will be selected for delete action.
DELETE p1
FROM Person p1
    INNER JOIN Person p2
    ON  p1.Email = p2.Email
        -- only consider the rows where p1.Id > p2.Id or p1.Id != p2.Id
        AND p1.Id > p2.Id;


-- Solution 2
With
    t1
    as
    (
        Select *,
            row_number() over(partition by email order by id) as rk
        from person
    )
Delete from person
where id in (Select t1.id
from t1
where t1.rk>1)