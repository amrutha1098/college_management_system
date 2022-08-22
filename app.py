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
        def create_student():
            try:
                data = request.get_json()
                self.insert_table_data_teacher(data)
                return data
            except Exception as error:
                print("Failed to do a post request {}".format(error))
            else:
                print("successful post request ")

    # get a list of students
    # get a list of teachers

    # add a class for students
    # assign that class for a student


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
