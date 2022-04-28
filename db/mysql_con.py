import mysql.connector
from mysql.connector import errorcode
import os

config = {
    'user': os.environ[''],
    'password': os.environ[''],
    'host': os.environ[''],
    'database': os.environ[''],
    'raise_on_warnings': True
}

cnx = None


def get_connection():
    global cnx
    if cnx is not None:
        return cnx
    else:
        try:
            cnx = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.close()
    return cnx
