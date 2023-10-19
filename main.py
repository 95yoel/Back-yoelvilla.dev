from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import json


# acces to database config on json file
with open("database_config.json", "r") as file:
    config = json.load(file)


# connection to postgresql database with psycopg2
conn = psycopg2.connect(
    host=config.get("database_host"),
    database=config.get("database_name"),
    user=config.get("database_user"), 
    password=config.get("database_password")
)



app = FastAPI()


# CORS CONFIG
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/check")
async def check_db_connection():
    try:
        # Test connection
        cursor = conn.cursor()
        cursor.execute("SELECT 'Conexión exitosa'")
        result = cursor.fetchone()[0]
        cursor.close()
        return {"message": result}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

