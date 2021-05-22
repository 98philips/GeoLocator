import mysql.connector
from os import environ

def getConnection():
    mydb = mysql.connector.connect(
        host="localhost",
        user=environ["DB_USER"],
        password=environ["DB_PASSWORD"],
        database=environ["DB_NAME"]
    )
    return mydb