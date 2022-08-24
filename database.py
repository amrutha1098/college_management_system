import mysql.connector
from constants import DB_USER, DB_HOST, DB_PASSWORD, DB_DATABASE


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
            query = 'Insert into STUDENT (FIRST_NAME, LAST_NAME) values ("'+ str(data["first_name"]) + '","' + str(data["last_name"]) + '");'
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
            query = 'Insert into TEACHER (FIRST_NAME, LAST_NAME) values ("' + str(data["first_name"]) + '","' + str(data["last_name"]) + '");'
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

    def insert_table_data_class(self, data):
        try:
            query = 'Insert into CLASS (CNAME, TIME, TEACHER_ID) values ("' + str(data["class_name"]) + '","' + str(
                data["schedule_time"]) + '",' + str(data["teacher_id"]) + ');'
            print(query)
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as error:
            print("Error inserting into database {}".format(error))
        else:
            print("Inserted data succcessfully into DB ")

    def insert_table_data_enroll_student(self, data):
        try:
            query = 'Insert into ENROLL (STUDENT_ID, CNAME) values ("' + str(data["roll_no"]) + '","' + str(
                data["class_name"]) + '");'
            print(query)
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as error:
            print("Error inserting into database {}".format(error))
        else:
            print("Inserted data succcessfully into DB ")


    def get_table_data_cms(self, table = "STUDENT"):
        try:
            query = 'SELECT * FROM  ' + str(table) + ';'
            print(query)
            self.cursor.execute(query)
            header = [row[0] for row in self.cursor.description]
            data = self.cursor.fetchall()
            print(data)
            data = self.convert_sql_to_json(header, data)
            print(data)
            return data
        except Exception as error:
            print("Error fetching the table data {}".format(error))
        else:
            print("Fetching data succcessfully from DB ")

    def convert_sql_to_json(self, headers, datas):
        return_list = []

        for data in datas:
            return_data = {}
            for header,value in zip(headers, data):
                return_data[header] = str(value)
            return_list.append(return_data)
        return_data = { "data" : return_list}
        return return_data

    def fetch_student_enrolled_class(self, roll_no, date):
        try:
            query = 'SELECT en.CNAME FROM ENROLL en join CLASS cl on en.CNAME = cl.CNAME WHERE en.STUDENT_ID = ' + str(roll_no)+ ' and cl.TIME LIKE "' + str(date + '%') + '";'
            print(query)
            self.cursor.execute(query)
            header = [row[0] for row in self.cursor.description]
            data = self.cursor.fetchall()
            print(data)
            data = self.convert_sql_to_json(header, data)
            print(data)
            return data
        except Exception as error:
            print("Error fetching the table data {}".format(error))
        else:
            print("Fetching data succcessfully from DB ")

    def fetch_teacher_assigned_class(self, id, date):
        try:
            query = 'SELECT CNAME FROM CLASS WHERE teacher_id = ' + str(id)+ ' and TIME LIKE "' + str(date + '%') + '";'
            print(query)
            self.cursor.execute(query)
            header = [row[0] for row in self.cursor.description]
            data = self.cursor.fetchall()
            print(data)
            data = self.convert_sql_to_json(header, data)
            print(data)
            return data
        except Exception as error:
            print("Error fetching the table data {}".format(error))
        else:
            print("Fetching data succcessfully from DB ")