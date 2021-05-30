-- Question 13
-- Table: Ads

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | ad_id         | int     |
-- | user_id       | int     |
-- | action        | enum    |
-- +---------------+---------+
-- (ad_id, user_id) is the primary key for this table. Each row of this table
-- contains the ID of an Ad, the ID of a user and the action taken by this user
-- regarding this Ad. The action column is an ENUM type of ('Clicked', 'Viewed',
-- 'Ignored').


-- A company is running Ads and wants to calculate the performance of each Ad.

-- Performance of the Ad is measured using Click-Through Rate (CTR) where:

-- ctr = 0 if Number of Clicks for Ad + Number of Views for Ad = 0
--                      Number of Clicks for Ad
-- ctr =      ----------------------------------------------
--          Number of Clicks for Ad + Number of Views for Ad

-- Write an SQL query to find the ctr of each Ad.

-- Round ctr to 2 decimal points. Order the result table by ctr in descending
-- order and by ad_id in ascending order in case of a tie.

-- The query result format is in the following example:

-- Ads table:
-- +-------+---------+---------+
-- | ad_id | user_id | action  |
-- +-------+---------+---------+
-- | 1     | 1       | Clicked |
-- | 2     | 2       | Clicked |
-- | 3     | 3       | Viewed  |
-- | 5     | 5       | Ignored |
-- | 1     | 7       | Ignored |
-- | 2     | 7       | Viewed  |
-- | 3     | 5       | Clicked |
-- | 1     | 4       | Viewed  |
-- | 2     | 11      | Viewed  |
-- | 1     | 2       | Clicked |
-- +-------+---------+---------+
-- Result table:
-- +-------+-------+
-- | ad_id | ctr   |
-- +-------+-------+
-- | 1     | 66.67 |
-- | 3     | 50.00 |
-- | 2     | 33.33 |
-- | 5     | 0.00  |
-- +-------+-------+
-- for ad_id = 1, ctr = (2/(2+1)) * 100 = 66.67
-- for ad_id = 2, ctr = (1/(1+2)) * 100 = 33.33
-- for ad_id = 3, ctr = (1/(1+1)) * 100 = 50.00
-- for ad_id = 5, ctr = 0.00, Note that ad_id = 5 has no clicks or views.
-- Note that we don't care about Ignored Ads.
-- Result table is ordered by the ctr. in case of a tie we order them by ad_id

-- Solution

SELECT
    ad_id,
    -- if clicks and views are 0, return 0 else find the rate
    (
        case when
            t.clicks + t.views = 0 then 0
        else
            round(t.clicks / (t.clicks + t.views) * 100, 2)
        end
    ) as ctr

FROM
    -- Group by ad_id and find clicks and views
    (
        SELECT
        ad_id,
        SUM(case when action='Clicked' then 1 else 0 end) as clicks,
        SUM(case when action='Viewed' then 1 else 0 end) as views
    FROM ads
    GROUP BY ad_id
) as t

-- order by ctr desc and later ad_id by asc
ORDER BY ctr DESC, ad_id ASC


