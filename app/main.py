import os
from dotenv import load_dotenv  # Import dotenv
from fastapi import FastAPI, HTTPException
from supabase import create_client, Client
from typing import Optional

# Load environment variables from the .env file
load_dotenv()  # This will load the .env variables automatically

# Create FastAPI instance
app = FastAPI()

# Set up Supabase connection using environment variables
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.get("/schools/")
async def get_school_by_name(school_name: Optional[str] = None):
    if not school_name:
        raise HTTPException(status_code=400, detail="School name query parameter is required")
    
    # Query the database for the school with the specified name
    response = supabase.table("schools").select("*").eq("school_name", school_name).execute()

    # Check if the response has data
    if len(response.data) == 0:
        raise HTTPException(status_code=404, detail="School not found")
    
    return {"school_data": response.data}
