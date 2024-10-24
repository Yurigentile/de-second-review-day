-- add queries here!
SELECT * FROM (SELECT title,SUM(num_items) 
FROM sales INNER JOIN products ON products.id = sales.product_id 
GROUP BY title) as foo ORDER BY sum DESC limit 3;

select * from(SELECT title,sum(num_items)
*(SELECT product_cost FROM products) 
as tot FROM sales INNER JOIN products 
ON products.id = sales.product_id 
GROUP BY title) as foo ORDER BY tot DESC limit 3; 