from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Replace with your actual PostgreSQL connection details
DATABASE_URL = "postgresql://username:password@localhost/dbname"

# Create the engine and metadata
engine = create_engine(DATABASE_URL)
metadata = MetaData(bind=engine)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#user=postgres.gztwxiuuautxwkghxehl password=[YOUR-PASSWORD] host=aws-0-ap-southeast-1.pooler.supabase.com port=6543 dbname=postgres