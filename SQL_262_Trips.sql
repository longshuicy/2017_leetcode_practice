# Write your MySQL query statement below
SELECT Request_at as Day, ROUND(COUNT(IF(Status != 'completed', TRUE, NULL)) / COUNT(*),2) as 'Cancellation Rate'
    FROM Trips 
    WHERE Request_at between '2013-10-01' and '2013-10-03'
    AND Client_Id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
    GROUP BY Request_at;
