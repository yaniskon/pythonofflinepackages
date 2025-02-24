import pyodbc
import duckdb
import pandas as pd

# Connection to SQL Server
server = 'DESKTOP-5RJSIM1\\MSSQLSERVERDEV'
database = 'feestje'
username = 'hello'
password = 'hello'
conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
conn = pyodbc.connect(conn_str)

# Query the data
query = "SELECT * FROM [feestje].[dbo].[logging]"
df = pd.read_sql(sql = query, con = conn)
print(df)
# Close the connection
conn.close()

# Use DuckDB to process the data
duckdb_conn = duckdb.connect()
duckdb.sql("CREATE TABLE logging AS SELECT * FROM my_df")
duckdb.sql("SELECT * FROM FROM my_df")



# Export to Parquet
duckdb_df.to_parquet("output.parquet")

# # Export to Parquet
# duckdb_df.to_parquet("outputhello.parquet")
