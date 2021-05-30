-- Question 24
-- Table my_numbers contains many numbers in column num including duplicated ones.
-- Can you write a SQL query to find the biggest number, which only appears once.

-- +---+
-- |num|
-- +---+
-- | 8 |
-- | 8 |
-- | 3 |
-- | 3 |
-- | 1 |
-- | 4 |
-- | 5 |
-- | 6 | 
-- For the sample data above, your query should return the following result:
-- +---+
-- |num|
-- +---+
-- | 6 |
-- Note:
-- If there is no such number, just output null.

-- Solution

SELECT max(t.num)
FROM
    (
    SELECT num
    FROM my_numbers
    GROUP BY num
    HAVING count(*) = 1
) as t

-- WRONG SOLUTION
---- GROUP BY returns unique results so MAX(each result) would not make
---- any difference We have to first find the numbers where count is 1
---- and then select max out of that.
select MAX(num)
from my_numbers
group by num
having count(*) = 1;

-- Author solution
Select max(a.num) as num
from
    ( 
    select num, count(*)
    from my_numbers
    group by num
    having count(*)=1
) a