from studentservice import StudentService
from studentinfo import Student,db

class StudentServiceImpl(StudentService):

    def add_student(self, student):
        student_in_db = self.get_student_info(student.sid)
        if not student_in_db:
            db.session.add(student)
            db.session.commit()
        else:
            print("Student already exist")


    def get_student_info(self, sid):
        return Student.query.filter_by(sid=sid).first()

    def get_all_students(self):
        return Student.query.all()

    def update_student_info(self, student):
        student_in_db = self.get_student_info(student.sid)
        if student_in_db:
            student_in_db.sid = student.sid
            student_in_db.name  = student.name
            student_in_db.cls = student.cls
            student_in_db.div = student.div
            db.session.commit()
        else:
            print("Student not available")

    def delete_student_info(self, sid):
        student_in_db = self.get_student_info(sid)
        if student_in_db:
            db.session.delete(student_in_db)
            db.session.commit()
        else:
            print("student does not exist")