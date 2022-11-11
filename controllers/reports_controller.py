from repositories.reports_repository import ReportsRepository

class ReportsController():
    def __int__(self):
        self.reports_repository = ReportsRepository()

    def get_highest_grade(self):
        return self.reports_repository.get_highest_grade()
