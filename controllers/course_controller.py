class CourseController:
    # contructor
    def __int__(self):
        print("Course controller ready...")

    # get all
    def index(self) -> list:
        """

        :return:
        """
        print("get all course")

    # get one by id
    def show(self,id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("get course")

    # insert
    def create(self, course_: dict) -> dict:
        """

        :param course_:
        :return:
        """
        print("Insert course")

    # update
    def update(self, id_: str, course_: dict) -> dict:
        """

        :param id_:
        :param course_:
        :return:
        """
        print("update course")

    # Delete
    def delete(self,id_: str) -> str: # la flecha indica que se espera que se retorne ese tipo de dato
        """

        :param id_:
        :return:
        """
        print("Delete course")
