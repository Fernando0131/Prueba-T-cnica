import pandas as pd
from sqlalchemy import text
from etl_olist_sqlserver_conexion import engine

# Lee los archivos CSV
orders = pd.read_csv("olist_orders_dataset.csv")
order_items = pd.read_csv("olist_order_items_dataset.csv")
customers = pd.read_csv("olist_customers_dataset.csv")

# Convierte las columnas en fechas
orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
orders["order_approved_at"] = pd.to_datetime(orders["order_approved_at"])
orders["order_delivered_carrier_date"] = pd.to_datetime(orders["order_delivered_carrier_date"])
orders["order_delivered_customer_date"] = pd.to_datetime(orders["order_delivered_customer_date"])
orders["order_estimated_delivery_date"] = pd.to_datetime(orders["order_estimated_delivery_date"])

# Elimina órdenes sin cliente
orders = orders.dropna(subset=["customer_id"])

# Carga a SQL Server
customers.to_sql('customers', con=engine, index=False, if_exists='append')
orders.to_sql('orders', con=engine, index=False, if_exists='append')
order_items.to_sql('order_items', con=engine, index=False, if_exists='append')

# Prueba si la insercion de datos fue exitosa
with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM customers"))
    print("🧾 Total de registros en customers:", result.scalar())





