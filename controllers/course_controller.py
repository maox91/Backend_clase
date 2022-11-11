from models.course import Course
from models.department import Department
from repositories.course_repository import CourseRepository
from repositories.department_repository import DepartmentRepository


class CourseController:
    # contructor
    def __int__(self):
        print("Course controller ready...")
        self.course_repository = CourseRepository()
        self.department_repository = DepartmentRepository()

    # get all
    def index(self) -> list:
        """

        :return:
        """
        print("get all course")
        self.course_repository.find_all()
    # get one by id
    def show(self,id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        return self.course_repository.find_by_id(id_)
        print("get course")

    # insert
    def create(self, course_: dict) -> dict:
        """

        :param course_:
        :return:
        """
        print("Insert course")
        course = Course(course_)
        return self.course_repository.save(course)
    # update
    def update(self, id_: str, course_: dict) -> dict:
        """

        :param id_:
        :param course_:
        :return:
        """
        print("update course")
        course = Course(course_)
        return self.course_repository.update(id_, course)


    # Delete
    def delete(self,id_: str) -> str: # la flecha indica que se espera que se retorne ese tipo de dato
        """

        :param id_:
        :return:
        """
        print("Delete course")
        self.course_repository.delete(id_)

    def department_assign(self,course_id: str, department_id: str) -> dict:
        """

        :param course_id:
        :param department_id:
        :return:
        """

        course_dict = self.course_repository.find_by_id(course_id)
        course_obj = Course(course_dict)
        department_dict = self.department_repository.find_by_id(department_id)
        department_obj = Department(department_dict)
        course_obj.department = department_obj
        return self.course_repository.save(course_obj)


