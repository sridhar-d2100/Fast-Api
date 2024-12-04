from fastapi import FastAPI, HTTPException, Query
from supabase import create_client, Client
from typing import Optional
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Supabase client
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = FastAPI()

@app.get("/api/schools/")
async def get_school_by_name(school_name: Optional[str] = Query(None)):
    try:
        if not school_name:  # If no school_name is provided, fetch all schools
            response = supabase.table("schools").select("*").execute()
        else:  # Fetch schools matching the provided name
            response = supabase.table("schools").select("*").ilike("school_name", f"%{school_name}%").execute()

        if not response.data:  # Check if data is empty
            return {"school_data": []}

        return {"school_data": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")
