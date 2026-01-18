SELECT 
    c.customer_unique_id,
    c.customer_city,
    c.customer_state,
    o.order_id,
    o.order_purchase_timestamp,
    -- KPI: Total Revenue per order (Price + Shipping)
    SUM(i.price + i.freight_value) AS total_order_revenue,
    -- KPI: Number of items in this order
    COUNT(i.product_id) AS items_count
FROM olist_orders_dataset o
JOIN olist_order_items_dataset i ON o.order_id = i.order_id
JOIN olist_customers_dataset c ON o.customer_id = c.customer_id
WHERE o.order_status = 'delivered'
GROUP BY o.order_id;