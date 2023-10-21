import json
import psycopg2

# function to connect to database
def connect_to_database():

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
    
    return conn
