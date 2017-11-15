# Write your MySQL query statement below
SELECT DISTINCT s1.* FROM 
    stadium s1, stadium s2, stadium s3
    WHERE (
            (s1.id - s2.id = 1 and s1.id - s3.id = 2 and s2.id - s3.id =1)  -- t1, t2, t3
                or
            (s2.id - s1.id = 1 and s2.id - s3.id = 2 and s1.id - s3.id =1) -- t2, t1, t3
            or
            (s3.id - s2.id = 1 and s2.id - s1.id =1 and s3.id - s1.id = 2) -- t3, t2, t1
        ) 
    AND s1.people>=100
    AND s2.people>=100
    AND s3.people>=100 ORDER BY s1.id ;
