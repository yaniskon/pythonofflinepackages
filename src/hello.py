import pyodbc
import pandas as pd
import duckdb

# Database connection details
SERVER = 'DESKTOP-5RJSIM1\MSSQLSERVERDEV'
DATABASE = 'feestje'
USERNAME = 'hello'
PASSWORD = 'hello'
DRIVER = 'ODBC Driver 17 for SQL Server'  # Adjust if using a different version

# Query to run
QUERY = '''
SELECT TOP (1000) [RowNumber]
      ,[EventClass]
      ,[ApplicationName]
      ,[ClientProcessID]
      ,[DatabaseID]
      ,[DatabaseName]
      ,[EventSequence]
      ,[GroupID]
      ,[Handle]
      ,[HostName]
      ,[IsSystem]
      ,[LoginName]
      ,[LoginSid]
      ,[NTDomainName]
      ,[NTUserName]
      ,[RequestID]
      ,[SPID]
      ,[ServerName]
      ,[SessionLoginName]
      ,[StartTime]
      ,[TransactionID]
      ,[XactSequence]
      ,[CPU]
      ,[Duration]
      ,[EndTime]
      ,[Error]
      ,[Reads]
      ,[RowCounts]
      ,[TextData]
      ,[Writes]
      ,[IntegerData]
      ,[IntegerData2]
      ,[LineNumber]
      ,[NestLevel]
      ,[Offset]
      ,[EventSubClass]
      ,[ObjectID]
      ,[ObjectName]
      ,[ObjectType]
      ,[SqlHandle]
      ,[State]
      ,[MethodName]
      ,[BinaryData]
      ,[SourceDatabaseID]
      ,[Success]
      ,[GUID]
      ,[IndexID]
  FROM [feestje].[dbo].[logging]
'''

# Output file name
OUTPUT_FILE = 'hello_python_logging.parquet'

def connect_to_sql_server():
    """Establish a connection to the SQL Server."""
    conn_str = (
        f'DRIVER={{{DRIVER}}};'
        f'SERVER={SERVER};'
        f'DATABASE={DATABASE};'
        f'UID={USERNAME};'
        f'PWD={PASSWORD};'
        'Trusted_Connection=no;'
    )
    try:
        conn = pyodbc.connect(conn_str)
        print("Connected to the database successfully.")
        return conn
    except Exception as e:
        print(f"Failed to connect to the database. Error: {e}")
        exit()

def query_and_export():
    """Query the database and export the result to a Parquet file."""
    conn = connect_to_sql_server()
    
    # Execute query and load into DataFrame
    df = pd.read_sql_query(QUERY, conn)
    print(f"Query executed successfully. Retrieved {len(df)} rows.")
    print(df)
    # Export to Parquet using duckdb
    # duckdb.write_parquet(df, OUTPUT_FILE)
    # print(f"Data exported successfully to {OUTPUT_FILE}")

if __name__ == '__main__':
    query_and_export()
