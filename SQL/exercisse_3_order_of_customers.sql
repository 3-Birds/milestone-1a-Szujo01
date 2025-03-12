/*
Question 1: Total Orders Per Customer

Write a query to display the total number of orders placed by each customer, 
along with their name and the date they joined. Sort the results by the total number of orders in descending order.
*/

SELECT 
customers.customer_id, 
customers.customer_name, 
customers.join_date, 
COUNT(Orders.order_id) as total_orders
FROM customers
LEFT JOIN orders ON customers.customer_id=orders.customer_id
GROUP BY customers.customer_id
ORDER BY total_orders DESC;




/*
Question 2: Rank Customers by Spending

For each customer, calculate their total spending (sum of the total amounts from the `Orders` table) 
and rank them by total spending within their respective country. 
Use a **window function** to rank the customers.
*/

SELECT
customers.customer_id, 
customers.customer_name, 
customers.country,
sum(orderitems.quantity * orderitems.price) as spending,
rank() OVER (PARTITION BY customers.country ORDER BY sum(orderitems.quantity * orderitems.price)desc) as ranking 
FROM customers
join orders on customers.customer_id = orders.customer_id
join orderitems on orders.order_id = orderitems.order_id
GROUP by customers.country, customers.customer_id
order by Customers.country, ranking;
