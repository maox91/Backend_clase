from models.student import Student
from repositories.studen_repository import StudentRepository

class StudentController:

    def __int__(self):
        """

        :return:
        """
        print ("Studen controller ready...")
        self.student_repository = StudentRepository()

    def index(self) -> list:
        """

        :return:
        """
        print("get all students")
        return self.student_repository.find_all()
    def show(self, id_) -> dict:
        """

        :param id_:
        :return:
        """
        print("get student")
        return self.student_repository.find_by_id(id_)

    def create (self, student_: dict) -> dict:
        """

        :param student_:
        :return:
        """
        print("insert student")
        student = Student(student_)
        return self.student_repository.save(student)

    def update(self, id_: str, student_: dict) ->dict:
        """

        :param id_:
        :param student_:
        :return:
        """
        print("update student")
        student = Student(student_)
        return  self.student_repository.update(id_, student)

    def delete(self, id_:str) -> dict:
        """

        :param id_:
        :return:
        """

        print("Delete student" + id_)
        return self.student_repository.delete(id_)