select * from superstore



create or replace view overview_vw as 
select round(sum(sales), 2) as total_sales,
	   round(sum(profit), 2) as total_profit,
	   round(avg(discount), 2) as avg_discount_per_order,
	   round(sum((sales - profit)), 2) as total_cost
from superstore




create or replace view regular_vw as
select row_id,
	   order_id,
	   customer_id,
	   segment,
	   country,
	   city,
	   state,
	   postal_code,
	   region,
	   product_id,
	   category,
	   sub_category,
	   product_name,
	   sales,
	   quantity,
	   discount,
	   profit,
	   order_date,
	   ship_date,
	   ship_mode,
	   (sales - profit) as cost,
	   (ship_date - order_date) AS day_difference
from superstore

	   