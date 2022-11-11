from models.enrollment import Enrollment
from models.course import Course
from models.student import Student
from repositories.enrollment_repository import EnrollmentRepository
from repositories.course_repository import CourseRepository
from repositories.studen_repository import StudentRepository


class EnrolmentController:

    def __int__(self):
        print("Enrolment controller ready ")
        self.enrollment_repository = EnrollmentRepository()
        self.course_repository = CourseRepository()
        self.student_repository = StudentRepository

    def index(self) -> list:
        """

        :return:
        """
        print("get all enrolment")
        return self.enrollment_repository.find.all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("get enrolment")
        self.enrollment_repository.find_by_id(id_)

    def get_student_by_course(self, course_id: str) -> list:
        """

        :param course_id:
        :return:
        """
        return self.enrollment_repository.get_enrrolment_by_course(course_id)

    def create(self, enrolment_: dict, course_id: str, student_id: str) -> dict:
        """

        :param student_id:
        :param course_id:
        :param enrolment_:
        :return:
        """
        print("insert enrolment")
        enrollment = Enrollment(enrolment_)
        course_dict = self.course_repository.find_by_id(enrollment)
        course_obj = Course(course_dict)
        student_dict = self.student_repository.find_by_id(student_id)
        student_obj = Student(student_dict)
        enrollment.course = course_obj
        enrollment.student = student_obj
        return self.enrollment_repository.save(enrollment)

    def update(self, id_: str, enrollment_: dict) -> dict:
        """

        :param id_:
        :param enrollment_:
        :return:
        """
        print("update enrollment")
        enrollment = Enrollment(enrollment_)
        return self.enrollment_repository.update(id_, enrollment)

    def delete(self, id_str) -> str:
        """

        :param id_str:
        :return:
        """
        print("Delete enrolment")
        return self.enrollment_repository(id_)
