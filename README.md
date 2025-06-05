# Prueba-T-cnica
Este repositorio contiene una solución de prueba técnica para Analista de Datos, basada en el dataset público de [Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
# Olist ETL - SQL Server

## 📦 Archivos utilizados

- `olist_orders_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_customers_dataset.csv`

## 🧱 Modelo de datos

Relaciones:
- Una orden tiene un cliente
- Una orden puede tener múltiples ítems

Tablas:
- `customers`
- `orders`
- `order_items`

Incluye archivo `ddl_script.sql` con las instrucciones para crear las tablas en SQL Server.

## ⚙️ Proceso ETL

Los script `etl_olist_sqlserver.py` y `etl_olist_sqlserver_conexion.py` realizan:
1. Conexion con la base de datos 
2. Lectura de los CSV
3. Limpieza de datos y conversión de fechas
4. Carga en SQL Server con SQLAlchemy y pyodbc

### Requisitos

```bash
pip install pandas sqlalchemy pyodbc

### Dashboard en power BI
Como un extra decidi agregar tambien un archivo PBIX donde se puede apreciar el uso de los datos extraidos a travez de difentes graficos y objetos.
- `OLIST - Dashboard de Ventas y Pedidos.pbix` 
