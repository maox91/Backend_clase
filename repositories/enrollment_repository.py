from bson import ObjectId
from models.enrollment import Enrollment
from repositories.interfaceRepository import InterfaceRepository


class EnrollmentRepository(InterfaceRepository[Enrollment]):
    def get_enrollments_by_course(self, course_id: str) -> list:
        query_dict = {"course.$id": ObjectId(course_id)}
        return self.query(query_dict)

