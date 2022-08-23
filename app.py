from flask import Flask, request, jsonify
from database import *

app = Flask(__name__)


#  inherit db
class CM(MyDatabase):
    def __init__(self):
        self.app = Flask(__name__)
        MyDatabase.__init__(self)

    # create a student data
    def create_student(self):
        @self.app.route('/student', methods=['POST'])
        def create_student():
            try:
                data = request.get_json()
                self.insert_table_data_student(data)
                return data
            except Exception as error:
                print("Failed to do a post request {}".format(error))
            else:
                print("successful post request ")

    # create a teacher data
    def create_teacher(self):
        @self.app.route('/teacher', methods=['POST'])
        def create_teacher():
            try:
                data = request.get_json()
                self.insert_table_data_teacher(data)
                return data
            except Exception as error:
                print("Failed to do a post request {}".format(error))
            else:
                print("successful post request ")

    # get a list of students
    def get_student_details(self):
        @self.app.route('/student', methods=['GET'])
        def get_student_details():
            try:
                data = self.get_table_data_cms("STUDENT")
                return data
            except Exception as error:
                print("Failed to do a get request {}".format(error))
            else:
                print("successful get request ")

    # get a list of teachers
    def get_teacher_details(self):
        @self.app.route('/teacher', methods=['GET'])
        def get_teacher_details():
            try:
                data = self.get_table_data_cms("TEACHER")
                return data
            except Exception as error:
                print("Failed to do a get request {}".format(error))
            else:
                print("successful get request ")

    # add a class for students ( creating class for now )
    def create_class(self):
        @self.app.route('/class', methods=['POST'])
        def create_class():
            try:
                data = request.get_json()
                self.insert_table_data_class(data)
                return data
            except Exception as error:
                print("Failed to do a post request {}".format(error))
            else:
                print("successful post request ")
    # enrolls class for students
    def enroll_student(self):
        @self.app.route('/enroll/student', methods=['POST'])
        def enroll_student():
            try:
                data = request.get_json()
                self.insert_table_data_enroll_student(data)
                return data
            except Exception as error:
                print("Failed to do a post request {}".format(error))
            else:
                print("successful post request ")

    # assign that class for a student


# Run Server
if __name__ == '__main__':
    Test = CM()
    Test.create_student()
    Test.create_teacher()
    Test.get_teacher_details()
    Test.get_student_details()
    Test.create_class()
    Test.enroll_student()
    Test.app.run(debug=True)
