from models.department import Department
from repositories.department_repository import DepartmentRepository


class DepartmentController:

    def __int__(self):
        """

        :return:
        """
        print("department controller ready")
        self.department_repository = DepartmentRepository()

    def index(self) -> list:
        """

        :return:
        """
        print("get all department")
        self.department_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("get department")
        return self.department_repositoryment.find_by_id(id_)


    def create(self, department_: dict) -> dict:
        """

        :param department_:
        :return:
        """
        print("insert department")
        department = Department(department_)
        return self.department_repository.save(department)

    def update(self, id_: str, deparment_: dict) -> dict:
        """

        :param id_:
        :param department_:
        :return:
        """
        print("update department")
        deparment = Department(deparment_)
        return self.department_repository.update(id_, deparment)

    def delete(self, id_:str) -> str:
        """

        :param id_:
        :return:
        """
        print("delete department")
        return self.department_repository.delete(id_)