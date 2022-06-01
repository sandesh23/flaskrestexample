import json
from studentinfo import Student,db,app
from studentserviceimpl import StudentServiceImpl
from flask import request
impl = StudentServiceImpl()


@app.route("/stud/", methods = ['POST'])
def add_student():
    req_obj = request.get_json()
    print(type(req_obj))
    sid = 0
    stud = Student(sid= sid, name = req_obj.get('name'), cls = req_obj.get("cls"),
                   div = req_obj.get('div'))
    impl.add_student(stud)
    response_dict = {"Message": "Student Added Successfully"}
    return json.dumps(response_dict)

@app.route("/stud/", methods= ['GET'])
def student_data():
    students = impl.get_all_students()
    dict_of_students = {}
    for student in students:
        student.__dict__.pop('_sa_instance_state')
        dict_of_students[student.sid] = student.__dict__
    print(dict_of_students)
    return json.dumps(dict_of_students)

@app.route("/stud/<int:sid>", methods = ["GET"])
def search_student(sid):
    student = impl.get_student_info(sid =sid)
    student.__dict__.pop('_sa_instance_state')
    return json.dumps(student.__dict__)

@app.route("/stud/<int:sid>", methods = ['PUT'])
def update_student(sid):
    req_obj = request.get_json()
    stud = Student(sid = sid, name = req_obj.get('name'), cls = req_obj.get('cls'),
                   div = req_obj.get('div'))
    impl.update_student_info(stud)
    response_dict = {'message': "Student Updated Successfully"}
    return json.dumps(response_dict)

@app.route("/stud/<int:sid>", methods = ['DELETE'])
def delete_student(sid):
    impl.delete_student_info(sid)
    return json.dumps({"message": "Student Deleted Successfully"})

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)