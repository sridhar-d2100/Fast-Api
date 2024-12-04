from fastapi import FastAPI, HTTPException, Query
from supabase import create_client, Client
from typing import Optional

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Supabase client
url: str = "https://gztwxiuuautxwkghxehl.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd6dHd4aXV1YXV0eHdrZ2h4ZWhsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzA0NjE3MDEsImV4cCI6MjA0NjAzNzcwMX0.PbQkDpl8RuHTEhf6puH4emhbKv0wzmFQZjbYUpnRizQ"
supabase: Client = create_client(url, key)

app = FastAPI()

@app.get("/schools/")
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
