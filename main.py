import pandas as pd
import sqlite3
import os

# 1. Connect to (or create) a database file
conn = sqlite3.connect('retail_data.db')

# 2. List of files to import
files = [
    'olist_customers_dataset.csv',
    'olist_orders_dataset.csv',
    'olist_order_items_dataset.csv'
]

# 3. Load each CSV into the SQL Database
for file in files:
    table_name = file.replace('.csv', '')
    file_path = os.path.join('data', file)
    
    df = pd.read_csv(file_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"✅ Imported {table_name} into SQL database.")

conn.close()
# ... (previous code remains above)

# Connect to the DB we created earlier
conn = sqlite3.connect('retail_data.db')

# The SQL Query to create our Master Dataset
query = """
SELECT 
    c.customer_unique_id,
    c.customer_city,
    c.customer_state,
    o.order_id,
    o.order_purchase_timestamp,
    SUM(i.price + i.freight_value) AS total_order_revenue,
    COUNT(i.product_id) AS items_count
FROM olist_orders_dataset o
JOIN olist_order_items_dataset i ON o.order_id = i.order_id
JOIN olist_customers_dataset c ON o.customer_id = c.customer_id
WHERE o.order_status = 'delivered'
GROUP BY o.order_id;
"""

# Run the query and save to a new CSV
master_df = pd.read_sql_query(query, conn)
master_df.to_csv('data/ecommerce_master.csv', index=False)

print("✅ Phase 2 Complete: ecommerce_master.csv created with KPIs.")
conn.close()

# ... previous SQL code ...
from cleaner import DataCleaner

# 1. Initialize the cleaner with the CSV we created in Phase 2
cleaner = DataCleaner('data/ecommerce_master.csv')

# 2. Run the cleaning steps
cleaner.format_dates('order_purchase_timestamp')
cleaner.handle_nulls()
cleaner.remove_outliers('total_order_revenue')

# 3. Save the final version for Tableau
cleaner.save_data('data/ecommerce_final_tableau.csv')

print("\n🚀 PIPELINE COMPLETE: Your data is ready for Tableau!")