from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database_users import connect_to_database


# Connect to database
conn = connect_to_database()

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

