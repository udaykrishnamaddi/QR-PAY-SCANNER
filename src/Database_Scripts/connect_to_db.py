import os
from mysql import connector
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def get_db_obj():

    mydb = connector.connect( 
                host = "localhost", 
                user = os.getenv('MY_USERNAME'),
                password = os.getenv('MY_PASSWORD'),
                database = os.getenv('MYDB')
            )

    return mydb