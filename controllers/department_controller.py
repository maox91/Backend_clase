class DepartmentController:

    def __int__(self):
        print("department controller ready")

    def index(self) -> list:
        """

        :return:
        """
        print("get all department")

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("get department")

    def create(self, department_: dict) -> dict:
        """

        :param department_:
        :return:
        """
        print("insert department")

    def update(self, id_:str, department_: dict) -> dict:
        """

        :param id_:
        :param department_:
        :return:
        """
        print("update department")

    def delete(self, id_:str) -> str:
        """

        :param id_:
        :return:
        """
        print("delete department")