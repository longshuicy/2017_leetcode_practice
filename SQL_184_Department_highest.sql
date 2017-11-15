# Write your MySQL query statement below

SELECT t2.Name as Department, E.Name as Employee, t1.Salary 
    FROM 
    Employee E,
    (SELECT MAX(Salary) as Salary, DepartmentId FROM Employee  GROUP BY DepartmentId) t1, 
    Department t2 
    WHERE E.salary = t1.salary AND t1.DepartmentId = t2.Id AND E.DepartmentId = t1.DepartmentId
ORDER BY Salary ASC;
