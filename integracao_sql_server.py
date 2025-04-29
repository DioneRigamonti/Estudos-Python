import pandas as pd
import pyodbc

def extract_from_sqlserver(query, server, database):
    # String de conexão usando Trusted Connection (Autenticação do Windows)
    conn_str = (
        f"DRIVER={{SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )
    conn = pyodbc.connect(conn_str)

    # Executa a query
    print("Extraindo dados...")
    df = pd.read_sql(query, conn)
    conn.close()
    print("Extração concluída!")
    return df

if __name__ == "__main__":
    # Informações da conexão
    server = "DRIGAMONTI"
    database = "ContosoRetailDW"

    # Query de extração
    query = """
        SELECT
           *
        FROM DimChannel;
    """
    df_raw = extract_from_sqlserver(query, server, database)
    print(df_raw.head())
