import urllib
from sqlalchemy import create_engine, text

#Configura los parámetros de conexión
server = r'DESKTOP-ARN7LMP\SQLEXPRESS02'
database = 'olist_db'
driver = 'SQL Server Native Client 11.0'  

#Crea la cadena ODBC para autenticación de Windows
params = urllib.parse.quote_plus(
    f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
)

#Crea el motor SQLAlchemy
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

#Prueba si la conexcion con la base de datos fue exitosa
with engine.connect() as conn:
    result = conn.execute(text("SELECT GETDATE()"))
    print("✅ Conectado. Fecha actual desde SQL Server:", result.fetchone()[0])

