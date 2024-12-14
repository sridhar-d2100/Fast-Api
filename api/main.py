from fastapi import FastAPI
import psycopg2
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow specific origins, methods, and headers
origins = [
    "https://fast-api-l0qs.onrender.com", # Allow other domains as necessary
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"], # Adjust methods as needed
    allow_headers=["Content-Type", "Authorization"], # Adjust headers as needed
)

# Database connection details
USER = "postgres.gztwxiuuautxwkghxehl"
PASSWORD = "sridhar6379426473"
HOST = "aws-0-ap-southeast-1.pooler.supabase.com"
PORT = "6543"
DBNAME = "postgres"

# Establishing the connection
conn = psycopg2.connect(
    dbname=DBNAME,
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT
)

@app.get("/sales")
def get_sales():
    # Query to select from the sales table
    query = "select * from salestable "
    df = pd.read_sql(query, conn)

    # Fill NaN values with 0
    df = df.fillna(0)

    # Close the connection
    

    # Return the dataframe as JSON
    return df.to_dict(orient="records")
