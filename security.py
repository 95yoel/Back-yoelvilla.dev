import bcrypt

# Hashes a password and returns the hashed password and salt
def hash_password(password):

    # generate a salt
    salt = bcrypt.gensalt()

    # hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password, salt



