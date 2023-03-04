# Write your MySQL query statement below
select name as Customers from Customers cus left outer join Orders ord on cus.Id = ord.CustomerId
WHERE ord.CustomerId IS NULL 
