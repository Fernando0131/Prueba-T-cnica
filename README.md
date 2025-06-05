# Prueba-T-cnica
Este repositorio contiene una solución de prueba técnica para Ingeniería de Datos, basada en el dataset público de [Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
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

El script `etl_olist_sqlserver.py` realiza:
1. Lectura de los CSV
2. Limpieza de datos y conversión de fechas
3. Carga en SQL Server con SQLAlchemy y pyodbc

### Requisitos

```bash
pip install pandas sqlalchemy pyodbc
