

from flask import Flask, request, jsonify
from database import *

app = Flask(__name__)


#  inherit db
class CM(MyDatabase)
    def __init__(self):
        pass
    # create a student data
    # create a teacher data

    # get a list of students
    # get a list of teachers

    # add a class for students
    # assign that class for a student


# Run Server
if __name__ == '__main__':
  app.run(debug=True)