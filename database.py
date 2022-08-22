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

    def get_db_details(self, table_name='STUDENT'):

        ('SELECT * FROM ' + str(table_name))
        data = self.cursor.fetchall()
        return data

    def insert_table_data_student(self, data):
        try:
            query = 'Insert into STUDENT (ROLL_NO, FIRST_NAME, LAST_NAME) values (' + str(
                data["roll_no"]) + ',' + str(data["first_name"]) + ',"' + str(data["last_name"]) + '");'
            print(query)
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as error:
            print("Error inserting into database {}".format(error))
        else:
            print("Inserted data succcessfully into DB ")

    def update_table_data_student(self, data):
        try:
            query = 'UPDATE STUDENT set FIRST_NAME = "' + str(
                data["first_name"]) + '", LAST_NAME = "' + str(data["last_name"]) + '" WHERE ROLL_NO = ' + str(
                data['roll_no']) + ';'
            print(query)
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as error:
            print("Error updating into database {}".format(error))
        else:
            print("Updated data succcessfully into DB ")

    def insert_table_data_teacher(self, data):
        try:
            query = 'Insert into TEACHER (ID, FIRST_NAME, LAST_NAME) values (' + str(
                data["id"]) + ',' + str(data["first_name"]) + ',"' + str(data["last_name"]) + '");'
            print(query)
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as error:
            print("Error inserting into database {}".format(error))
        else:
            print("Inserted data succcessfully into DB ")

    def update_table_data_teacher(self, data):
        try:
            query = 'UPDATE TEACHER set FIRST_NAME = "' + str(
                data["first_name"]) + '", LAST_NAME = "' + str(data["last_name"]) + '" WHERE id = ' + str(
                data['id']) + ';'
            print(query)
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as error:
            print("Error updating into database {}".format(error))
        else:
            print("Updated data succcessfully into DB ")
