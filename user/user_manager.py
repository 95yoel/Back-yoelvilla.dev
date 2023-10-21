import bcrypt
from datetime import datetime
from security import hash_password
from db.database_users import connect_to_database

conn = connect_to_database()

def create_user(user):
    try:
        # initialize connection
        cursor = conn.cursor()
        # format current date
        current_date = datetime.now().isoformat()
        # Hash password
        hashed_password, salt = hash_password(user.password)
        # query for inserting user
        query = """
        INSERT INTO users (name, surname, email, password, register_date,salt)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        # execute query
        cursor.execute(query, (user.name, user.surname, user.email, hashed_password, current_date,salt))
        # commit changes
        conn.commit()
        # close connection
        cursor.close()
        # return success message
        return {"message": "User created successfully"}
    except Exception as e:
        return {"error": str(e)}
    
def login_user(user_login):
    try:
        # initialize connection
        cursor = conn.cursor()
        # Search the email provided by the user in the database
        cursor.execute("SELECT password, salt FROM users WHERE email = %s", (user_login.email,))

        # Fetch one record
        user_data = cursor.fetchone()

        # if user not found return error
        if user_data is None:
            return {"error": "User not found"}
        
        # obtain stored password hash and salt from database
        stored_password_hash, salt = user_data

        # format stored password hash
        stored_password_hash = bytes(stored_password_hash)

        # format stored salt in database
        salt_bytes = bytes(salt)

        # encode the password provided by the user in the login form
        encoded_password = user_login.password.encode('utf-8')

        # Generate hash from hashed password and salt used to create it
        hashed_password = bcrypt.hashpw(encoded_password, salt_bytes)

        # Compare both hashes and return success message if they match 
        if hashed_password == stored_password_hash:
            return {"message": "Successful login"}
        else:
            return {"error": "Wrong password"}

    except Exception as e:
        return {"error": str(e)}
