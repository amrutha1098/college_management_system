import mysql.connector
from constants import *


class MyDatabase:
    connection = None
    cursor = None

    def __init__(self):
        if MyDatabase.connection is None:
            try:
                MyDatabase.connection = mysql.connector.connect(
                    host=DB_HOST,
                    user=DB_USER,
                    passwd=DB_PASSWORD,
                    database=DB_DATABASE
                )
                MyDatabase.cursor = MyDatabase.connection.cursor()
            except Exception as error:
                print("Error: Connection not established {}".format(error))
            else:
                print("Connection established")

        self.connection = MyDatabase.connection
        self.cursor = MyDatabase.cursor

