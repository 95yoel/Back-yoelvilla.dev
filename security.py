import bcrypt

# Hashes a password and returns the hashed password and salt
def hash_password(password):

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password, salt


# Checks if a password is correct and returns a boolean
def check_password(password, hashed_password):
    
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
