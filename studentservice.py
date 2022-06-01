from abc import ABC, abstractmethod

class StudentService(ABC):

    @abstractmethod
    def add_student(self, student):
        pass

    @abstractmethod
    def get_student_info(self, sid):
        pass

    @abstractmethod
    def get_all_students(self):
        pass

    @abstractmethod
    def update_student_info(self, student):
        pass

    @abstractmethod
    def delete_student_info(self, sid):
        pass