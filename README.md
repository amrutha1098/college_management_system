# college_management_system
 This system should handle Teachers, Students, and Classes’ data. 



APIS ued :

Create STUDENT > /student [POST request]
BODY > {
"first_name" : str,
"last_name" : str
}

Create TEACHER > /teacher [POST request]
BODY > {
"first_name" : str,
"last_name" : str
}

Get STUDENT > /student [GET requet]
get data > 
 {
    "FIRST_NAME": str,
    "LAST_NAME": str,
    "ROLL_NO": str
}

Get TEACHER > /teacher [GET request]
get data > 
{
    "FIRST_NAME": str,
    "LAST_NAME": str,
    "id": str
}

Create CLASS > /class [POST request]
BODY > {
"class_name" : str,
"schedule_time" : datetime,
"teacher_id" : int
}

Create ENROLL > /enroll/student [POST request]
BODY > {
"roll_no" : int,
"class_name" : str
}

Get class list for a student in a day >> /class/student/<roll_no>/day/<date>
get requet data example >> 
{
    "data": [
        {
            "CNAME": "Sub4"
        },
        {
            "CNAME": "Sub1"
        }.....
    ]
}

Get class list for a teacher in a day  >> /class/teacher/<id>/day/<date>
get requet data example >> 
{
    "data": [
        {
            "CNAME": "Sub1"
        },
        {
            "CNAME": "Sub4"
        }
    ]
}
