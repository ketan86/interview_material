-- Question 39
-- Table: Prices

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | product_id    | int     |
-- | start_date    | date    |
-- | end_date      | date    |
-- | price         | int     |
-- +---------------+---------+
-- (product_id, start_date, end_date) is the primary key for this table.
-- Each row of this table indicates the price of the product_id in the period
-- from start_date to end_date. For each product_id there will be no two
-- overlapping periods. That means there will be no two intersecting periods for
-- the same product_id.


-- Table: UnitsSold

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | product_id    | int     |
-- | purchase_date | date    |
-- | units         | int     |
-- +---------------+---------+
-- There is no primary key for this table, it may contain duplicates.
-- Each row of this table indicates the date, units and product_id of each
-- product sold.


-- Write an SQL query to find the average selling price for each product.

-- average_price should be rounded to 2 decimal places.

-- The query result format is in the following example:

-- Prices table:
-- +------------+------------+------------+--------+
-- | product_id | start_date | end_date   | price  |
-- +------------+------------+------------+--------+
-- | 1          | 2019-02-17 | 2019-02-28 | 5      |
-- | 1          | 2019-03-01 | 2019-03-22 | 20     |
-- | 2          | 2019-02-01 | 2019-02-20 | 15     |
-- | 2          | 2019-02-21 | 2019-03-31 | 30     |
-- +------------+------------+------------+--------+

-- UnitsSold table:
-- +------------+---------------+-------+
-- | product_id | purchase_date | units |
-- +------------+---------------+-------+
-- | 1          | 2019-02-25    | 100   |
-- | 1          | 2019-03-01    | 15    |
-- | 2          | 2019-02-10    | 200   |
-- | 2          | 2019-03-22    | 30    |
-- +------------+---------------+-------+

-- Result table:
-- +------------+---------------+
-- | product_id | average_price |
-- +------------+---------------+
-- | 1          | 6.96          |
-- | 2          | 16.96         |
-- +------------+---------------+
-- Average selling price = Total Price of Product / Number of products sold.
-- Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96
-- Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96

-- Solution

SELECT t.product_id,
    round(SUM(t.cost)/t.units, 2) as average_price
FROM
    -- UnitsSold table:
    -- +------------+---------------+-------+
    -- | product_id | purchase_date | units |
    -- +------------+---------------+-------+
    -- | 1          | 2019-02-25    | 100   |  5
    -- | 1          | 2019-03-01    | 15    |  20
    -- | 2          | 2019-02-10    | 200   |  15
    -- | 2          | 2019-03-22    | 30    |  30
    -- +------------+---------------+-------+

    (
    SELECT p.product_id, SUM(us.units) as units, (us.units * p.price) as cost
    FROM Prices as p
        INNER JOIN UnitsSold as us
        ON p.product_id = us.product_id AND
            us.purchase_date BETWEEN p.start_date AND p.end_date
    ) as t
GROUP BY product_id


-- Without subquery
SELECT
    p.product_id,
    round(
        SUM(us.units * p.price) / SUM(us.units), 2
    ) as average_price
FROM Prices as p
    INNER JOIN UnitsSold as us
    ON p.product_id = us.product_id AND
        us.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY product_id

-- From Author
Select d.product_id, round((sum(price*units)+0.00)/(sum(units)+0.00),2) as average_price
from(
Select *
    from prices p
natural join
    unitssold u 
where u.purchase_date between p.start_date and p.end_date
) d
group by d.product_id 