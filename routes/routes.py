from fastapi import APIRouter

from user.models import UserCreate, UserLogin

from user.user_manager import create_user, login_user

from db.database_users import connect_to_database


conn = connect_to_database()

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/check")
async def check_db_connection():
    try:
        # Test connection
        cursor = conn.cursor()
        cursor.execute("SELECT 'Succesful connection '")
        result = cursor.fetchone()[0]
        cursor.close()
        return {"message": result}
    except Exception as e:
        return {"error": str(e)}

@router.post("/create_user")
# this function receives a user object from the registration form
async def create_user(user: UserCreate):

    return create_user(user)
    
    
@router.post("/login")
# this function receives a user login object from the login form
async def login(user_login: UserLogin):

    return login_user(user_login)
   
