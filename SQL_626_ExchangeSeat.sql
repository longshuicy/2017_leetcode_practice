# Write your MySQL query statement below
SELECT 
    (CASE
        WHEN MOD(id,2)!=0 AND id != counts THEN id+1
        WHEN MOD(id,2)!=0 AND id = Counts THEN id
        ELSE id-1
    END) as id, student FROM seat, (SELECT COUNT(*) as counts FROM seat) as seatCounts
    ORDER BY id ASC;
