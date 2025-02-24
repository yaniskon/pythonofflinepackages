import polars as pl
from sqlalchemy import create_engine

# Create a connection string for SQL Server
pyodbc_uri = (
            "mssql+pyodbc://hello:hello@localhost:56884/feestje?"
                "driver=ODBC+Driver+17+for+SQL+Server"
                )
engine = create_engine(pyodbc_uri, fast_executemany=True)

# Read the table into a Polars DataFrame
#df = pl.read_database(
#            query="SELECT * FROM feestje.dbo.logging1000;",
#                connection=engine,
#                )
with engine.connect() as connection:
    df = pl.read_database(
        query="SELECT * FROM feestje.dbo.logging1000",
        connection=connection
    )
print(df)

df.write_parquet("logging1002.parquet")
