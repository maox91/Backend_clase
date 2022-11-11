from models.enrollment import Enrollment
from repositories.interfaceRepository import InterfaceRepository


class ReportsRepository(InterfaceRepository[Enrollment]):
    def get_highest_grade(self):
        query_aggregation =  {
            "_id": "$course",
            "max" = {"$max" : "$grade"},
            "enrollment": {"$first": "$$ROOT"}

        }

        pipeline= [query_aggregation]
        return self.query_aggregation(pipeline)