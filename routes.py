from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

from security import hash_password, check_password
from database_users import connect_to_database
conn = connect_to_database()

router = APIRouter()


class UserCreate(BaseModel):
    name: str
    surname: str
    email: str
    password: str




@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/check")
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

@router.post("/create_user")
async def create_user(user: UserCreate):
    try:
        cursor = conn.cursor()

        current_date = datetime.now().isoformat()

        hashed_password, salt = hash_password(user.password)

        query = """
        INSERT INTO users (name, surname, email, password, register_date)
        VALUES (%s, %s, %s, %s, %s)
        """
        
        cursor.execute(query, (user.name, user.surname, user.email, hashed_password, current_date))
        conn.commit()
        cursor.close()
        return {"message": "Usuario creado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    